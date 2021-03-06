#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
from  more_itertools import unique_everseen
import pickle
import re
from time import time

print('from here')
first_page_links = []
second_page_links = []
third_page_links = []
my_url = 'http://forum.santabanta.com/'
append_url = 'http://forum.santabanta.com'
time_start_gath = time()
r = requests.get(my_url)
soup = BeautifulSoup(r.content, "lxml")
ls = soup.findAll('a')

ph_div = soup.findAll('img')
fpl = []
spl =[]
tpl = []
all_linkss = []
main_links = []
photo_links = []
ph_links1 = []
ph_links2 = []
ph_links3 = []
ph_linksall =[]
for phot in ph_div:
    try:
        ph_link = phot['src']
        ph_links1.append(ph_link)
        print('Image Link: '+ ph_link)
    except Exception as e:
        print(str(e))
for i in ls:
    try:
        link = i['href']
        # for every img tag found put the src link in a list
        
        first_page_links.append(link)
    except:
        print('couldnot find href')

first_page_links = list(unique_everseen(first_page_links))
for i in first_page_links:
    if re.match(r'^show',i) or re.match(r'^forumdisplay',i):
        i = my_url + i
        print('Link on 1st page:SHOW OR FORUMDISPLAY '+ i)
        fpl.append(i)
    elif re.match(r'^/',i):
        i = append_url + i
        print('Link on 1st page: '+ i)
        fpl.append(i)
        
    else:
        fpl.append(i)
        print('Link on 1st page: '+ i)

for j in fpl:
    try:
        new_nage = requests.get(j)
        new_soup = BeautifulSoup(new_nage.content,'html.parser')
        sls = new_soup.findAll('a')
        # now get all the img tags
        photoreq2 = requests.get(j)
        photo_soup2 = BeautifulSoup(photoreq2.content,'lxml')
        ph_div2 = photo.soup2.findAll('img')
        try:
            for k in sls:
                slink = k['href']
                second_page_links.append(slink)
                
        except Exception as e:
            print(str(e))
        try:
            for pot in ph_div2:
                # find and add all the src links
                ph_link2 = pot['src']
                ph_links2.append(ph_link2)
                print('Image Link on second page : '+ ph_link2)
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
for q in second_page_links:
    if re.match(r'^show',q) or re.match(r'^forumdisplay',q):
        q = my_url + q
        print('Link on 2nd page: SHOW OR FORUMDISPLAY '+ q)
        spl.append(q)
    elif re.match(r'^/',q):
        q = append_url + q
        print('Link on 1st page: '+ q)
        spl.append(q)
    else:
        spl.append(q)
        print('Link on 2nd page: '+ q)

spl = list(unique_everseen(spl))

for k in spl:
    try:
        secon_page = requests.get(k)
        second_soup = BeautifulSoup(secon_page.content,'lxml')
        tls = second_soup.findAll('a')
        # now get all the img tags
        photoreq3 = requests.get(k)
        photo_soup3 = BeautifulSoup(photoreq3.content,'lxml')
        ph_div3 = photo.soup3.findAll('img')
        try:
            for l in tls:
                tlink = l['href']
                third_page_links.append(tlink)
        except Exception as e:
            print(str(e))
                
        try:
            for pot in ph_div3:
                # find and add all the src links
                ph_link3 = pot['src']
                ph_links3.append(ph_link3)
                print('Image Link on third page : '+ ph_link3)
        
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
for m in third_page_links:
    if re.match(r'^show',m) or re.match(r'^forumdisplay',m):
        m = my_url + m
        tpl.append(m)
        print('Link on 3rd page:SHOW OR FORUMDISPLAY '+ m)
    elif re.match(r'^/',m):
        m = append_url + m
        print('Link on 1st page: '+ m)
        tpl.append(m)
    else:
        tpl.append(m)
        print('Link on 3rd page: '+ m)

main_links = fpl + spl + tpl
ph_linksall = ph_links1 + ph_links2 + ph_links3
ph_linksall = list(unique_everseen(ph_linksall))
main_links = list(unique_everseen(main_links))
print('Total links found: '+ str(len(main_links)))

for ph in main_links:
    if ph.endswith(".jpg") or ph.endswith(".png") or ph.endswith(".jpeg"):
        photo_links.append(ph)
    else:
        pass
print('Photo links found: '+ str(len(photo_links)))
print('Image links found: ' + str(len(ph_linksall)))

with open('santabantalinks.pkl','wb') as ndtvlinks:
    pickle.dump(main_links,ndtvlinks)
