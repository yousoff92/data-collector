"""
Python source code to extract listing from mudah.my

"""
from functools import total_ordering
from mudah.config import General, Region, PropertyCategory, SupportedPropertyRegionArea, PropertyArea

import pandas as pd
import requests
import webbrowser as web
import urllib.parse as urlparse
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import dateutil.relativedelta as rd
import math

# TODO - Change print to logging

class PropertyExtractor:
    """
    Extractor for getting property dataset from mudah.my
    """

    __base_url__ = General.MUDAH_URL.value
    __chrome_path__ = General.CHROME_PATH.value

    # scraping from mudah.my. Will collect every properties
    def __scraping__(self, region, property_category, search_area, wanted_region=[]):
        """
        Class method to scrap data from mudah.my

        :param region:
            :type Region

        :param property_category:
            :type PropertyCategory

        :param wanted_region:
            :type List of String

        :return:
            :type pandas.core.frame.DataFrame
        """

        # Add search criteria
        print(region.value)
        print(property_category.value)
        search_criteria = [region.value, property_category.value]

        # Add advance criteria, dependent on property_category
        filter_criteria = {}
        hide_images = {'th': '1'}
        max_monthly_rent = {'mre': '2'}
        max_sqft = {'se': '1'}

        if search_area is not None:
          pass

        filter_criteria.update(hide_images)
        filter_criteria.update(max_monthly_rent)
        filter_criteria.update(max_sqft)

        # Combine URL, search and filter criteria here.
        page_url = self.__base_url__ + ''.join(search_criteria)
        url_parts = list(urlparse.urlparse(page_url))

        # Init request to get total list
        url_parts[4] = urlencode(filter_criteria)
        page_url = urlparse.urlunparse(url_parts)
        result = requests.get(page_url)

        if result.status_code != 200:
            raise ConnectionError("Cannot connect to " + page_url)

        # get total lists
        total_list = BeautifulSoup(result.content).find("div", class_="list-total").string
        print("Attempt to parse " + total_list + " properties at most")
        pages = math.ceil(int(total_list) / 40)  # 40 is item per page

        # only choose up to last 1 months
        minimum_date_posted = datetime.now() + rd.relativedelta(months=-1)
        exceed_minimum = False

        titles = []
        prices = []
        links = []
        bedrooms = []
        bathrooms = []
        sizes = []
        areas = []
        dates_posted = []

        final_df = pd.DataFrame()
        
        # To prevent over-scraping
        if General.PAGE_THRESHOLD.value != -1 and General.PAGE_THRESHOLD.value < pages :
          pages = General.PAGE_THRESHOLD.value

        for page in range(1, pages + 1):

            if exceed_minimum:
                break

            # request page
            page_criteria = {'o': str(page)}
            filter_criteria.update(page_criteria)
            url_parts[4] = urlencode(filter_criteria)
            page_url = urlparse.urlunparse(url_parts)

            print("Parsing page " + str(page) + " ... " + page_url)
            result = requests.get(page_url)

            if result.status_code != 200:
                raise ConnectionError("Cannot connect to " + page_url)

            raw_listing = BeautifulSoup(result.content).find_all("div", {'class': 'list_ads'})

            for element in raw_listing:

                temp = element.find("h2", class_="list_title")

                if temp is None:
                    continue

                if not temp.contents[0] is None:
                    temp = temp.contents[0]
                    title = temp.string

                    if title is None:
                        continue
                    else:
                        title = title.strip()

                    link = temp.get("href")

                price = self.__get_el_string__(element.find("div", class_="ads_price"))
                if not price == "":
                    price = int(price.replace("RM", "").replace("per month", "").strip().replace(" ", ""))
                else:
                    price = 0

                bedroom = self.__get_el_string__(element.find("div", class_="bedroom"))
                bathroom = self.__get_el_string__(element.find("div", class_="bathroom"))
                
                # House square feet
                size = self.__get_el_string__(element.find("div", class_="size"))
                if not size == "":
                    size = float(size.replace(" sq.ft", ""))
                else:
                    size = 0

                temp = element.find("div", class_="location")

                if temp is None:
                    area = ""
                    date_posted = ""
                else:
                    temp = temp.contents
                    area = temp[3].string.strip()
                    date_posted = temp[1].string.strip()

                    if date_posted.split(",")[0] == 'Today':
                        date_posted = datetime.now().strftime("%d %b %Y") + ", " + date_posted.split(",")[1]
                    elif date_posted.split(",")[0] == 'Yesterday':
                        date_posted = (datetime.now() - timedelta(days=1)).strftime("%d %b %Y") + ", " + \
                                      date_posted.split(",")[1]
                    else:
                        # sometime their system is weird
                        temp = datetime.strptime(date_posted.split(",")[0], "%d %b").replace(year=datetime.now().year)

                        if temp > datetime.now():
                            temp = temp.replace(year=datetime.now().year - 1)

                        if temp < minimum_date_posted:
                            exceed_minimum = True
                            break

                        date_posted = temp.strftime("%d %b %Y") + ", " + date_posted.split(",")[1]

                titles.append(title)
                links.append(link)
                prices.append(price)
                bedrooms.append(bedroom)
                bathrooms.append(bathroom)
                sizes.append(size)
                areas.append(area)
                dates_posted.append(date_posted)

            df = pd.concat([pd.Series(titles),
                            pd.Series(areas),
                            pd.Series(sizes),
                            pd.Series(dates_posted),
                            pd.Series(bedrooms),
                            pd.Series(bathrooms),
                            pd.Series(prices),
                            pd.Series(links)], axis=1)
            df.columns = [["Title", "Area", "Size", "Date Posted", "Bedroom", "Bathroom", "Price", "Links"]]
            final_df = final_df.append(df, ignore_index=True)

            titles.clear()
            prices.clear()
            links.clear()
            bedrooms.clear()
            bathrooms.clear()
            sizes.clear()
            areas.clear()
            dates_posted.clear()

        print("Parsing has ended...")

        # FIXED - Yousoff : Multi index bug
        final_df.columns = final_df.columns.get_level_values(0)
        final_df["Date Posted"] = pd.to_datetime(final_df["Date Posted"])
        return final_df

    @classmethod
    def find_properties(cls, region=Region.KUALA_LUMPUR, property_category=PropertyCategory.APARTMENT, search_area=None, wanted_areas=[],
                        unwanted_areas=[]):
        """

        Find datasets by providing any search and filter criterias.

        :param region: Example Region.KUALA_LUMPUR
            :type Region

        :param property_category : Example PropertyCategory.APARTMENT
            :type PropertyCategory

        :param wanted_area: Not yet implemented
            :type List of String

        :param unwanted_area: Not yet implemented
            :type List of String

        :return:
            :type pandas.core.frame.DataFrame

            Return dataset of properties with given criterias

        """

        # Scraping from URL
        df = cls.__scraping__(cls, region, property_category, search_area)

        # Filter results from scraping
        minimum_rental = 400
        df = cls.__filtering__(cls, df, unwanted_areas, minimum_rental)

        # Export to excel
        filename = "Mudah Properties " + datetime.today().strftime('%Y%m%d%H%M%S') + ".xlsx"

        # BUG - index False cause column jadi pelik
        df.to_excel(filename, sheet_name="" + region.name + " - " + property_category.name, header=True,
                    index=False)
        return df

    @classmethod
    def read_excel(cls):
        return pd.read_excel("properties.xlsx")

    def __filtering__(self, df, unwanted_areas, minimum_rental):
        df = df.loc[~df['Area'].isin(unwanted_areas)]
        df = df[df["Price"] > minimum_rental]
        return df

    def __get_el_string__(element):
        if element is None:
            return ""
        else:
            t = element.string
            if t is not None :
                return t.strip()
            else:
                return ""

