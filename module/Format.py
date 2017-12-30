import re, shutil
from Config_tools import ConfigSectionMap
from os import listdir
from os.path import isfile, join

verbose = ConfigSectionMap("MEDIABOT")['verbose']

class bcolors:
    MOVIE = '\033[94m'
    SERIE = '\033[92m'
    ENDC = '\033[0m'

def format_movie(filename):
    movie_filter = ["20[0-9]{2}","19[0-9]{2}","(AC|ac)[0-9]{1}","(x|X)[0-9]{3}-Pop","(x|X)[0-9]{3}","(H|h)[0-9]{3}","R[0-9]{1}","Pimp[0-9]{4}","(DTS|HDTS)","DD[0-9]{1}","[0-9]{3}(MB|mb)","(V|R)[0-9]{1}","MP[0-9]{1}","dvdrip","(1080|720|480)(p|P)","(TRUEFRENCH|TRUFRENCH|truefrench)","(FRENCH|french)","(ENGLISH|ENG)","VOSTFR","BRR(iP|ip|IP)","(brrip|BRrip)","BD(Rip|RIP|RiP)","bdrip","(BluRay|bluray|Bluray|BLURAY)","DVDR(IP|ip|iP)","DVDrip","DVD(SCR|Scr|scr)","WiHD","HD(CAM|TV|Rip|RiP)","HD","C(AM|am)","WEB(Rip|RiP|riP)","WEB-DL","MD","X(ViD|viD|vid|VID|Vid)","RERIP|RERiP","AUDIO","AAC","Source","New","PROPER","BladeBDP","ARTEFAC","(RARBG|rarbg)","QCP","VAiN","Visual","NEW","ShAaNiG","RARBG","SOURCE","HC","BLiTZCRiEG","CH","WEEDMADE","S.V","rough","YIFY","MOi","UTT","CRYS","Isisatis","goatlove","NIKOo","MAXSPEED","ATN","VERSUS","Dossinet","(DesTroY|destroy)","SHiFT","STVFRV","FRV","STR","SLaP","FB","FANSUB","SUBFORCED","BROTHERS","CARPEDIEM","REPACK","TiTAN","TMB","CPG","READNFO","SVR","US","SaM","ETRG","CpasBien","REsuRRecTioN","NIKOo","(GLUPS|glups)","FIRST","www\.torentz\.3xforum\.ro","TS","MrSeeN","SiMPLE","ADDiCTiON","KRiNe","(RELIC|relic|RELiC)","ooOoo","VENUM","LiBERTY","FIX","Hive","CM[0-9]{1}","(HQ|Hq|hq)","LiberTeam","Z[0-9]{1}","REMUX","MULTi","^Pop'$'","Ofek","MAXSPEED","BluDragon","(anoXmous|anoxmous)","AiRLiNE","Remastered","dvdsize","quality","murdoc[0-9]{2}","yify","aac","(extended|EXTENDED|Extended)","BLOW","x0r","AVC","w{3}","OMGTORRENT","com","cinefile","AtomicGdog","zetorrents","ofek","ShowFr","zip","(blu|Blu)","ray","MA","fullhd","best","gaia","filou","5.1","(Final|final)","(Cut|cut)","Rip","vf","vost","dir","MURD3R","AViTECH","AViTE","RaStA","walt\.disney\.","Walt Disney - ","UNRATED","WEB","RIP","FANTA","BLUB","KK3N","Slay3R","TeamSuW","ZT","cpasbien","pw","Mystic","BoSs","RUDY","LOST","VENUE","SANSDouTE","LYS","MZISYS","MRG","zone","telechargement","Cortex91","EXTREME","ViVi","TRT","FUNKKY","eVe","LiMiTED","RERip","GODSPACE","ACOOL","CTOM","Workshop","AlloTeaM","[0-9]{1}CD","(torrent9|Torrent9)","EBD","BLURRED","T9","GZR","(WWW|www|WwW)","tv"]

    filename = re.sub('^\[.*\]\s*','',filename)
    for i in range(len(movie_filter)):
        filename = re.sub(movie_filter[i],'',filename)

    filename = re.sub('[\. \-\+]','_',filename)
    filename = re.sub('{\. \-\+}','_',filename)
    filename = re.sub('\[.*\]','',filename)
    filename = re.sub('\(.*\)','',filename)
    filename = re.sub('\{.*\}','',filename)
    filename = re.sub('_(avi|mp4|mkv)$',r'.\1',filename)
    filename = re.sub('\_*\.','.',filename)

    return filename

def format_serie(filename):
    filename = re.sub('\(.*\)\s*','',filename)
    filename = re.sub('US.','',filename)
    filename = re.sub('UK.','',filename)
    filename = re.sub('FASTSUB.','',filename)
    filename = re.sub('VOSTFR.','',filename)
    filename = re.sub('.201[0-9].',' ',filename)
    filename = re.sub('^\[.*\]\s*','',filename)
    filename = re.sub('[\. \-]','_',filename)
    filename = re.sub('_(avi|mp4|mkv)$',r'.\1',filename)
    filename = re.sub('(.*(S[0-9]{2}E[0-9]{2}))(.*)(.(avi|mp4|mkv))$',r'\1\4',filename)

    return filename

def media_format(directory):
    if (verbose == "True"):
        print bcolors.SERIE + "-- MEDIA FORMAT -- " + bcolors.ENDC + " ["+directory+"]"
    mypath = directory
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for of in onlyfiles:
        media_file = re.search('\.(avi|mp4|mkv)$', of)
        if media_file is not None:
            serie_file = re.search('S[0-9]{2}E[0-9]{2}', of)
            if serie_file is not None:
                n = format_serie(of)
                new = join(mypath, n)
                shutil.move(join(mypath,of),new)
                if (verbose == "True"):
                    print bcolors.SERIE + "\t-- SERIE -- " + bcolors.ENDC + n
            else:
                n = format_movie(of)
                new = join(mypath, n)
                shutil.move(join(mypath,of),new)
                if (verbose == "True"):
                    print bcolors.MOVIE + "\t-- MOVIE -- " + bcolors.ENDC + n
