import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

def SSTIVuln(url,s,param):
	payloads1=["{{7*7}}","${7*7}","<%= 7*7 %>","${{7*7}}","#{7*7}","*{7*7}","{{7*'7'}}"]
	dict=[{"payload":"{{7*7}}","template" :"Twig (PHP) or NUNJUCKS (NodeJS) or Tornado (Python)"},{"payload":"${7*7}","template" :"java or freemarker"},{"payload":"<%= 7*7 %>","template" :"ERB (Ruby) or ASP or Mojolicious (Perl)"},{"payload":"${{7*7}}","template" :"Expression Language - EL (Java) or java"},{"payload":"#{7*7}","template" :"Expression Language - EL (Java) or PugJs (NodeJS) or Slim"},{"payload":"*{7*7}","template" :"Spring"},{"payload":"{{7*'7'}}","template" :"Jinja2 (Python) or Tornado (Python)"}]
	def dirinit(ins):
		if "=" in ins:
			x = ins.split("=")
			m=len(x)
			if m==2:
				xx=x[0]+"="
				SSTI(xx)
			if m==3:
				xx=x[0]+"="+x[1]+"="
				SSTI(xx)
		else:
			SSTI(ins)
	def SSTI(i):
		for j in payloads1:
			newurl=i+j
			response = s.get(newurl)
			soup = BeautifulSoup(response.content, 'html.parser')
			sou=str(soup)
			if "49" in sou:
				for d in dict:
    					if d['payload'] == j:
    						print(newurl+" is vulnerable to ssti")
    						print("It might be"+d['template'])
			
	for i in param:
		dirinit(i)
