import wget
import time
import json
import shutil
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument('--headless')

print('Сколько видео надо скачать?')
vidCount=input()
while True:
    try:
        vidCount=int(vidCount)
        break
    except:
        print('Введите корректное значение!')

filenames=[]
urls=[]
vidLinks=[]
useOneQ=''
statQ=999
mesSh=False

for n in range(vidCount):
    url=input('Введите ссылку на видео №'+str(n+1)+': ')
    urls.append(url)
    filename=input('Введите название видео №'+str(n+1)+': ')
    filenames.append(filename)

driver=webdriver.Edge(options=options)
for vid in range(vidCount):
    print('Пожалуйста,подождите...')
    driver.get(urls[vid])
    time.sleep(10)
    getQL=driver.execute_script('return(window.cur?.videoInlinePlayer.vars)')
    if getQL=='undefined':
        getQL=driver.execute_script('return(window.mvcur?.player?.vars)')
    if statQ==999:
        print('Выберите качество:')
        try:
            vidLinks.append(getQL['url144'])
            print('1)144')
            vidLinks.append(getQL['url240'])
            print('2)280')
            vidLinks.append(getQL['url360'])
            print('3)360')
            vidLinks.append(getQL['url480'])
            print('4)480')
            vidLinks.append(getQL['url720'])
            print('5)720')
            vidLinks.append(getQL['url1080'])
            print('6)1080')
            vidLinks.append(getQL['url1440'])
            print('7)1440')
            vidLinks.append(getQL['url2160'])
            print('8)2160')
        except:
            corrQ=False
        corrQ=False
        while corrQ==False:
            try:
                qual=int(input())
                corrQ=True
            except:
                print('Использовано неверное значение.')
    while mesSh==False:
        useOneQ=input('Использовать это качество для всех видео? д/н: ')
        if useOneQ=='д' or useOneQ=='Д' or useOneQ=='d' or useOneQ=='D':
            statQ=qual
            mesSh=True
        elif useOneQ=='н' or useOneQ=='Н' or useOneQ=='n' or useOneQ=='N':
            mesSh=True
        else:
            print('Введите корректное значение!')
    completed=False
    if statQ!=999:
        qual=statQ
    else:
        qual=qual-1
    print('Пожалуйста,подождите...')
    link=vidLinks[qual]
    link,vidID=link.split('id=')
    driver.get(vidLinks[qual])
    time.sleep(10)
    while completed==False:
        try:
            shutil.copyfile(('C:/Users/'+os.environ.get('USERNAME')+'/Downloads/'+vidID+'.mp4'), (os.getcwd()+'/'+filenames[vid]+'.mp4'))
            os.remove('C:/Users/'+os.environ.get('USERNAME')+'/Downloads/'+vidID+'.mp4')
            completed=True
        except:
            ficha=''
            time.sleep(15)
    print('Видео №'+str(vid+1)+' сохранено.')

try:
    driver.close()
except:
    print()
print('Скачивание всех файлов завершено.')
input('Нажмите Enter для закрытия программы.')