with open('santabantalinks.txt', 'w',encoding="utf-8") as nd:
    for p in main_links:
        nd.write('{}\n'.format(p))
with open('santabantaphotolinks.pkl','wb') as ndtvphoto:
    pickle.dump(photo_links,ndtvphoto)
with open('santabantaimagelinks.pkl','wb') as p_l:
    pickle.dump(ph_linksall,p_l)

time_end_gath = time()
time_tak = (time_start_gath-time_end_gath)/60
print('Time take to gather links: '+str(time_tak))

'''




import threading

from multiprocessing.pool import ThreadPool
import multiprocessing
from multiprocessing import Pool
from queue import Queue

print('Scraping starts from here...')
time_start_scraper = time()
with open('ndtvlinksagain.pkl', 'rb') as links:
    my_links = pickle.load(links)

print('Number of links: ' + str(len(my_links)))
tot_links = len(my_links)
a = int(tot_links / 2)

print('first list - ' + str(a))


list1 = my_links[:a]
list2 = my_links[a:]

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

def get_data(my_links, q1):
    for q, i in enumerate(my_links):
        try:            
            #req = urllib.request.Request(i,headers = headers)
            #resp = urllib.request.urlopen(req)
            #respData = resp.read()
            respData = requests.get(i)
            soup = BeautifulSoup(respData.content, 'lxml')
            print(str(q) + ' -- ' + i)
        except Exception as e:
            print(str(e))
        try:
            headline = soup.findAll('h1',{'itemprop':'headline'})
            paras = soup.findAll('p')
            divs = soup.findAll('div', {'itemprop': 'articleBody'})
            sdivs = soup.findAll('article', {'class': 'content_text row description'})
            #tdivs = soup.findAll('article', {'class': 'Cont'})
            if headline and divs:
                for head in headline:
                    print(str(q) + ' --- ' + str(i))
                    print('Headline: ' + head.text.strip())                 

                    q1.put(head.text.strip())
                for div in divs:
                    print('Article: ' + div.text.strip())                 

                    q1.put(div.text.strip())
                    
                    
            if divs and not headline:
                for j in divs:
                    print(str(q) + ' --- ' + str(i))
                    print('Article: ' + j.text.strip())                  

                    q1.put(j.text.strip())
                  
            elif sdivs:

                for k in sdivs:
                    print(str(q) + ' --- ' + str(i))
                    print('Article: ' + k.text.strip())                   
                    q1.put(k.text.strip())
                   
            #if tdivs:
                #for l in tdivs:
                    #print(str(q) + ' --- ' + str(i))
                    #print('Article: ' + l.text.strip())                    
                    #q1.put(l.text.strip())
            
                    
            if paras and not divs and not headline:
               for t in paras:
		
                   print(str(q) + ' --- ' + str(i))
                   print('Paragraph: ' + t.text.strip())                    
                   q1.put(t.text.strip())                   

        except Exception as e:
            
            print(str(e))


zz = []



def yield_from_processp1(q, p1):
    while p1.is_alive():
        p1.join(timeout=1)
        while True:
            try:
                zz.append(q.get(block=False))
            except:
                break


def yield_from_processp2(q, p2):
    while p2.is_alive():
        p2.join(timeout=1)
        while True:
            try:
                zz.append(q.get(block=False))
            except:
                break





def write_to_text_file(filename, arr):
    filename = filename + '.txt'
    filename = str(filename)
    arr = list(unique_everseen(arr))
    with open(filename, 'w', encoding="utf-8") as nd:
        for p in arr:
            nd.write('{}\n'.format(p))
def write_to_pickle(filename,arr):
    filename = filename + '.pkl'
    filename = str(filename)
    arr = list(unique_everseen(arr))
    with open(filename,'wb') as file_pkl:
        pickle.dump(arr,file_pkl)
    


if __name__ == '__main__':
    
    q1 = multiprocessing.Queue()

    q2 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=get_data, args=(list1, q1,))
    p2 = multiprocessing.Process(target=get_data, args=(list2, q1,))
    
    p1.start()
    p2.start()
    
    yield_from_processp1(q1, p1)
    yield_from_processp2(q1, p2)
    
    write_to_text_file('ndtv25mayData', zz)
    write_to_pickle('ndtv25mayData',zz)
    print('Time taken by scraper: '+ str(time()-time_start_scraper))
    print('Total time program took: '+ str(time() - time_strat_gath))

'''

