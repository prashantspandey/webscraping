#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
from  more_itertools import unique_everseen
import pickle
from time import time


def get_data(my_links,textfilename,picklefilename):
    data_list = []
    textfilename = str(textfilename)
    
    picklefilename = str(picklefilename)
    
    for q, i in enumerate(my_links):
        try:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, 'lxml')
            print(str(q) + ' -- ' + i)
        except Exception as e:
            print(str(e))
        try:

            headline = soup.findAll('h1',{'class':'alpha tweet-title'})            
            divs = soup.findAll('div', {'class': 'article-entry text'})
            sdivs = soup.findAll('article', {'class': 'content_text row description'})
           
            if headline and divs:
                for head in headline:
                    print(str(q) + ' --- ' + str(i))
                    print('Headline: ' + head.text.strip())
                    for div in divs:
                        print('Article: ' + div.text.strip())
                        data_list.append(str('Headline:') + head.text.strip() +'\n'+ str('Article: ') + div.text.strip())
                    
                
                    

            if divs and not headline:
                for j in divs:
                    print(str(q) + ' --- ' + str(i))
                    print('Article: ' + j.text.strip())
                    data_list.append(j.text.strip())


            if sdivs:

                for k in sdivs:
                    print(str(q) + ' --- ' + str(i))
                    print('Article: ' + k.text.strip())
                    data_list.append(k.text.strip())
            #if tdivs:
                #for l in tdivs:
                    #print(str(q) + ' --- ' + str(i))
                    #print('Article: ' + l.text.strip())
                    #data_list.append(l.text.strip())

        except Exception as e:

            print(str(e))
        if q%1000 ==0:
            data_list = list(unique_everseen(data_list))
            picklefilename = str(q)+picklefilename+'pkl'
            textfilename = str(q)+textfilename+'txt'
            with open(picklefilename,'wb') as writetofile:
                pickle.dump(data_list,writetofile)
            with open(textfilename,'w',encoding='utf-8') as writetotext:
                for item in data_list:
                    writetotext.write(str(item)+'\n')
        else:
            pass
    

if __name__ == '__main__':
    time_start = time()
    print('Single process scraper begins here.........')
    with open('techcrunchLinks.pkl','rb') as linksfile:
        my_links = pickle.load(linksfile)
    print(str(len(my_links)) + ' links to scrape')
    get_data(my_links,'techcrunchData','techcrunchData')
    time_end =()
    total_time = time_end - time_start
    print('Total time take to scrape : ' + str(len(my_links)) + ' links ' + str(total_time))

