import os, sys, urllib, ConfigParser, shutil
from urlparse import urljoin
from Config_tools import ConfigSectionMap

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

fp = webdriver.FirefoxProfile()

notYetOnline=[]

### TORRENT9
def getUrlFromTorrent9(episodeName):
    driver.get("https://www.torrent9.biz/")
    elem = driver.find_element_by_name("champ_recherche")
    elem.send_keys(episodeName)
    elem.send_keys(Keys.RETURN)

    try:
        wait = WebDriverWait(driver, 5)
        element= wait.until(EC.presence_of_element_located((By.XPATH,"html/body/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/a")))
    except:
        notYetOnline.append(ml)
        return 0

    return element.get_attribute("href")
###

### NEXTORRENT
def getUrlFromNextorrent(episodeName):
    driver.get("https://www.nextorrent.net/")
    elem = driver.find_element_by_name("torrentSearch")
    elem.send_keys(episodeName)
    elem.send_keys(Keys.RETURN)

    try:
        wait = WebDriverWait(driver, 5)
        element= wait.until(EC.presence_of_element_located((By.XPATH,"html/body/div[5]/div[1]/div[2]/div/div/table/tbody/tr/td[1]/a[2]")))
    except:
        notYetOnline.append(ml)
        return 0

    return element.get_attribute("href")
###

def check_torrent(torrent_list):
    visible = ConfigSectionMap("MEDIABOT")['visible']
    global driver
    if (visible == "True"):
        driver = webdriver.Firefox(fp)
    elif (visible == "False"):        driver = webdriver.PhantomJS()
    else:
        print ("ERROR DRIVER CONFIG")
        exit()
    ##
    # TORRENT9
    print "="*63+"\n"+"DOWNLOAD\n"+"="*63+"\n"
    for ml in torrent_list:
        ml = ml.rstrip('\n')
        if ("Lethal Weapon" in ml):
            ml = ml.replace("Lethal Weapon","L'Arme Fatale")
        if ("A Series of Unfortunate Events" in ml):
            ml = ml.replace("A Series of Unfortunate Events","Les desastreuses aventures des orphelins Baudelaire")
        print ml
        url=getUrlFromTorrent9(ml)
        if (url != 0):
            # find torrent
            print ml

    print "\n"+"="*63+"\n"+"NOT YET ON TORRENT9\n"+"="*63+"\n"
    for nyo in notYetOnline:
        print "-> "+nyo

    ##
    # NEXTORRENT
    print "="*63+"\n"+"DOWNLOAD\n"+"="*63+"\n"
    content = notYetOnline[:]
    notYetOnline = []
    for ml in content:
        ml = ml.rstrip('\n')
        if ("Lethal Weapon" in ml):
            ml = ml.replace("Lethal Weapon","L'Arme Fatale")
        if ("A Series of Unfortunate Events" in ml):
            ml = ml.replace("A Series of Unfortunate Events","Les desastreuses aventures des orphelins Baudelaire")
        url=getUrlFromNextorrent(ml)
        if (url != 0):
            # find torrent
            print ml

    print "\n"+"="*63+"\n"+"NOT YET ON NEXTORRENT\n"+"="*63+"\n"
    for nyo in notYetOnline:
        print "-> "+nyo
    ###################
    #driver = FixProxy()
    driver.quit()

    return notYetOnline
