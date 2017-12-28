import os, urllib, shutil, sqlite3

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import urllib.request
import re

def updateDB(DB_filepath, table):
    if (os.path.isfile(DB_filepath)):
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()
        curUP = db.cursor()

        cur.execute("SELECT * FROM {tn}".format(tn=table))
        for row in cur:
            query = row[1].replace("_"," ")+" S"+row[2]+"E"+row[3]
            url = 'http://www.torrents9.pe/search_torrent/'+ row[1].replace("_","-") +'.html'
            # un tiret entre les mots
            req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
            response = urllib.request.urlopen( req )
            html = response.read()
            # Parsing response
            soup = BeautifulSoup(html, 'html.parser')
            res=None
            for heading in soup.body.find_all('a'):
                if re.search(query, heading.text) is not None:
                    res=heading.text
            if (res is None):
                res = "FALSE"
            else:
                res = "TRUE"
            #curUP.execute("UPDATE {tn} SET TORRENT = {to} WHERE ID= {wid}".format(tn=table, to=res, wid=row[0]))
            curUP.execute("UPDATE notify SET TORRENT = ? WHERE ID= ?",(res, row[0]))
            db.commit()
        cur.close()
        db.close()

updateDB("notify_db.sqlite", "notify")
