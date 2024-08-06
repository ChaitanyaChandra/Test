import requests

def check_url(url):
	try:
		response = requests.head(url)
		if response.status_code == 200:
			return f"{url} working fine"
	except requests.ConnectionError as e:
		return f"{url} not working!"
# 		return f"{url} not working  {e}"


web_sites = ["https://www.chaitu.net/", "https://difjkdjfkfjkdfj.net" , "https://www.google.com"]

for item in web_sites:
    print(check_url(item))