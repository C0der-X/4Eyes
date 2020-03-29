from lib import request
import re
from urllib.parse import urljoin
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
targetLinks=[]
def extractLinksFrom(url):
	response = request.request(url)
	return re.findall(r'(?:href=")(.*?)"', response.content.decode('utf-8', 'ignore'))
def spider(url):
	hrefLinks = extractLinksFrom(url)

	for link in hrefLinks:
		link = urljoin(url, link)

		if "#" in link:
			link = link.split("#")[0]
		if (url in link) and (link not in targetLinks):
			targetLinks.append(link)
			print(Fore.RED+"="*30)
			print(Fore.RED+"| ",Fore.GREEN+"[+] Found URL: "+link)
			print(Fore.RED+"="*30)
			try:
				spider(link)
			except KeyboardInterrupt:
				return targetLinks
				break

