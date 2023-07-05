import requests
from bs4 import BeautifulSoup
import re
def Clickjacking(urll,s):
	response = s.get(urll)
	if not "X-Frame-Options" in response.headers:
		print(urll+ " is vulnerable to clickjking")
	else:
		print("it is not vulnerable")
