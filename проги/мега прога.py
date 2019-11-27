import requests, bs4
from itertools import groupby

#функция поиска рейтинга брокерской фирмы по трем ресурсам
def get_rate():
    a=str(input('Введите название компании: '))
    print(' ')
    url = 'https://ratingfx.ru/forex/'
    rate1_dict= {} 
    for j in range(1,20):
        par= {'page':j}
        s1=requests.get(url, params=par)
        b1=bs4.BeautifulSoup(s1.text, 'html.parser')
        if j==19:
            k=2
        else:
            k=15
        for i in range(k):
            rate1_title=b1.findAll('div',{'class':'br3'})[i].getText()
            rate1_rating=b1.findAll('div', {'class':'rait-n'})[i].getText()
            rate1_dict[rate1_title]=rate1_rating
            i+=1
        j+=1
    if rate1_dict.get(a) == None:
        print('Такого в списке ratingfx нет')
    else: print('Рейтинг по ratingfx компании '+a+' - '+ rate1_dict[a])
# =============================================================================
    s2=requests.get('http://forex-ratings.ru/forex-brokers/')
    rate2_dict= {} 
    b2=bs4.BeautifulSoup(s2.text, 'lxml')
    rates2= b2.find('table', {'class':'table table-responsive'}).findAll('tr')
    for rate2 in rates2[1:]:
        rate2_title=rate2.find('a',{'class':'blink h2'}).text
        rate2_desc= rate2.find('span', {'class':'text-muted'}).text
        rate2_dict[rate2_title]=rate2_desc
    if rate2_dict.get(a) == None:
        print('Такого в списке forex-ratings нет')
    else: print('Описание по forex-ratings компании '+a+' - '+ rate2_dict[a])
# =============================================================================
    s=requests.get('http://www.brokers-rating.ru/archive/')
    b=bs4.BeautifulSoup(s.text, 'lxml')
    rates11 = b.getText()
    nomer=rates11.find('№')
    rates11 = rates11[nomer::]
    zvezda = rates11.rfind('*')
    rates11 = rates11[:zvezda:]
    nachalonew=rates11.find('New')
    koneznew=nachalonew+3
    rates11 = rates11[:nachalonew:]+rates11[koneznew::]
    nachalonazvania = rates11.find(a)
    dlinanazvania = len(a)
    koneznazvania = nachalonazvania+dlinanazvania     
    if  nachalonazvania == - 1:
         print('Информации о компании '+ a+ ' в списке brokers-rating нет')
    else:   
         nachalogoda = koneznazvania+1
         if rates11[nachalogoda]  == '1' or rates11[nachalogoda] == '2' :
            konezgoda = nachalogoda + 3
         else :
             konezgoda = koneznazvania
    
         status= rates11.find('Закрыт',koneznazvania,koneznazvania+13 )
        
         if status != -1:
            print ('Компания '+ a+' закрыта')
        
         else: 
        
            nachaloreitinga = konezgoda + 3
            
            if ord(rates11[nachaloreitinga] )== 10 :
                print ('Рейтинг компании '+ a+' по списку brokers-rating неизвестен')
            else: 
                konezreitinga = nachaloreitinga + 1 
                for i in range(2,5):
                    if rates11[nachaloreitinga+i] ==' ' :
                        break
                    else: 
                        konezreitinga = konezreitinga + 1 
                rezultat = rates11[nachaloreitinga:konezreitinga:]
                
                print('Рейтинг компании '+a+' по списку brokers-rating - '+ rezultat)
# =============================================================================
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
    
    print('Возможные значения ИНН компании '+a+': ', inn)  
    if len(inn1) != 1:
        print('Чаще всего встречается значение',maxinn1)
# =============================================================================
    url = 'https://www.cbr.ru/finmarket/nfo/cat_ufr/?Query=' + str(inn)+'&QueryField=inn'
    s=requests.get(url)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    
    p=b.find_all(class_="data")
    
    if len(p) != 0 :
        print('Компания '+a+' состоит в реестре Банка России')
    else:
        print('Данных нет')
#использование функции
get_rate() #'Открытие Брокер'
