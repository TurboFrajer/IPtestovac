import re, requests
from netaddr import *

url = requests.get("ENTER-URL")
url.encoding = "utf-8"

text = url.text
found = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|)',text)
info = url.text.splitlines()


najit = input("Zadat IP adresu: ")


for x in range(len(found)):
    if IPAddress(najit) in (IPNetwork(found[x])):        
        for y in range(len(info)):
            if found[x] in info[y]:
                print(info[y])




