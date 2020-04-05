# -*- coding: utf-8 -*-
try:
	from lib.domain import Domain
	from lib.spider import spider
	from lib.subdomain import Subdomain
	import argparse
	from colorama import Fore
	from time import sleep
	import os
	from random import choice

	class Eyes:
		def __init__(self):
			parse = self.parser()
			if  parse == None:
				pass
			else:
				self.url = parse.url
				self.select = parse.select
				self.output = parse.output
				self.settings()
		def parser(self):
			parseObject = argparse.ArgumentParser()
			parseObject.add_argument("-u",dest="url", help="enter url: 'https://www.example.com'")
			parseObject.add_argument("-s",dest="select", help="method: [1]spider, [2]subdomain, [3]domain ")
			parseObject.add_argument("-o",dest="output", help="output: noname.txt")
			parse = parseObject.parse_args()
			if  "http" not in parse.url :
				print(Fore.YELLOW+"usage: main.py [-h] [--help]")
				return None
			else:
				return parse

		def settings(self):
			os.system('cls' if os.name == 'nt' else 'clear')
			print(self.show())

			if self.select == "1":
				print(Fore.YELLOW+"\t"+"*"*7,"SPIDER",Fore.YELLOW+"*"*7)
				x = spider(self.url)
				self.write(x)

			elif self.select == "2":
				print(Fore.YELLOW+"\t"+"*"*7,"SUBDOMAIN",Fore.YELLOW+"*"*7)
				Subdomain(self.url,self.output)
			elif self.select == "3":
				print(Fore.YELLOW+"\t"+"*"*7,"DOMAIN",Fore.YELLOW+"*"*7)
				Domain(self.url,self.output)
			else:
				print(Fore.YELLOW+"\t"+"*"*7,"DEFAULT: SPIDER",Fore.YELLOW+"*"*7)
				x = spider(self.url)
				self.write(x )
		def write(self,urls):
			if self.output != None:
				with open(self.output, "w", encoding="utf-8") as file:
					for i in urls:
						file.write("="*30+"\n")
						file.write("| " + i +"\n")
						file.write("="*30+"\n")
				if len(urls) == 0:
					print(Fore.GREEN+f"\n[+] Created {self.output} but list is empty")
				else:
					print(Fore.GREEN+"\n[+] Created "+self.output)



		def show(self):
			dizi = ["""
	'##::::::::'########:'##:::'##:'########::'######::
	 ##:::'##:: ##.....::. ##:'##:: ##.....::'##... ##:
	 ##::: ##:: ##::::::::. ####::: ##::::::: ##:::..::
	 ##::: ##:: ######:::::. ##:::: ######:::. ######::
	 #########: ##...::::::: ##:::: ##...:::::..... ##:
	...... ##:: ##:::::::::: ##:::: ##:::::::'##::: ##:
	:::::: ##:: ########:::: ##:::: ########:. ######::
	::::::..:::........:::::..:::::........:::......:::
	
				""","""
	   __ __  ______               
	  / // / / ____/_  _____  _____
	 / // /_/ __/ / / / / _ \/ ___/
	/__  __/ /___/ /_/ /  __(__  ) 
	  /_/ /_____/\__, /\___/____/  
				/____/             
				
				""","""
	██╗  ██╗███████╗██╗   ██╗███████╗███████╗
	██║  ██║██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝
	███████║█████╗   ╚████╔╝ █████╗  ███████╗
	╚════██║██╔══╝    ╚██╔╝  ██╔══╝  ╚════██║
		 ██║███████╗   ██║   ███████╗███████║
		 ╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝
											 
	                                         
				""","""
	  _______ __   __ _______ _______
	  |______   \_/   |______ |______
	 4|______    |    |______ ______|
									
	                                
				"""]
			color = [Fore.GREEN,Fore.YELLOW,Fore.WHITE,Fore.CYAN,Fore.RED]
			return choice(color) + choice(dizi)

	Eyes()
except AttributeError:
	try:
		print(Fore.RED+"ERR: AttributeError => Check Information")
	except NameError:
		print("ERR: AttributeError => Check Information")
except:
	print("\n")
	ex=0
	while (ex<=64):
		try:
			print(Fore.BLUE+"\r"+"#"*ex,end="")
			sleep(0.010)
			if ex == 64:
				print("\n")
			ex+=1
		except NameError:
			print("BYE")
			break


