import re
import os
import sqlite3

con = sqlite3.connect('./data/bitchute_videos.db')

cur = con.cursor()

length_pattern = re.compile('<p class=\"length\">\s*(.+?)</p>')
channel_pattern = re.compile('<b>\s*<a style=\"width:100%;\" href=\"/channel/(.+?)\">')
date_pattern = re.compile('<div\s*class=\"pure-u-2-3\">\s*(.+)', re.MULTILINE ) #Multiline 
views_pattern = re.compile('<div\s*class=\"pure-u-1-3\"\s*style="text-align:right">\s*(.+)', re.MULTILINE ) #Multiline
id_title_pattern = re.compile('<p>\s*<a style=\"width:100%;\" href=\"/watch\?v=(.+?)\">\s*(.+?)</a>', re.MULTILINE ) #Multiline

errors = []           

dir = "./data/altcensored_pages/"
files =  os.listdir(dir)
for file in files:
    print(file)
    with open(dir + file, "r") as data:
       # try: 
            text = data.read()
            length_matches = re.findall(length_pattern,text)  
            channel_matches = re.findall(channel_pattern,text)  
            date_matches = re.findall(date_pattern,text)  
            views_matches = re.findall(views_pattern,text)  
            id_title_matches = re.findall(id_title_pattern,text)  
                
            for i in range(0, len(id_title_matches)):
                cur.execute('''INSERT into alt_censored_videos VALUES (?, ?, ?, ?, ?, ?)''',
                            (
                            id_title_matches[i][0],
                            length_matches[i],
                            channel_matches[i],
                            date_matches[i],
                            views_matches[i],
                            id_title_matches[i][1],
                            ))
       # except Exception :
         #   errors.append(file)

#con.commit()
print(len(errors))