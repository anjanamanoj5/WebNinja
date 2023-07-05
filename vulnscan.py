import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys
from crawl import *
from cors import *
from dir import *
from cmdinj import *
from clickjacking import *
from ssti import *
from open import *
from xss import *
from sql import *
s = requests.Session()
print("Enter url")
urll=input()
param,linksalls=Crawler(urll,s)
Cors(urll,s,linksalls)
Dirtraversal(urll,s,param)
Cmdinjection(urll,s,param)
Clickjacking(urll,s)
Openrediretion(linksalls,s)
SSTIVuln(urll,s,param)
XSS(param,linksalls,s)
SQL(param,linksalls,s)
