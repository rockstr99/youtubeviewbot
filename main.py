from selenium import webdriver
import time
from random import randrange

print("THIS IS A YOUTUBE viewBOT, DEVELOPED BY ROCKSTR99")

LINK = input("Enter your youtube video link here: ")
TABS = int(input("Enter number of tabs (**warning this depends upon your system, it is not advisable to open more than 4 tabs**) : "))
TIME = int(input("Enter view time in seconds: "))

browser_list = []

for i in range(0, TABS):
    browser = webdriver.Chrome("./Driver//chromedriver.exe")
    browser_list.append(browser)    


for browser in browser_list : 
    browser.get (LINK)

while(True):
    for i in range(len(browser_list)):
        time.sleep(TIME)
        browser_list[i].refresh()
        print("Browser number: ", i, "has been refreshed !")
        