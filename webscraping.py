from bs4 import BeautifulSoup
import requests
from traceback import print_exc

print('from here')
my_url = 'http://www.news18.com/india/'
r = requests.get(my_url)
soup = BeautifulSoup(r.content, "lxml")
# print(soup.prettify())
te = soup.findAll("p")
topnews = soup.findAll("h1", {"class": "hd1"})
'''
for j in range(1,7):
    
    try:        
        head = soup.findAll(eval('"h"+str(j)'))
        #print(eval("soup.h"+str(j)))
        for k in head:
          
            print(k.text)
    except:
          print('not found')


alinks = soup.findAll("a")
for i in alinks:
    try:
        li = i['href']
        newr = requests.get(li)
        sou = BeautifulSoup(newr.content, 'lxml')
        print('link '+ li)
        for j in range(1,7):
        
            try:        
                he = soup.findAll(eval('"h"+str(j)'))
                #print(eval("soup.h"+str(j)))
                for k in he:
                      
                    print(k.text.strip())
            except:
                  print('not found')
    except:
        print('url not found')
        '''

hline = set()
di = soup.findAll('div')
with open('news18.txt', 'w') as th:
    for i in di[20:55]:

        try:
            k = i.findAll("a")
            try:
                for uuu, p in enumerate(k):
                    print(str(uuu) + ' a  of ' + str(len(k)))
                    divlink = p['href']
                    new_page = requests.get(divlink)
                    new_soup = BeautifulSoup(new_page.content, 'lxml')
                    for q in range(1, 7):
                        try:
                            yy = new_soup.findAll(eval('"h"+str(q)'))
                            for w in yy:

                                if len(w.text.strip()) > 25:
                                    print(w.text.strip())
                                    th.write("{}\n".format(w.text.strip()))
                                    try:
                                        new_para = new_soup.findAll('p')
                                        for ppp, pp in enumerate(new_para):
                                            if len(pp.text.strip()) > 30:
                                                print('Paragraph  ' + str(ppp) + ' '  + pp.text.strip())
                                                th.write("{}\n".format(pp.text.strip()))
                                    except:
                                        print('no paragraphs on new page')

                        except:
                            print('heading not found')
            except:
                print('href not found')
        except:
            print('a not found')
'''      
with open('bhaskerhead.txt', 'w') as file_handler:
    for item in hline:
        file_handler.write("{}\n".format(item))
'''
