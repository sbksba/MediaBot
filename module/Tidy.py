import re, shutil, urllib
from Config_tools import ConfigSectionMap
from os import listdir, makedirs
from os.path import isfile, join, exists
import tmdbsimple as tmdb

tmdb.API_KEY = ConfigSectionMap("TMDB")['key']
verbose = ConfigSectionMap("MEDIABOT")['verbose']
debug = ConfigSectionMap("MEDIABOT")['debug']

class bcolors:
    MOVIE = '\033[94m'
    SERIE = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

# Create the directory "directory"
def create_directory(directory):
    if not exists(directory):
        if (debug == "True"):
            media_dir = re.sub(directory+"/(Serie|Movie)/",'',directory)
            print bcolors.WARNING + "\t-- Create Directory --"+ bcolors.ENDC + " ["+media_dir+"]"
        makedirs(directory)

# Dispatch every media file in their respective directory (movies in Movie and
# series in Serie)
def classify(directory):
    #print bcolors.SERIE + "-- CLASSIFY -- " + bcolors.ENDC + " ["+directory+"]"
    create_directory(directory+"/Movie")
    create_directory(directory+"/Serie")
    mypath = directory
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for of in onlyfiles:
        media_file = re.search('\.(avi|mp4|mkv)$', of)
        if media_file is not None:
            serie_file = re.search('S[0-9]{2}E[0-9]{2}', of)
            if serie_file is not None:
                shutil.move(join(mypath,of),mypath+"/Serie/"+of)
            else:
                shutil.move(join(mypath,of),mypath+"/Movie/"+of)

# Test if internet is accessible
def internet_access():
    try:
        stri = "https://www.google.com"
        data = urllib.urlopen(stri)
        return True
    except:
        return False

def get_genre_name(s,list_genre):
    gId=gName=""
    for tmp in s['genre_ids']:
        gId = tmp
        break
    for g in list_genre.get('genres'):
        if (g['id'] == gId):
            gName = g['name']

    return gName

def getGenre(filename):
    search = tmdb.Search()
    genre = tmdb.Genres()
    responseM = search.movie(query=filename.replace("_"," ").rsplit('.',1)[0])
    responseG = genre.list()
    for s in responseM.get('results'):
        # GET GENRE NAME
        gName = get_genre_name(s,responseG)
        return gName

# Tidy up the directory "directory"
# IDEA -> for Movie a pourcentage bar
def tidy_up(directory):
    if (verbose == "True"):
        print bcolors.SERIE + "-- TIDY UP -- " + bcolors.ENDC + "      ["+directory+"]"
    mypath = directory
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for of in onlyfiles:
        media_file = re.search('\.(avi|mp4|mkv)$', of)
        if media_file is not None:
            # SERIE
            serie_file = re.search('S[0-9]{2}E[0-9]{2}', of)
            if serie_file is not None:
                serie  = re.sub('S[0-9]{2}E[0-9]{2}\.(avi|mkv|mp4)','',of)
                serie  = re.sub('_$','',serie)
                season = re.sub('(.*)(S[0-9]{2})(.*)',r'\2',of)
                newpath = mypath+"/"+serie+"/"+season
                create_directory(newpath)
                shutil.move(join(mypath,of),newpath+"/"+of)
            # Movie -> need to increase the speed
            else:
                if (internet_access() == True):
                    genre = getGenre(of)
                    if (genre is None):
                        genre = "None"
                else:
                    genre = "None"
                newpath = mypath+"/"+genre.encode('utf-8')
                create_directory(newpath)
                shutil.move(join(mypath,of),newpath+"/"+of)
