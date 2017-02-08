from selenium import webdriver
import webbrowser, requests, bs4
import time
import datetime
import os

link = raw_input("Enter link of page want to download: ")		#link of page to download

for i in xrange(0,365):											#dsleep till 2am 
    # sleep until 2AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year,t.month,t.day,2,0)
    if t.hour >= 2:
        future += datetime.timedelta(days=1)
    time.sleep((future-t).seconds)

browser = webdriver.Chrome()

browser.get(link)													#open download page
	
elems = browser.find_elements_by_xpath("//a[@href]")				#find links
for elem in elems:
	try:
		webbrowser.open(elem.get_attribute("href"))					#open each links
	except TypeError:
		continue
    #print elem.get_attribute("href")


for i in xrange(0,365):                                          #dsleep till 2am 
    # sleep until 2AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year,t.month,t.day,5,0)
    if t.hour >= 5:
        future += datetime.timedelta(days=1)
    os.system("shutdown -h now")
