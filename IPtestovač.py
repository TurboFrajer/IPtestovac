import requests
from netaddr import *
from datetime import datetime


url4 = requests.get("IPv4 seznam")
url6 = requests.get("IPv6 seznam")
url4.encoding = "utf-8"
url6.encoding = "utf-8"

text = url4.text + url6.text
info = text.splitlines()
found = [z.split()[0] for z in info]
najit = input("Zadat IP adresu: ").strip()





for x in range(len(found)):
    try:
        IPNetwork(najit) == True

    except:
        print("Není IP adresa nebo rozsah.")
        break
    
    if IPNetwork(najit) in IPNetwork(found[x]):        
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
        break
else:
    print("Není blacklisted.")









