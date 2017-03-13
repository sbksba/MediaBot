import re, sys, ConfigParser, ast, os, datetime
from Config_tools import ConfigSectionMap
from Tidy import internet_access
import tmdbsimple as tmdb
from os import listdir
from os.path import isdir, isfile, join, exists

tmdb.API_KEY = ConfigSectionMap("TMDB")['key']
verbose = ConfigSectionMap("MEDIABOT")['verbose']
debug = ConfigSectionMap("MEDIABOT")['debug']

class bcolors:
    COMPLETE = '\033[92m'
    NOTCOMPLETE = '\033[93m'
    EMPTY = '\033[91m'
    ENDC = '\033[0m'

## SERIE
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
        if (debug == "True"):
            print bcolors.COMPLETE + "-- Season Complete --"+ bcolors.ENDC + "["+season_nb+"]"
    else:
        if (debug == "True"):
            print bcolors.NOTCOMPLETE + "-- Season Not Complete --"+ bcolors.ENDC +"["+season_nb+"] Episodes to download -> ",
            print dict_need
######

def notifcation_serie(directory):
    if (verbose == "True"):
        if (internet_access() == False):
            print bcolors.EMPTY + "-- NOTIFICATION -- " + bcolors.ENDC + " ["+directory+"]"
            exit()
        else:
            print bcolors.COMPLETE + "-- NOTIFICATION -- " + bcolors.ENDC + " ["+directory+"]"
    mypath = directory
    series = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    for serie in series:
        name = serie.replace("_"," ").rsplit('.',1)[0]
        serie_id = get_Serie_Id(name)
        last_season = int(get_Last_Season_Number(serie_id))
        season = ""
        print "\n## "+name+" ##"
        for s in range(1,last_season+1):
            if (s < 10):
                season = "0"+str(s)
            else:
                season = str(s)
            if (isdir(join(mypath+"/"+serie+"/S"+season))):
                check_serie(mypath+"/",serie,serie_id,season)
            else:
                if (debug == "True"):
                    print bcolors.EMPTY + "-- Season Download --"+ bcolors.ENDC + "["+season+"]"

if __name__=="__main__":
    #serie = ConfigSectionMap("MEDIABOT")['media']+"/Serie"
    serie = "/home/sbksba/nyx/Media/Movie/Serie"
    notifcation_serie(serie)
