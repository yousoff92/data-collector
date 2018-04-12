from enum import Enum

class General(Enum):
  JOBSTREET_URL = "https://www.jobstreet.com.my/en/job-search/job-vacancy.php"
  CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

  # If set to 10, it will retrieve 10 pages with latest jobs. Set to -1 to get all available job.  
  PAGE_THRESHOLD = 3 

class Authentication(Enum):
  JOBSTREET_USERNAME = "" # Put your username, its better to use other than your official account
  JOBSTREET_PASSWORD = "" # Put your password
  JOBSTREET_LOGIN_URL = "https://myjobstreet.jobstreet.com.my/home/login.php?site=MY&language_code=3&nrfr=1&go=JOB-ADS"

class Location(Enum):
  JOHOR	= 50100
  KEDAH	= 50200
  KELANTAN = 50400
  KUALA_LUMPUR = 	50300
  LABUAN	= 51500
  MELAKA = 50500
  NEGERI_SEMBILAN =	50600
  PAHANG =	50800
  PENANG =	50700
  PERAK	= 50900
  PERLIS =	51000
  PUTRAJAYA =	51600
  SABAH	= 51100
  SARAWAK	= 51300
  SELANGOR = 51200
  TERENGGANU = 51400
