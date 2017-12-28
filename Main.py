from module.Config_tools import ConfigSectionMap
from module.Format import media_format
from module.Tidy import classify, tidy_up, internet_access
from module.Download import move_media
from module.Notification import notification_media

verbose = ConfigSectionMap("MEDIABOT")['verbose']

class bcolors:
    MOVIE = '\033[94m'
    SERIE = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__=="__main__":

    if (verbose == "True"):
        print "___  ___ ___________ _____  ___   ______  _____ _____\n|  \/  ||  ___|  _  \_   _|/ _ \  | ___ \|  _  |_   _|\n| .  . || |__ | | | | | | / /_\ \ | |_/ /| | | | | |\n| |\/| ||  __|| | | | | | |  _  | | ___ \| | | | | |\n| |  | || |___| |/ / _| |_| | | | | |_/ /\ \_/ / | |\n\_|  |_/\____/|___/  \___/\_| |_/ \____/  \___/  \_/\n"
        if (internet_access() == False):
            print bcolors.FAIL + "-- Please enable your internet connection for movie genre classification or serie notification --" + bcolors.ENDC
    download = ConfigSectionMap("MEDIABOT")['download']
    media = ConfigSectionMap("MEDIABOT")['media']
    # DOWNLOAD
    move_media(download,media)
    # FORMAT
    media_format(media)
    # TIDY UP
    classify(media)
    tidy_up(media+"/Serie")
    tidy_up(media+"/Movie")
    # NOTIFICATION
    #notification_media(media+"/Serie")
