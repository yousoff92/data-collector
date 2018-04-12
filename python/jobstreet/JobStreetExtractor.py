"""
Python source code to extract listing from mudah.my

"""
from functools import total_ordering
from jobstreet.config import General, Authentication, Location

import pandas as pd
import requests
import webbrowser as web
import urllib.parse as urlparse
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import dateutil.relativedelta as rd
import math
import mechanicalsoup

import os
clear = lambda: os.system('cls') #on Windows System

# TODO - Advance criteria
# TODO - Logging

class JobStreetExtractor:
    """
    Extractor for getting job dataset from jobstreet malaysia
    """
    __chrome_path__ = General.CHROME_PATH.value
    __base_url__ = General.JOBSTREET_URL.value

    # Mapping values to required Jobstreet parameter
    # https://www.jobstreet.com.my/en/job-search/job-vacancy.php?key=Software&area=2&location=51200&position=3%2C4&job-type=5&experience-min=03&experience-max=-1&salary=6%2C000
    # &salary-max=7%2C000&classified=1&salary-option=on&job-posted=0&src=1&ojs=4
    # key
    # area
    # location
    # position
    # job-type  : 5,10,16
    # experience-min
    # experience-max
    # salary
    # salary-max
    # classified
    # salary-option
    # job-posted
    # src
    # ojs
    # sort
    # order
    # pg
    def __authenticate__(self):
        login_url = Authentication.JOBSTREET_LOGIN_URL.value
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(login_url)
        browser.select_form('#login')
        browser['login_id'] = Authentication.JOBSTREET_USERNAME.value
        browser['password'] = Authentication.JOBSTREET_PASSWORD.value
        browser.submit_selected()
        return browser

    def __scraping__(self, keyword=None, location=None, minSalary=None, maxSalary=None, minExperience=None, maxExperience=None):

        # login
        browser = self.__authenticate__(self)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

        # construct filter criteria
        filter_criteria = {}
        if keyword is not None:
          filter_criteria.update({'key': keyword })

        if location is not None:
          filter_criteria.update({'location' : location.value })

        if minSalary is not None:
          filter_criteria.update({'salary' : minSalary })

        if maxSalary is not None:
          filter_criteria.update({'salary-max' : maxSalary })

        if minExperience is not None:
          filter_criteria.update({'experience-min' : minExperience })

        if maxExperience is not None:
          filter_criteria.update({'experience-max' : maxExperience })

        # filter_criteria = {
        #             'key':'Software',
        #             'area': '2',
        #             'location':'51200',
        #             'position':'3,4',
        #             'job-type':'5',
        #             'salary':'6000',
        #             'salary-max':'7000',
        #             'classified':'1',
        #             'salary-option':'on',
        #             'job-posted':'0',
        #             'src':'1',
        #             'ojs':'4',
        #         }

        page_url = self.__base_url__
        url_parts = list(urlparse.urlparse(page_url))

        final_df = pd.DataFrame()

        # test to get number of pages
        page_criteria = {'pg': str(1)}
        filter_criteria.update(page_criteria)
        url_parts[4] = urlencode(filter_criteria)
        page_url = urlparse.urlunparse(url_parts)

        response = browser.open(page_url)
        print(page_url)

         # get total lists
        total_list = BeautifulSoup(response.content, "html.parser").find("span", class_="pagination-result-count").string

        pages = 1

        if total_list is not None:
          print(total_list)
          total_list = total_list[total_list.find("of")+len("of"):total_list.rfind("jobs")]
          total_list = total_list.strip().replace(',', '')
          print("Attempt to parse " + str(total_list) + " jobs at most")

          pages = math.ceil(int(total_list) / 40)  # 40 is item per page

        # To prevent over-scraping
        if General.PAGE_THRESHOLD.value != -1 and General.PAGE_THRESHOLD.value < pages :
          pages = General.PAGE_THRESHOLD.value

        for page in range(1, pages + 1):

            job_titles = []
            job_urls = []
            com_names = []
            com_urls = []

            locations = []
            salaries = []
            descriptions = []

            page_criteria = {'pg': str(page)}
            filter_criteria.update(page_criteria)
            url_parts[4] = urlencode(filter_criteria)
            page_url = urlparse.urlunparse(url_parts)

            print(page_url)
            response = browser.open(page_url)

            if response.status_code != 200:
              raise ConnectionError("Cannot connect to " + page_url)

            #raw_listing = BeautifulSoup(response.content, "html.parser").find_all("div", {'id': 'job_listing_panel'})
            raw_listing = BeautifulSoup(response.content, "html.parser").find_all("div",
                                {
                                    'id' : lambda value: value and value.startswith("job_ad"),
                                    'itemtype' : 'http://schema.org/JobPosting'
                                })


            for element in raw_listing:

                job_el = element.find("a", {'id' : lambda value: value and value.startswith("position_title")})
                job_titles.append(job_el.get('data-job-title'))
                job_urls.append(job_el.get('href'))

                com_el = element.find("a", {'id' : lambda value: value and value.startswith("company_name")})

                if com_el is None:
                    com_el = element.find("span", {'id': lambda value: value and value.startswith("company_name")})
                    com_names.append(com_el.string)
                    com_urls.append(None)

                else:
                    com_names.append(com_el.find('span').string)
                    com_urls.append(com_el.get('href'))

                loc_el = element.find("li", {'class' : 'job-location'})
                locations.append(loc_el.get('title'))

                sal_el =  element.find("li", {'id' : 'job_salary'})

                if sal_el:
                    salaries.append(sal_el.find("font").string)
                else:
                    salaries.append(None)

                des_el = element.find("li", {'itemprop' : 'description'})
                descriptions.append(des_el.string)

            df = pd.concat([pd.Series(job_titles),
                            pd.Series(job_urls),
                            pd.Series(com_names),
                            pd.Series(com_urls),
                            pd.Series(locations),
                            pd.Series(salaries),
                            pd.Series(descriptions),
                            ], axis=1)

            df.columns = [["Job Titles", "Job URLS", "Company Name", "Company URLS", "Location", "Salaries", "Descriptions"]]
            final_df = final_df.append(df, ignore_index=True)

        return final_df
        print("Parsing has ended...")

    @classmethod
    def find_jobs(cls, keyword=None, location=None, minSalary=None, maxSalary=None, minExperience=None, maxExperience=None):

        df = cls.__scraping__(cls, keyword=keyword, location=location, minSalary=minSalary, maxSalary=maxSalary, minExperience=minExperience, maxExperience=maxExperience)

        # Export to excel
        filename = "Jobstreet " + datetime.today().strftime('%Y%m%d%H%M%S') + ".xlsx"

        # BUG - index False cause column jadi pelik
        df.to_excel(filename, sheet_name="Jobstreet", header=True, index=False)
        return