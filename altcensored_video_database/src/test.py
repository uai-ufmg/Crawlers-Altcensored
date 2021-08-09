import re
import sqlite3

con = sqlite3.connect('''C:/Users/gabriel.freire/Documents/mestrado/pesquisa/bitchute_database/src/data/bitchute_videos.db''')

cur = con.cursor()

youtube_video_id_pattern = re.compile('https://www\.youtube\.com/watch\?v=(.+?)[\"|/|<|?:\s+|$]')
youtube = re.compile('youtube')

try:
    cur.execute('SELECT * FROM videos')
    
    for row in cur:        
            text = row[4]
            youtube_video_id_matches = re.findall(youtube_video_id_pattern,text) 
            yt = re.findall(youtube,text) 
            
            if (len (youtube_video_id_matches) > 0):
                cur.execute('UPDATE videos SET youtube_video = "' + str(list(set(youtube_video_id_matches))) + '" WHERE url = "' + row[0]  + '"') ;    
        
except:
        pass            

con.commit()

