import re, shutil
from Config_tools import ConfigSectionMap
from os import listdir
from os.path import isfile, join, exists
#import tmdbsimple as tmdb

#tmdb.API_KEY = ConfigSectionMap("TMDB")['key']

# Move the media files from the download directory to the directory "directory"
def move_media(directory_download, directory_target):
    mypath = directory_download
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for of in onlyfiles:
        media_file = re.search('\.(avi|mp4|mkv)$', of)
        if media_file is not None:
            shutil.move(join(mypath,of),directory_target+"/"+of)
