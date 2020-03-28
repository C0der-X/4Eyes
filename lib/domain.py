import colorama
from colorama import Fore, Back, Style
from lib import request
import os

class Domain:
	def __init__(self,url,output):

		self.url = url
		self.output = output

		self.finder()

	def finder(self):
		urls = []
		colorama.init(autoreset=True)
		try:
			with open(f"{os.getcwd()}/text/common.txt", "r") as file:
				print("\n")
				for i in file:
					adress = self.url.split("//")[0] + "//" + self.url.split("//")[1] + "/" +  i.strip()
					response = request.request(adress)
					if response:
						urls.append(adress)
						print("\n"+Fore.BLUE+"="*30)
						print(Fore.BLUE+"| "+Fore.GREEN+"[+] Discovered URL: "+Fore.CYAN+adress)
						print(Fore.BLUE+"="*30)
					print(Fore.RED+"\r[-] Tried: "+Fore.YELLOW+adress+"                               ",end="")
			return self.writer(urls)
		except FileNotFoundError:
			print("'4Eyes' klasöründe değilsiniz. Lütfen belirtilen klasöre girip programı tekrar çalıştırınız")
		except KeyboardInterrupt:
			return self.writer(urls)
	def writer(self,urls):
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
