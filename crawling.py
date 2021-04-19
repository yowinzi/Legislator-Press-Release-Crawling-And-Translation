# -*- coding: utf-8 -*
import sys
import requests
from bs4 import BeautifulSoup
import time
import re
import numpy as np

class PttCrawler:
    
    def __init__(self):

        self.prefix = 'https://www.ly.gov.tw'

        self.homepage = 'https://www.ly.gov.tw/Pages/List.aspx?nodeid=110'

        self.sessions = {}

        self.legislators = {}

    def getWebPage(self,url):
        
        response = requests.get(url=url)
        if response.status_code != 200: 
            print('Invalid url:', response.url)
            return None
        else:
            response.encoding = "utf-8"
            return response.text

    def getSessionLinks(self):

        page = self.getWebPage(self.homepage)
        soup = BeautifulSoup(page, 'html.parser')

        a_tags = soup.find_all('a')
        
        for tag in a_tags:
            if tag.string:
                if tag.string[0] == '第':
                    self.sessions[tag.string] = self.prefix + tag['href']

        print ('Got all sessions...')

        print (self.sessions)
                    

    def getLegislators(self):

        for key in self.sessions.keys():

            print (key,'...')

            page = self.getWebPage(self.sessions[key])
            soup = BeautifulSoup(page, 'html.parser')
            

            tags = soup.find_all('a' , {'data-toggle':"tooltip"})

            
            for tag in tags:

                name = tag.find('div',class_='legislatorname')

                if name:
    
                    if name.string not in self.legislators:
                        self.legislators[key+name.string] = self.prefix+ tag['href']

        print ('Got all legislators links...')


        

    def getNewsLink(self,url):

        print (url)

        page = self.getWebPage(url)
        soup = BeautifulSoup(page, 'html.parser')
        tags = soup.find_all('a')

        url = None
        
        for tag in tags :
            if tag.text == '新聞稿':
                url = self.prefix+tag['href']

        print (url)

        if not url:
            return None
        '''
        page = self.getWebPage(url)
        soup = BeautifulSoup(page, 'html.parser')
        tag = soup.find('a',class_="btn six-articleBtn")
        url = self.prefix+tag['href']
        '''
        
        return url
    

    def getAllArticleLinks(self,url):


        links = []

        if None:
            return links

        keyword = url.split('?')[-1]+'&'

        page = self.getWebPage(url)

        page = self.getWebPage(url)
        soup = BeautifulSoup(page, 'html.parser')
        tags = soup.find_all('a')

        
        for tag in tags:
            try:
                if keyword in tag['href']:
                    url = self.prefix+tag['href']
                    links.append(url)           
            except:
                pass

        return links

    
    def getArticle(self,url):

        page = self.getWebPage(url)
        soup = BeautifulSoup(page, 'html.parser')
        ts = soup.find('div',class_="col-md-12")
        text = ""
        title = ts.find('b').text
        ts = ts.find_all('p')

        for i,t in enumerate(ts):
            text +=t.text
        
        return title,text

    def processing(self):

        self.getSessionLinks()
        self.getLegislators()

        i = 1

        for key in self.legislators.keys():

            print ("legislator ",key,' downloading...')

            legislators_url = self.legislators[key]

            url = self.getNewsLink(legislators_url)

            
            if url:
        
                urls = self.getAllArticleLinks(url)

                for u in urls:
                    try:
                        title,text = self.getArticle(u)
                        fp = open('Chinese/'+str(i)+".txt", "w", encoding="utf-8")
                        fp.write(text)
                        i+=1
                        fp.close()
                    except:
                        pass
        
                

    '''
            
    def func(self):

        url = 'https://lis.ly.gov.tw/lylegismc/lylegismemkmout?000869720011000100000000000019000000003C000000000^'

        page_ = [ str(i) for i in range(9,0,-1)]

        for p in page_:
    
            person_url = url+p
            
            page = self.getWebPage(person_url)
            soup = BeautifulSoup(page, 'html.parser')
            tags = soup.find_all('a')

            t = 0
            
            for tag in tags:
                if tag.text == '謝生富':
                    t = 'https://lis.ly.gov.tw' + tag['href']

    def func2(self):

        url = 'https://lis.ly.gov.tw/lylegisc/lylegiskmout?.f0a1008030200000A000E00000^00001000000000000050008A6003fb9'

        
        page = self.getWebPage(url)
        soup = BeautifulSoup(page, 'html.parser')
        tags = soup.find_all('a')

        
        for tag in tags:
            try :
                x = tag.find('img',alt="問政成果")
                if x:
                    t = 'https://lis.ly.gov.tw'+tag['href']
                    print (t)
            except:
                pass

        return t

    '''
        

def main():

    pttcrawler = PttCrawler()

    pttcrawler.processing()
    


if __name__ == '__main__':


    main()


