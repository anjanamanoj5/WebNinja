import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

def Openrediretion(linksalls,s):
	c=0
	def Openred(urls):
		for i in payload:
			"""
			response = s.get(i)
			abc = BeautifulSoup(response.content, 'html.parser')
			ab=str(abc)
			"""
			req=urls+i
			response = s.get(req,allow_redirects=True)
			soup = BeautifulSoup(response.content, 'html.parser')
			sou=str(soup)
			f=re.search(i,response.url)
			if f:
				c=1
				print(req+ " is vulnerable to open riderection")
				break
		return c
		
	def initial(parameter):
		if "=" in parameter:
			x = parameter.split("=")
			print(x)
			m=len(x)
			if m==2:
				craftedurl=x[0]+"="
		else:
			craftedurl=parameter+"/"
		return craftedurl
	
	payload=["https://www.google.com"]
	for i in linksalls:
		urls=initial(i)
		c=Openred(urls)
		if c==1:
			break
