#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:41:30 2019

@author: macintosh
"""


import bs4
# =============================================================================
# 
# =============================================================================
import requests, bs4
s=requests.get('https://sinoptik.com.ru/погода-москва')
b=bs4.BeautifulSoup(s.text, "html.parser")
p3=b.select('.temperature .p3')
pogoda1=p3[0].getText()
p4=b.select('.temperature .p4')
pogoda2=p4[0].getText()
p5=b.select('.temperature .p5')
pogoda3=p5[0].getText()
p6=b.select('.temperature .p6')
pogoda4=p6[0].getText()
print('Утром :' + pogoda1 + ' ' + pogoda2)
print('Днём :' + pogoda3 + ' ' + pogoda4)
p=b.select('.rSide .description')
pogoda=p[0].getText()
print(pogoda.strip())
# =============================================================================
# 
# =============================================================================
import requests
from bs4 import BeautifulSoup

def get_upcoming_events(url):
    req = requests.get(url)
    events_dict = {}
    i = 0
    soup = BeautifulSoup(req.text, 'lxml')
    events = soup.find('div', {'class': 'events-box'}).findAll('div', {'class', 'unit span4 event '})

    for event in events:
        event_type = event.find('small').text
        event_title = event.find('h3', {'class', 'title'}).text
        event_desc = event.find('p', {'itemprop': 'description'}).text
        events_dict[i] = [event_type, event_title, event_desc]
        i += 1
    print(events_dict)
get_upcoming_events('https://runet-id.com/events/')
# =============================================================================
# 
# =============================================================================

import requests, bs4

def get_rate(a):
    s=requests.get('http://www.brokers-rating.ru/archive/')
    rate_dict= {}
    b=bs4.BeautifulSoup(s.text, 'lxml')
    rates= b.find('div', {'class':'table-responsive'}).findAll('tr')
    for rate in rates[1:]:
        rate_title= rate.find('a',{'class':'text-dark h6'}).text
        rate_year= rate.find('td',{'class':"align-middle text-center text-muted text-small"}).text
        rate_rating= rate.find('td',{'class':"align-middle text-center text-muted text-small"}).text
        rate_dict[rate_title]= [rate_year,rate_rating]
    print(rate_dict[a])
get_rate('Открытие Брокер')
        
a= b.select('.align-middle .text-dark h6')
aa=a[0].getText()
print(aa)