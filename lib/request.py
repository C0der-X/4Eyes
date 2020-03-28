import requests

def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		pass