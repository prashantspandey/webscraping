from bs4 import BeautifulSoup 
import requests
from  more_itertools import unique_everseen
print('from here')
my_url = 'http://www.ndtv.com/'
r = requests.get(my_url)
soup = BeautifulSoup(r.content, "html5lib")
#print(soup.prettify())
#te = soup.findAll("p")
#topnews = soup.findAll("h1",{"class":"hd1"})
'''
for j in range(1,6):
    
    try:        
        head = soup.findAll(eval('"h"+str(j)'))
        for k in head:
            print(k.content)
            print(k.text)
    except:
          print('not found')

'''
links = []
ins_divs = []
divs = soup.findAll('div')
for i in divs[40:60]:
    try:
        aas = i.findAll('a')
        aas = list(unique_everseen(aas))
        for j in aas:
            try:
                hreff = j['href']
                links.append(hreff)
                
            except:
                print('link not found')
    except:
        print('url not found')
        
try:
    links_hreff = list(unique_everseen(links))
    print(links_hreff)
except:
    print('problem with unique href list')
for m,k in enumerate(links_hreff):
    try:
        new_page = requests.get(k)
        new_soup = BeautifulSoup(new_page.content,'html5lib')
        print('THESE PARAGRAPHS WERE FOUND AT'+ str(k))
        new_para = new_soup.findAll('p')
                
        #new_para = list(unique_everseen(new_para))
        for n,l in enumerate(new_para):
            if len(l.text.strip())>15 and n <= int(len(new_para)-2):
                print('paragraph: '+str(n) +': '+ l.text.strip())
            if n== int(len(new_para)-1):
                print('last paragraph :' + l.text.strip() + '----------------------------------')
    except:
        print('paragraph not found')
            
    try:
        print('THESE PARAGRAPHS WERE FOUND AT'+ str(k))
        new_div = new_soup.findAll('div',{'class':'ins_storybody'})
        for o in new_div:
            print( o.text.strip())
            ins_divs.append(str(k) + '\n' +o.text.strip())
    except:
        print('cannot find div')
important_div = list(unique_everseen(ins_divs))
with open('ndtv.txt','w') as nd:
    for p in important_div:
        nd.write('{}\n'.format(p))
