import requests, bs4, re

def dohodnost():
    
    s=requests.get(str(input('Введите url - адрес: ')))
    b=bs4.BeautifulSoup(s.text, "html.parser")
    kod=b.getText()
    
    znachenia = []
    
    b1=kod.count('доходностью')
    for i in range (1, b1+1):
#        'Получим строчку с доходностью'
        b11= kod.find('доходностью')
        b111=b11+20
        b1111= kod[b11:b111:]
     
#        'Найдем место первой цифры процента'
        p = 0
        for i in range (1,10):
            a = str(i)
            p1=b1111.find(a)
            if p1==-1:
                p=0
            else: 
                p=p1
                break
#        'Найдем место символа процента'
        pp = b1111.find('%')
        
#        'Обрежем строчку'
        b11111 = b1111[p:pp:]
        b11111=int(b11111)
        znachenia.append(b11111)
#        "Уберем обработанную информацию"
        kod = kod[b111::]
        
    print('Значения доходности равны: ',znachenia)

dohodnost()
#'https://vkoshelek.com/fexbet/'
#?????????'Ключевые слова : годовых '