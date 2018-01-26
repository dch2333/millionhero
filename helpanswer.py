#!/usr/bin/python3
#coding=utf-8

from lxml import etree
from threading import Thread
import re,requests

class HeroThread(Thread) :
    def __init__(self, content1, content2) :
        super().__init__()
        self.content1 = content1
        self.content2 = content2
        
    def run(self) :
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
                }
        res = requests.get(url = 'https://www.baidu.com/s?cl=3&wd=' + self.content1 + ' ' + self.content2,
                       headers = headers)
        html = res.text
        e_html = etree.HTML(html)
        text = e_html.xpath('//*[@id="container"]/div[2]/div/div[2]/text()')[0]
        self.result = int(re.sub(r'\D','',text))
        
    def get_result(self) :
        return self.result
        

def read_file(file_name = '1.txt') :
    with open(file_name, 'r') as f :
        content = f.readlines()
        question = content[0]
        answerA = content[1]
        answerB = content[2]
        answerC = content[3]
        
    return [question,answerA,answerB,answerC]
'''
def degree_of_association(content = []) :
    headers = {"User-Agent": 
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
    }
    question,answerA,answerB,answerC = content[0],content[1],content[2],content[3]
    #A
    res = requests.get(url = 'https://www.baidu.com/s?cl=3&wd=' + question + ' ' + answerA,
                       headers = headers)
    html = res.text
    A_html = etree.HTML(html)
    a_text = A_html.xpath('//*[@id="container"]/div[2]/div/div[2]/text()')[0]
    a = int(re.sub(r'\D','',a_text))
    #B
    res = requests.get(url = 'https://www.baidu.com/s?cl=3&wd=' + question + ' ' + answerB,
                       headers = headers)
    html = res.text
    B_html = etree.HTML(html)
    b_text = B_html.xpath('//*[@id="container"]/div[2]/div/div[2]/text()')[0]
    b = int(re.sub(r'\D','',b_text))
    #C
    res = requests.get(url = 'https://www.baidu.com/s?cl=3&wd=' + question + ' ' + answerC,
                       headers = headers)
    html = res.text
    C_html = etree.HTML(html)
    c_text = C_html.xpath('//*[@id="container"]/div[2]/div/div[2]/text()')[0]
    c = int(re.sub(r'\D','',c_text))
    
    return [100*a/(a+b+c),100*b/(a+b+c),100*c/(a+b+c)]
'''
#相关度
def degree_of_association(content = []) :
    question,answerA,answerB,answerC = content[0],content[1],content[2],content[3]
    threads = [HeroThread(question, answerA) ,
               HeroThread(question, answerB) ,
               HeroThread(question, answerC)]
    for thread in threads :
        thread.start()
    for thread in threads :
        thread.join()
    a = threads[0].get_result()
    b = threads[1].get_result()
    c = threads[2].get_result()
    
    return [100*a/(a+b+c), 100*b/(a+b+c), 100*c/(a+b+c)]


def main() :
    t = read_file()
    print(degree_of_association(t))
if __name__ == '__main__' :
    main()





