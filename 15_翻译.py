import urllib
import codecs
from bs4 import BeautifulSoup
from sys import argv
import re,time

class Translate:
    def Start(self):
        self._get_html_sourse()
        self._get_content("enc")
        self._remove_tag()
        self.print_result()

    def _get_html_sourse(self):
        word=argv[1] if len(argv)>1 else ''
        url="https://dict.youdao.com/ugc/wordjson/" %  word
        self.htmlsourse=unicode(urllib.urlopen(url).read(),"gb2312","ignore").encode("utf-8","ignore")

    def _get_content(self,div_id):
        soup=BeautifulSoup("".join(self.htmlsourse))
        self.data=str(soup.find("div",{"id":div_id}))

    def _remove_tag(self):
        soup=BeautifulSoup(self.data)
        self.outtext=''.join([element  for element in soup.recursiveChildGenerator()
                              if isinstance(element,unicode)])

    def print_result(self):
        for item in range(1,10):
            self.outtext=self.outtext.replace(str(item),"\n%s" % str(item))
        self.outtext=self.outtext.replace("  ","\n")
        print (self.outtext)

if __name__=="__main__":
    Translate().Start()

# from Wucx
# # !/usr/local/Cellar/python/3.7.2/bin/python3
# from urllib import request
# from bs4 import BeautifulSoup
# #
# keyword = input()
# url = 'http://www.youdao.com/w/'+keyword+'/#keyfrom=dict2.top'
# html = request.urlopen(url).read().decode('utf-8')
# soup0 = BeautifulSoup(html,'html.parser')
# pointed_div1 = soup0.findAll(name='',attrs={"class":"trans-container"})[0].findAll('li')
# # pointed_div2 = pointed_div1[0].findAll('li')
# # print (pointed_div)
# print (pointed_div1)
# # print (soup0)