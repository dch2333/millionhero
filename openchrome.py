#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import re
from lxml import etree

def read_file(file_name = '1.txt') :
    with open(file_name, 'r') as f :
        content = f.readlines()
        question = content[0]
        
    return question


question = read_file() 
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/s?cl=3&wd=' + question)
