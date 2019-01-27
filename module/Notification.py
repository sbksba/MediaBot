import re, sys, ConfigParser, ast, os, datetime, urllib, shutil, sqlite3
from os import listdir
from os.path import isdir, isfile, join, exists
from .Config_tools import ConfigSectionMap

try:
    import tmdbsimple as tmdb
except:
    print("TMDBSimple Module Installation...")
    os.system('python -m pip install tmdbsimple')
import tmdbsimple as tmdb

def internet_access():
    try:
        stri = "https://www.google.com"
        data = urllib.urlopen(stri)
        return True
    except:
        return False

tmdb.API_KEY = ConfigSectionMap("TMDB")['key']
verbose = ConfigSectionMap("MEDIABOT")['verbose']
torrent_notif = ConfigSectionMap("MEDIABOT")['torrent_notif']

class bcolors:
    COMPLETE = '\033[92m'
    NOTCOMPLETE = '\033[93m'
    EMPTY = '\033[91m'
    ENDC = '\033[0m'

## GLOBAL FUNCTIONS
def get_Serie_Id(serie_name):
    search = tmdb.Search()
    ser = search.tv(query=serie_name)
    serie_id = ""
    for s in ser.get('results'):
        serie_id = s['id']
        break

    return serie_id

def get_Last_Season_Number(serie_id):
    search = tmdb.TV(serie_id)
    ser = search.info()

    for s in ser.get("seasons"):
        if (s['season_number'] < 10):
            season_nb = "0"+str(s['season_number'])
        else:
            season_nb = str(s['season_number'])

    return season_nb

def get_Dict_Serie(mypath):
    if not os.path.exists(mypath):
        onlyfiles = []
    else:
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    key=1
    mydict = {}
    for f in onlyfiles:
        mydict [key] = f.rsplit('.',1)[0]
        key += 1

    return mydict
##

## NOT DISCRET
def check_serie(mypath,serie_name,serie_id,season_nb):
    mypath= mypath+serie_name+"/S"+season_nb
    mydict = get_Dict_Serie(mypath)
    search = tmdb.TV_Seasons(serie_id,season_nb)
    ser = search.info()
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    dict_need=[]

    for s in ser.get('episodes'):
        if (s['episode_number'] < 10):
                episode = serie_name+"_S"+season_nb+"E0"+str(s['episode_number'])
        else:
                episode = serie_name+"_S"+season_nb+"E"+str(s['episode_number'])
        if (episode in mydict.values()):
            continue
        elif(now > s['air_date'] and s['air_date'] is not None):
            dict_need.append(str(s['episode_number']))

    if (not dict_need):
        print(bcolors.COMPLETE + "-- Season Complete --    "+ bcolors.ENDC + "["+season_nb+"]")
    else:
        print bcolors.NOTCOMPLETE + "-- Season Not Complete --"+ bcolors.ENDC +"["+season_nb+"] EPISODES TO DOWNLOAD -> ",
        print(dict_need)

def get_first_episode_last_season(mypath,serie_name,serie_id,season_nb):
    mypath= mypath+serie_name+"/S"+season_nb
    mydict = get_Dict_Serie(mypath)
    search = tmdb.TV_Seasons(serie_id,season_nb)
    ser = search.info()
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    date = ""
    
    for s in ser.get('episodes'):
        if (isinstance(s['air_date'],type(None))):
            date = "UNKNOWN"
        else:
            date = s['air_date']
        
        if (now > s['air_date'] and s['air_date'] is not None):
            print(bcolors.EMPTY + "-- Season To Download -- "+ bcolors.ENDC + "["+season_nb+"] PRESENT ONLINE (" +date+")")
        else:
            print(bcolors.EMPTY + "-- Season To Download -- "+ bcolors.ENDC + "["+season_nb+"] NOT PRESENT ONLINE (" +date+")")
        break
        
def notifcation_serie(directory):
    if (verbose == "True"):
        if (internet_access() == False):
            print(bcolors.EMPTY + "-- NOTIFICATION -- " + bcolors.ENDC + " ["+directory+"]")
            exit()
        else:
            print(bcolors.COMPLETE + "-- NOTIFICATION -- " + bcolors.ENDC + " ["+directory+"]")
    mypath = directory
    series = [f for f in listdir(mypath) if isdir(join(mypath, f))]

    for serie in series:
        name = serie.replace("_"," ").rsplit('.',1)[0]
        serie_id = get_Serie_Id(name)
        last_season = int(get_Last_Season_Number(serie_id))
        season = ""
        print("\n## "+name+" ##")
        for s in range(1,last_season+1):
            if (s < 10):
                season = "0"+str(s)
            else:
                season = str(s)
            if (isdir(join(mypath+"/"+serie+"/S"+season))):
                check_serie(mypath+"/",serie,serie_id,season)
            else:
                if (s == last_season):
                    get_first_episode_last_season(mypath+"/",serie,serie_id,season)
                else:
                    print(bcolors.EMPTY + "-- Season To Download -- "+ bcolors.ENDC + "["+season+"]")

