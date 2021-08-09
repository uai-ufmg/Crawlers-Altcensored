import re
import sqlite3

def remove_erros_regex_matches(matches):
    ret = []
    for x in matches:
        if len(x) < 2:
            continue
        if '"' in x:
            continue
        ret.append(x)
    return ret
    

con = sqlite3.connect('''C:/Users/gabriel.freire/Documents/mestrado/pesquisa/bitchute_database/src/data/videos.db''')
con_views = sqlite3.connect('''C:/Users/gabriel.freire/Documents/mestrado/pesquisa/bitchute_database/src/data/views.db''')

cur = con.cursor()
cur_views = con_views.cursor()

youtube_channel_user_pattern = re.compile('https://www\.youtube\.com/user/(.+?)[\"|/|<|?:\s+|$]')
youtube_channel_user_pattern_2 = re.compile('https://www\.youtube\.com/c/(.+?)[\"|/|<|?:\s+|$]')
youtube_video_id_pattern = re.compile('https://www\.youtube\.com/watch\?v=(.+?)[\"|/|<|?:\s+|$]')
youtube_video_id_pattern_2 = re.compile('https://youtu\.be/(.+?)[\"|/|<|?:\s+|$]')
youtube_channel_id_pattern = re.compile('https://www\.youtube\.com/channel/(.+?)[\"|/|<|?:\s+|$]')

erros = []
cur.execute('SELECT * FROM videos WHERE views is NULL')
videos_info = cur.fetchall()
total = len(videos_info)
i = 0
for row in videos_info:
    try:
        print(total - i)
        i += 1
        text = row[4]
        youtube_channel_id_matches = re.findall(youtube_channel_id_pattern,text) 
        youtube_channel_user_matches = re.findall(youtube_channel_user_pattern,text) 
        youtube_channel_user_matches.extend(re.findall(youtube_channel_user_pattern_2, text))
        youtube_video_id_matches = re.findall(youtube_video_id_pattern,text) 
        youtube_video_id_matches.extend(re.findall(youtube_video_id_pattern_2, text))

        youtube_channel_id_matches = remove_erros_regex_matches(youtube_channel_id_matches)  
        youtube_channel_user_matches = remove_erros_regex_matches(youtube_channel_user_matches)  
        youtube_video_id_matches = remove_erros_regex_matches(youtube_video_id_matches)  

        cur_views.execute('SELECT views FROM views WHERE url = "' + row[0]  + '"')
        views = cur_views.fetchone()
        if views is None:
            views = [-400]

        cur.execute('UPDATE videos SET views = "' + str(views[0]) + '" , youtube_channel = "' + str(list(set(youtube_channel_id_matches))) + '" , youtube_user = "' + str(list(set(youtube_channel_user_matches))) + '" , youtube_video = "' + str(list(set(youtube_video_id_matches))) +  '" WHERE url = "' + row[0]  + '"') ;      
    except Exception :
        erros.append(row[0])

print(erros)
con.commit()

