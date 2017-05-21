#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
from  more_itertools import unique_everseen
import pickle
import threading
from multiprocessing.pool import ThreadPool
import multiprocessing
from multiprocessing import Pool
from queue import Queue
print('from here')

with open('wikireddit.pkl', 'rb') as links:
    my_links = pickle.load(links)

print('Number of links: ' + str(len(my_links)))
tot_links = len(my_links)
a = int(tot_links /4)
if not tot_links%4==0:
    b =a
    b = b+a
    c =a+b
    
    d = tot_links - (3*a)
    d = c+d
elif tot_links % 4 ==0:
    b =a
    b = b+a
    c =a+b
print('first list - ' + str(a))
print('second list - ' + str(b))
print('third list - ' + str(c))
print('fourth list - ' + str(d))
list1 = my_links[:a]
list2 = my_links[a:b]
list3 = my_links[b:c]
list4 = my_links[c:]
wl = []
wlt = []
cont1 = []
cont2 = []
wl2 = []
wlt2 = []

def get_data(my_links,q1):


    for q, i in enumerate(my_links):
        try:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, 'html.parser')
            print(str(q) + ' -- ' + i)
        except:
            print('Couldnot open the page')
        try:
            divs = soup.findAll('div', {'class': 'md'})
            sdivs = soup.findAll('div', {'id': 'article-content'})
            tdivs = soup.findAll('div', {'class': 'mw-content-ltr'})
            if divs:
                for j in divs:
                    print(str(q) + ' --- ' + str(i))
                    print('Article: ' + j.text.strip())
                    #cont.append(j.text.strip() + '\n\n||')

                    q1.put(j.text.strip() + '\n\n||')
                    # working_links.append(i)
                    # working_linkstxt.append(i)
            elif sdivs:

                for k in sdivs:
                    print(str(q) + ' --- ' + str(i))
                    print('Article: ' + k.text.strip())
                    #cont.append(k.text.strip() + '\n\n||')
                    q1.put(k.text.strip() + '\n\n||')
                    # q1.put(k.text.strip() + '\n\n||')
                    # working_links.append(i)
                    # working_linkstxt.append(i)
            elif tdivs:
                for l in tdivs:
                    print(str(q) + ' --- ' + str(i))
                    print('Article: ' + l.text.strip())
                    #cont.append(l.text.strip() + '\n\n||')
                    q1.put(l.text.strip() + '\n\n||')
                    # q1.put(l.text.strip() + '\n\n||')
                    # working_links.append(i)
                    # working_linkstxt.append(i)
        except:
            print('soup not available')


zz =[]


# p1 = multiprocessing.Process(target=get_data,args=(list1,wl,wlt,cont1,))
# p2 = multiprocessing.Process(target=get_data,args=(list2,wl2,wlt2,cont2,))

# async_result1 = pool.apply_async(get_data, (list1,wl,wlt,cont1,divs1,sdivs1,tdivs1))
# async_result2 = pool.apply_async(get_data, (list2,wl2,wlt2,cont2,divs2,sdivs2,tdivs2))
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
def yield_from_processp3(q, p3):
    while p3.is_alive():
        p3.join(timeout=1)
        while True:
            try:
                zz.append(q.get(block=False))
            except:
                break
def yield_from_processp4(q, p4):
    while p4.is_alive():
        p4.join(timeout=1)
        while True:
            try:
                zz.append(q.get(block=False))
            except:
                break

def write_to_text_file(filename,arr):
    filename = filename+'.txt'
    filename = str(filename)
    arr = list(unique_everseen(arr))
    with open(filename, 'w', encoding="utf-8") as nd:
        for p in arr:
            nd.write('{}\n'.format(p))



if __name__ == '__main__':
    # p = Pool()
    # l1 = p.map(get_data(list1, wl, wlt, cont1))
    q1 = multiprocessing.Queue()

    q2 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=get_data, args=(list1, q1,))
    p2 = multiprocessing.Process(target=get_data, args=(list2,q1,))
    p3 = multiprocessing.Process(target=get_data, args=(list3, q1,))
    p4 = multiprocessing.Process(target=get_data, args=(list4, q1,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    yield_from_processp1(q1,p1)
    yield_from_processp2(q1,p2)
    yield_from_processp3(q1,p3)
    yield_from_processp4(q1,p4)
    write_to_text_file('wikiandreddit',zz)






  
# with open('ndtvallpickle.pkl', 'wb') as ndtvpic:
#     pickle.dump(cont, ndtvpic)
# with open('ndtvworkinglinks.pkl', 'wb') as ndtvpi:
#     pickle.dump( cont, ndtvpi)
# with open('ndtvAllworkinglinks.txt', 'w', encoding="utf-8") as n:
#     for p in working_linkstxt:
#         n.write('{}\n'.format(p))
