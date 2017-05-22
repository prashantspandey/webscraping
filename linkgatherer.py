from bs4 import BeautifulSoup
import requests
from  more_itertools import unique_everseen
import pickle
import re

print('from here')
first_page_links = []
second_page_links = []
third_page_links = []
my_url = 'http://www.ndtv.com/'
append_url = 'http://www.ndtv.com/'
r = requests.get(my_url)
soup = BeautifulSoup(r.content, "html.parser")
ls = soup.findAll('a')
fpl = []
spl =[]
tpl = []
all_linkss = []
main_links = []
for i in ls:
    try:
        link = i['href']
        first_page_links.append(link)
    except:
        print('couldnot find href')

first_page_links = list(unique_everseen(first_page_links))
for i in first_page_links:
    if re.match(r'^/',i):
        i = append_url + i
        fpl.append(i)
    else:
        fpl.append(i)

for j in fpl:
    try:
        new_nage = requests.get(j)
        new_soup = BeautifulSoup(new_nage.content,'html.parser')
        sls = new_soup.findAll('a')
        try:
            for k in sls:
                slink = k['href']
                second_page_links.append(slink)
        except:
            print('couldnot find links on second page')
    except:
        print('couldnot go to second page')
for q in second_page_links:
    if re.match(r'^/',q):
        q = append_url + q
        spl.append(q)
    else:
        spl.append(q)

spl = list(unique_everseen(spl))

for k in spl:
    try:
        secon_page = requests.get(k)
        second_soup = BeautifulSoup(secon_page.content,'lxml')
        tls = second_soup.findAll('a')
        try:
            for l in tls:
                tlink = l['href']
                third_page_links.append(tlink)
        except:
            print('couldnot find links on third page')
    except:
        print('couldnot go to third page')
for m in third_page_links:
    if re.match(r'^/',m):
        m = append_url + m
        tpl.append(m)
    else:
        tpl.append(m)

main_links = fpl + spl + tpl
main_links = list(unique_everseen(main_links))


with open('ndtvlinksagain.pkl','wb') as ndtvlinks:
    pickle.dump(main_links,ndtvlinks)
with open('ndtvlinksagain.txt', 'w',encoding="utf-8") as nd:
    for p in main_links:
        nd.write('{}\n'.format(p))