import requests, bs4
def inn():    
    inn=''
    inn = input('Введите ИНН: ')
    url = 'https://www.cbr.ru/finmarket/nfo/cat_ufr/?Query=' + inn+'&QueryField=inn'
    s=requests.get(url)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    
    p=b.find_all(class_="data")
    
    if len(p) != 0 :
        print('Компания состоит в реестре Банка России')
    else:
        print('Данных нет')

inn()
#7710301140

