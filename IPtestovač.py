import re, requests
from netaddr import *
from datetime import datetime


url = requests.get("ZADAT-IP-ADRESU")
url.encoding = "utf-8"

text = url.text
found = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|)',text)
info = url.text.splitlines()



najit = input("Zadat IP adresu: ").strip()



for x in range(len(found)):
    if IPAddress(najit) in (IPNetwork(found[x])):        
        for y in range(len(info)):
            if found[x] in info[y]:
                tim = info[y].split()
                print(f"Adresa {tim[0]} je blacklisted.")
                if tim[1] == "0":
                    print("Perma blacklisted.")
                    duvoda = " ".join(tim[2:])
                    print(f"Důvod: {duvoda}")

                elif tim[1].isnumeric() == True and tim[2].isnumeric() == True:
                    print(f"Blacklisted od: {datetime.fromtimestamp(int(tim[2]))}")
                    bando = int(tim[1])+int(tim[2])
                    print(f"Blacklisted do: {datetime.fromtimestamp(bando)}")
                    duvodb = " ".join(tim[3:])
                    print(f"Důvod: {duvodb}")

                else:
                    print(info[y])
                    break
   









