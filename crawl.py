import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

def Crawler(urll,s):
	def urlcheck(ur):
		if ur[0:4]!="http":
			ur="http://"+ur
		if ur.endswith("--"):
			return ur[:-2]
		if ur.endswith("/*"):
			return ur[:-2]
		if ur.endswith("*"):
			return ur[:-1]
		if ur.endswith("#"):
			return ur[:-1]
		if ur.endswith("/"):
			return ur[:-1]
		return ur

	def url_crawl(url):
		def urlcrawl(url):
			hreflinks=[]
			response = s.get(url)
			soup = BeautifulSoup(response.content, 'html.parser')
			init_links=[]
			links=soup.findAll('a')
			for link in links:
				m=link.get('href')
				init_links.append(m)
			return init_links	
		web=url
		init_links=urlcrawl(web)
		pp=[]
		for i in init_links:
        		pp.append(i)
		return pp


	def crawl_check(p):
		l=len(p)
		for i in range(l):
			if p[i].startswith("mailto:"):
				extra.append(p[i])
				p[i]=""
			if p[i].startswith("javascript:"):
				extra.append(p[i])
				p[i]=""
			if p[i].startswith("tel:"):
				extra.append(p[i])
				p[i]=""
			if p[i]=="#":
				p[i]=""
			if p[i].startswith("http:") or p[i].startswith("https:"):
				if base not in p[i]:
					extra.append(p[i])
					p[i]=""
		p = list(filter(None, p))
		pp=[]
		for i in p:
        		pp.append(i)
		return pp
				
	def new_url(p1,urln):
		l=len(p1)
		for i in range(l):
			if p1[i].startswith("http:") or p1[i].startswith("https"):
				continue
			else:
				p1[i]=urljoin(urln,p1[i])
		pp=[]
		for i in p1:
        		pp.append(i)
		return pp
	
	def paramsfetch(newlinks):
		for i in newlinks:
			if "=" in i:
				params.append(i)
	def updates(newurl):
		sam_list=[]
		urln=newurl
		p=url_crawl(urln)
		p1=crawl_check(p)
		p2=new_url(p1,urln)
		paramsfetch(p2)
		for i in p2: 
    			if i not in sam_list: 
        			sam_list.append(i) 
		for i in sam_list:
        		linksall.append(i)		
		return sam_list
	def repeatparse(newlinks):
		for i in newlinks:
			m=updates(i)
			l=len(m)
			for j in range(l):
				if m[j] in linkssuu:
					m[j]=""
				else:
					linkssuu.append(m[j])
			m = list(filter(None, m))	
			if m!=0:			
				repeatparse(m)
			else:
				print(0)
			
	url=urll
	params=[]
	linksall=[]
	extra=[]
	base=url
	newurl=urlcheck(url)
	uu=updates(newurl)
	linkssuu=uu
	repeatparse(uu)


	param=[]
	linksalls=[]
	linksalls.append(url)
	for i in params: 
    		if i not in param: 
        		param.append(i)
	for i in linksall: 
		if i not in linksalls: 
        		linksalls.append(i)      
	print(param)
	print(linksalls)
	return param,linksalls