## DISCRET
def discret_check_serie(mypath,serie_name,serie_id,season_nb):
    mypath= mypath+serie_name+"/S"+season_nb
    mydict = get_Dict_Serie(mypath)
    search = tmdb.TV_Seasons(serie_id,season_nb)
    ser = search.info()
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    dict_need=[]
    torrent_list=[]

    for s in ser.get('episodes'):
        if (s['episode_number'] < 10):
                episode = serie_name+"_S"+season_nb+"E0"+str(s['episode_number'])
        else:
                episode = serie_name+"_S"+season_nb+"E"+str(s['episode_number'])
        if (episode in mydict.values()):
            continue
        elif(now > s['air_date'] and s['air_date'] is not None):
            torrent_list.append(episode)

    return torrent_list

def discret_notifcation_serie(directory):
    if (verbose == "True"):
        if (internet_access() == False):
            print(bcolors.EMPTY + "-- NOTIFICATION -- " + bcolors.ENDC + " ["+directory+"]")
            exit()

    mypath = directory
    series = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    torrent_list = []
    for serie in series:
        name = serie.replace("_"," ").rsplit('.',1)[0]
        serie_id = get_Serie_Id(name)
        last_season = int(get_Last_Season_Number(serie_id))
        season = ""
        for s in range(1,last_season+1):
            if (s < 10):
                season = "0"+str(s)
            else:
                season = str(s)
            if (isdir(join(mypath+"/"+serie+"/S"+season))):
                tmp = discret_check_serie(mypath+"/",serie,serie_id,season)
                if tmp:
                    torrent_list.append(tmp)

    return sum(torrent_list,[])

def notify_database(torrent_list, DB_filepath):
    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()
    cur.executescript("""
    DROP TABLE IF EXISTS notify;
    CREATE TABLE notify (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, SEASON TEXT, EPISODE TEXT, TORRENT TEXT);
    """)

    for torrent in torrent_list:
        name    = torrent.rsplit("_",1)[0]
        season  = torrent.rsplit("_",1)[1].rsplit("E",1)[0].rsplit("S",1)[1]
        episode = torrent.rsplit("_",1)[1].rsplit("E",1)[1]
        torrent_exist = "FALSE"
        to_db = [unicode(name, "utf8"), unicode(season, "utf8"), unicode(episode, "utf8"), unicode(torrent_exist, "utf8")]
        cur.execute("INSERT INTO notify (NAME, SEASON, EPISODE, TORRENT) VALUES(?, ?, ?, ?);", to_db)
        db.commit()

    cur.close()
    db.close()

def print_notify_database(DB_filepath,table):
    if (os.path.isfile(DB_filepath)):
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()

        cur.execute("SELECT * FROM {tn}".format(tn=table))
        print("")
        for row in cur:
            print("{:4}|{:50}|{:3}|{:3}|{}".format(row[0], row[1].encode('utf-8'), row[2].encode('utf-8'), row[3].encode('utf-8'), row[4].encode('utf-8')))
        cur.close()
        db.close()

def print_download_database(DB_filepath,table):
    if (os.path.isfile(DB_filepath)):
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()
        i=0
        cur.execute("SELECT * FROM {tn} WHERE TORRENT='TRUE'".format(tn=table))
        print("\nAVAILABLE TORRENTS\n==================\n")
        for row in cur:
            i=i+1
            print("{}_S{}E{}".format(row[1].encode('utf-8'), row[2].encode('utf-8'), row[3].encode('utf-8')))
        if (i==0):
            print("NONE")
        cur.close()
        db.close()

###
def notification_media(directory):
    if (verbose == "True"):
        notifcation_serie(directory)

    if (torrent_notif == "True"):
        torrent = []
        torrent = discret_notifcation_serie(directory)
        notify_database(torrent,"notify_db.sqlite")
        os.system("python3 module/Torrent.py")
        #print_notify_database("notify_db.sqlite", "notify")
        print_download_database("notify_db.sqlite", "notify")
