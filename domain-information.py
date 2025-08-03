import requests
import rich
domain = "testphp.vulnweb.com"
respanse = requests.get(f"http://api.whois.vu/?q={domain}")
if respanse.status_code == 200 : 
    json = respanse.text
    print(json)