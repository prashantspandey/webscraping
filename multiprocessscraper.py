from bs4 import BeautifulSoup
import requests
from  more_itertools import unique_everseen
import pickle
import threading
from multiprocessing.pool import ThreadPool
import multiprocessing
from multiprocessing import Pool

print('from here')

with open('mensxplinks.pkl', 'rb') as links:
    my_links = pickle.load(links)

print('Number of links: ' + str(len(my_links)))
list1 = my_links[:25]
list2 = my_links[50:75]
wl = []
wlt = []
cont1 = []
cont2 = []
wl2 = []
wlt2 = []


def get_data(my_links, working_links, working_linkstxt, cont,q1):
    for q, i in enumerate(my_links):
        try:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, 'html.parser')
            print(str(q) + ' -- ' + i)
        except:
            print('Couldnot open the page')
        try:
            divs = soup.findAll('div', {'class': 'cont blk'})
            sdivs = soup.findAll('span', {'itemprop': 'articleBody'})
            tdivs = soup.findAll('div', {'itemprop': 'description'})
            if divs:
                for j in divs:
                    print('Article: ' + j.text.strip())
                    cont.append(j.text.strip() + '\n\n||')
                    q1.put(j.text.strip() + '\n\n||')
                    # working_links.append(i)
                    # working_linkstxt.append(i)
            elif sdivs:

                for k in sdivs:
                    print('Article: ' + k.text.strip())
                    cont.append(k.text.strip() + '\n\n||')
                    # q1.put(k.text.strip() + '\n\n||')
                    # working_links.append(i)
                    # working_linkstxt.append(i)
            elif tdivs:
                for l in tdivs:
                    print('Article: ' + l.text.strip())
                    cont.append(l.text.strip() + '\n\n||')
                    # q1.put(l.text.strip() + '\n\n||')
                    # working_links.append(i)
                    # working_linkstxt.append(i)
        except:
            print('soup not available')
        # cont = list(unique_everseen(cont))




# p1 = multiprocessing.Process(target=get_data,args=(list1,wl,wlt,cont1,))
# p2 = multiprocessing.Process(target=get_data,args=(list2,wl2,wlt2,cont2,))

# async_result1 = pool.apply_async(get_data, (list1,wl,wlt,cont1,divs1,sdivs1,tdivs1))
# async_result2 = pool.apply_async(get_data, (list2,wl2,wlt2,cont2,divs2,sdivs2,tdivs2))



if __name__ == '__main__':
    # p = Pool()
    # l1, l2 = p.map(get_data(my_links, wl, wlt, cont1))
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=get_data, args=(list1, wl, wlt, cont1,q1,))
    p2 = multiprocessing.Process(target=get_data, args=(list2, wl2, wlt2, cont2,q2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('i am here')
    while q1.empty() is False:
        print(q1.get())

    # with open('mensxp.txt', 'w', encoding="utf-8") as nd:
    #     for p in zz:
    #         nd.write('{}\n'.format(p))
# with open('ndtvallpickle.pkl', 'wb') as ndtvpic:
#     pickle.dump(cont, ndtvpic)
# with open('ndtvworkinglinks.pkl', 'wb') as ndtvpi:
#     pickle.dump( cont, ndtvpi)
# with open('ndtvAllworkinglinks.txt', 'w', encoding="utf-8") as n:
#     for p in working_linkstxt:
#         n.write('{}\n'.format(p))
