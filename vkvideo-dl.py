import time
import json
import shutil
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument('--headless')

try:
    with open('vkvideo-dl.json','r') as rfile:
        conf=json.load(rfile)
except:
    print('Файл конфигурации не найден!')
    print('Edge установлен как браузер.')
    browser='Edge'
    conf={}
    conf['browser']=browser
else:
    browser=conf['browser']

while True:
    sel=0
    print('Выберите действие:')
    print('1) Скачать видео')
    print('2) Войти в аккаунт ВК')
    print('3) Изменить браузер')
    sel=str(input())
    if sel=='1':
        break
    elif sel=='2':
        print('Сейчас откроется окно браузера с главной ВК')
        print('Пожалуйста, войдите в аккаунт и нажмите Enter в консоли.')
        if browser=='Chrome':
            driver=webdriver.Chrome()
        else:
            driver=webdriver.Edge()
        driver.get('https://vk.com/')
        input()
        try:
            driver.close()
        except:
            ficha=1
        print('Ок')
    elif sel=='3':
        print('Выберите браузер (текущий - '+browser+')')
        print('1) Edge')
        print('2) Chrome')
        print('0) Отмена')
        ok=False
        while ok==False:
            selBr=str(input())
            if selBr=='1':
                browser='Edge'
                ok=True
                print('Браузер изменён на Edge')
            elif selBr=='2':
                browser='Chrome'
                ok=True
                print('Браузер изменён на Chrome')
            elif selBr=='0':
                ok=True
                print('Отмена')
            else:
                print('Ошибка. Попробуйте ещё раз')
    else:
        print('Выбрано несуществующее действие.')
    print(' ')
conf['browser']=browser
with open('vkvideo-dl.json','w') as wfile:
    json.dump(conf,wfile,indent=2)

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

if browser=='Chrome':
    driver=webdriver.Chrome(options=options)
else:
    driver=webdriver.Edge(options=options)
for vid in range(vidCount):
    print('Пожалуйста,подождите...')
    driver.get(urls[vid])
    time.sleep(10)
    print(' ')
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
    link=vidLinks[qual-1]
    link,vidID=link.split('id=')
    driver.get(vidLinks[qual-1])
    time.sleep(10)
    while completed==False:
        try:
            shutil.copyfile(('C:/Users/'+os.environ.get('USERNAME')+'/Downloads/'+vidID+'.mp4'), (os.getcwd()+'/'+filenames[vid]+'.mp4'))
            os.remove('C:/Users/'+os.environ.get('USERNAME')+'/Downloads/'+vidID+'.mp4')
            completed=True
        except:
            time.sleep(10)
    print('Видео №'+str(vid+1)+' сохранено.')
    print(' ')

try:
    driver.close()
except:
    ficha=1
print('Скачивание всех файлов завершено.')
print('Теперь вы можете закрыть программу.')
