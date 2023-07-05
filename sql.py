import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

def SQL(param,linksalls,s):
	listt=[]
	def getallforms(url):
		res=s.get(url)
		soup=BeautifulSoup(res.content,"html.parser")
		m=soup.find_all('form')
		return m
	def SqlErrorCheck(url):
		for i in errpayload:
			newurl=url+i
			response = s.get(newurl)
			soup = BeautifulSoup(response.content, 'html.parser')
			sou=str(soup)
			for j in errshow:
				found = re.search(j,sou)
				if found:
					print(newurl+" is vulneraable to sql injection")
	def submitform(form,payload,url):
		if form["method"].lower()=="get":
			data={}
			for input_tag in form.find_all("input"):
				print(input_tag)
		
				if input_tag["type"]=="submit":
					data.update({input_tag["name"]:input_tag["name"]})
				else:
					data.update({input_tag["name"]:payload})
			for textareas in form.find_all("textarea"):	
				data.update({textareas["name"]:payload})
			res = s.get(url, params=data)
			soup = BeautifulSoup(response.content, 'html.parser')
			sou=str(soup)
			print(sou)
			for j in errshow:
				found = re.search(j,sou)
				if found:
					print(newurl+" is vulneraable to sql injection")
		if form["method"].lower()=="post":
			data={}
			for input_tag in form.find_all("input"):
				print(input_tag)	
				if input_tag["type"]=="submit":
					data.update({input_tag["name"]:input_tag["name"]})
				else:
					data.update({input_tag["name"]:payload})
			for textareas in form.find_all("textarea"):	
				data.update({textareas["name"]:payload})
			res = s.post(url, data=data)
			soup = BeautifulSoup(response.content, 'html.parser')
			sou=str(soup)
			print(sou)
			for j in errshow:
				found = re.search(j,sou)
				if found:
					print(newurl+" is vulneraable to sql injection")
		else:
			data={}
			for input_tag in form.find_all("input"):
				print(input_tag)
				if input_tag["type"]=="submit":
					data.update({input_tag["name"]:input_tag["name"]})
				else:
					data.update({input_tag["name"]:payload})
			for textareas in form.find_all("textarea"):	
				data.update({textareas["name"]:payload})
			res = s.get(url, params=data)
			if payloads in res.text:
				print("xss")
			else:
				print("no xss")
	errshow=[r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"MySQL Query fail.*", r"SQL syntax.*MariaDB server",r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"Warning.*PostgreSQL",r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*odbc_.*", r"Warning.*mssql_", r"Msg \d+, Level \d+, State \d+", r"Unclosed quotation mark after the character string", r"Microsoft OLE DB Provider for ODBC Drivers",r"Microsoft Access Driver", r"Access Database Engine", r"Microsoft JET Database Engine", r".*Syntax error.*query expression",r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Warning.*oci_.*", "Microsoft OLE DB Provider for Oracle"r"CLI Driver.*DB2", r"DB2 SQL error"r"SQLite/JDBCDriver", r"System.Data.SQLite.SQLiteException",r"Warning.*ibase_.*", r"com.informix.jdbc",r"Warning.*sybase.*", r"Sybase message"]
	errpayload=["\"","'"]
	for i in param:
		SqlErrorCheck(i)
	for li in linksalls:
		u=getallforms(li)
		print(u)		
		for j in u:
			if j in listt:
				break
			else:
				listt.append(j)
			for i in errpayload:
				submitform(j,i,li)
