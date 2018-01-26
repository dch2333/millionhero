#!/usr/bin/python3
#coding=utf-8

import os
from PIL import Image
from aip import AipOcr


def get_screenshot() :
    os.system('adb shell screencap -p /sdcard/herodch.png')
    os.system('adb pull /sdcard/herodch.png')

def crop_img(img_name = 'herodch.png', crop_name = 'cropdch.png') :
    img = Image.open(img_name)
    cropimg = img.crop((45,300,1035,1420))
    cropimg.save(crop_name)
    img.close()
    cropimg.close()

def get_question(img_name = 'cropdch.png') :
    #
    APP_ID = '10709743'
    API_KEY ='HOCXbf3N3WjD6ZLatm3AG5op'
    SECRET_KEY = 'tZ78XzIlyb59XzAzRKsf3AMF5k2cCbq5'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #读取图片
    with open(img_name, 'rb') as fp:
        image = fp.read()
    #调用通用文字识别（含位置信息版），图片参数为本地图片
    client.general(image);
    #可选参数
    options = {}
    options['recognize_granularity'] = 'big'  #不返回单字信息
    #返回信息
    response=client.general(image, options)
    if response['words_result_num'] > 4 :
        question = response['words_result'][0]['words'][2:] + response['words_result'][1]['words']
        answerA = response['words_result'][-3]['words']
        answerB =	response['words_result'][-2]['words']
        answerC =	response['words_result'][-1]['words']
    else :
        question = response['words_result'][0]['words']
        answerA = response['words_result'][1]['words']
        answerB = response['words_result'][2]['words']
        answerC = response['words_result'][3]['words']
        
    return [question,answerA,answerB,answerC]
    
def write_to_file(question = []) :
    with open('1.txt','w') as f :
        for i in range(4) :
            f.writelines(question[i]+'\n')
        
def main():
    get_screenshot()
    crop_img()
    q = get_question()
    write_to_file(q)
    os.system('python3 openchrome.py')
    os.system('python3 helpanswer.py')
if __name__ == '__main__' :
    main()


