from enum import Enum

class General(Enum):
  MUDAH_URL = "http://www.mudah.my"
  CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

class Region(Enum):
  KUALA_LUMPUR = "/Kuala-Lumpur"
  SELANGOR = "/Selangor"
  NEIGHBOURING = "/Neighbouring-9"
  ENTIRE_MALAYSIA = "/Malaysia"
  JOHOR =  "/Johor"
  KEDAH =  "/Kedah"
  KELANTAN = "/Kelantan"
  LABUAN = "/Labuan"
  MELAKA = "/Melaka"
  NEGERI_SEMBILAN = "/Negeri-Sembilan"
  PAHANG =  "/Pahang"
  PENANG = "/Penang"
  PERAK = "/Perak"
  PERLIS = "/Perlis"
  PUTRAJAYA = "/Putrajaya"
  SABAH = "/Sabah"
  SARAWAK = "/Sarawak"
  TERENGGANU = "/Terengganu"

class PropertyCategory(Enum):
  APARTMENT = "/Apartments-for-rent-2020"
  HOUSE = "/Houses-for-rent-2040"
  COMMERCIAL = "/Commercial-Properties-for-rent-2060"
  LANDED = "/Land-for-rent-2080"
  ROOM = "/Rooms-for-rent-2100"