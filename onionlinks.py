#!/usr/bin/python3
import socket
import socks
import http.client
from urllib import request
import stem.process

SOCKS_PORT = 9050
from more_itertools import unique_everseen
from bs4 import BeautifulSoup
import requests
import pickle
import re

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
socket.socket = socks.socksocket


# Perform DNS resolution through the socket

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]


url = 'http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page'
socket.getaddrinfo = getaddrinfo
headers = {}
headers[
    'User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
req = request.Request(url, headers=headers)
resp = request.urlopen(req).read()

print('from here')
first_page_links = []
second_page_links = []
third_page_links = []
my_url = 'http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page'
append_url = 'http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page'
# r = requests.get(url)

soup = BeautifulSoup(resp, "lxml")

ls = soup.findAll('a')
fpl = []
spl = []
tpl = []
all_linkss = []
main_links = []
for i in ls:
    try:
        link = i['href']
        first_page_links.append(link)
    except Exception as e:
        print(str(e))

first_page_links = list(unique_everseen(first_page_links))
for i in first_page_links:
    if re.match(r'^/', i):
        i = append_url + i
        fpl.append(i)
    else:
        print('Link on first page:' + i)
        fpl.append(i)

for j in fpl:
    try:

        new_nage = request.Request(j, headers=headers)
        new_nage = request.urlopen(new_nage).read()
        new_soup = BeautifulSoup(new_nage, 'lxml')
        sls = new_soup.findAll('a')
        try:
            for k in sls:
                slink = k['href']
                second_page_links.append(slink)
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
for q in second_page_links:
    if re.match(r'^/', q):
        q = append_url + q
        spl.append(q)
    else:
        print('Link on 2nd page:' + q)
        spl.append(q)

spl = list(unique_everseen(spl))

for k in spl:
    try:

        secon_page = request.Request(k, headers=headers)
        secon_page = request.urlopen(secon_page).read()
        second_soup = BeautifulSoup(secon_page, 'lxml')
        tls = second_soup.findAll('a')
        try:
            for l in tls:
                tlink = l['href']
                third_page_links.append(tlink)
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
for m in third_page_links:
    if re.match(r'^/', m):
        m = append_url + m
        tpl.append(m)
    else:
        print('Link on 3rd page:' + m)
        tpl.append(m)

main_links = fpl + spl + tpl
main_links = list(unique_everseen(main_links))

with open('hiddenwikilinks.pkl', 'wb') as ndtvlinks:
    pickle.dump(main_links, ndtvlinks)
with open('hiddenwikilinks.txt', 'w', encoding="utf-8") as nd:
    for p in main_links:
        nd.write('{}\n'.format(p))
