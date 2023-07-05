import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

def Cors(url,s,linksalls):
	def cors(i):
		headers = {'Origin': 'www.example.com'}
		response = s.get(i,headers=headers)
		newhead=response.headers
		head=str(newhead)
		sear=["Access-Control-Allow-Origin: www.example.com","Access-Control-Allow-Credentials: true","Access-Control-Allow-Origin: *"]
		for j in sear:
			x = re.search(j,head)
			if x:
				print(i+" is vulnerable to cors")
				break
	headers = {'Origin': 'www.example.com'}
	for i in linksalls:
		cors(i)
