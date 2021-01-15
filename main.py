from selenium import webdriver
from functions import *

browser = webdriver.Chrome('chromedriver.exe')

username = input('Username: ')
password = input('Password: ')

usersToIgnoreStartRangeString = input('Ignore from ID# (leave blank and hit enter to ignore all): ')

if usersToIgnoreStartRangeString == '':
    login(username, password, browser)
    ignoreUsers(browser)
else:
    usersToIgnoreStartRange = int(usersToIgnoreStartRangeString)
    usersToIgnoreEndRange = int(input('Ignore to ID# (The last is currently around 32500): '))
    login(username, password, browser)
    ignoreUsers(browser, usersToIgnoreStartRange, usersToIgnoreEndRange)
