import requests, bs4
from itertools import groupby

def znach_inn():
    a =str(input('Введите название компании: '))  #'Связь-Банк'
    
    s=requests.get('https://www.google.com/search?q='+a+'инн')
    b=bs4.BeautifulSoup(s.text, 'lxml')
    zapros = b.getText()
    
    #'Подготовка'
    p1 = zapros.find('Результатов: примерно')
    p2 = zapros.rfind('Главная страница Google')
    zapros =zapros[p1:p2:]
    
    zifr = ['0','1','2','3','4','5','6','7','8','9']
    inn=[]
    
    #'Код'
    kolvoinn = zapros.count('ИНН')
    
    for i in range(0,kolvoinn):
        aa = zapros.find('ИНН')
        b = aa +14
        c = zapros[aa:b:]
        d = ''
        for j in range(0,len(c)):
            if c[j] in zifr :
                d =d +c[j]
        if len(d) == 10:        
            d = int(d)   
            inn.append(d)  
        b=b+1
        zapros = zapros[b::]
    
    
    inn.sort()
    inn1=inn
    inn2=[]
    
    inn1 = [el for el, _ in groupby(inn1)]    
    dlivainn1 = len(inn1)
    
    for i in range(0, dlivainn1):
        inn2.append(inn.count(inn1[i]))
        
    
    maxinn2 = 0 
    nomermaxinn2  = 0 
    for j in range(0, dlivainn1): 
        if inn2[j]>maxinn2 :
            maxinn2  = inn2[j]
            nomermaxinn2 = j
    
    maxinn1 = inn1[nomermaxinn2]
    
    inn = [el for el, _ in groupby(inn)]  
    
    print('Возможные значения ИНН', inn)  
    if len(inn1) != 1:
        print('Чаще всего встречается значение',maxinn1)
      
znach_inn()    
    #'длинна инн юр.лица = 10'