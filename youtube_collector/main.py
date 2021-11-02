from  googleapiclient.discovery  import build
api_key = 'AIzaSyDDK7s6j0OZlwm3Pb_5UOS2ccC9gEUaPBY'
service = build('youtube','v3', developerKey=api_key)

import csv
import os
import json

def write_file(file, data):
    dir = f"./data/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/{file}.txt', 'w', encoding="utf-8", newline='') as file:
        file.write(data)



skip = 1
stop_at = 100000
at = -1
erros = []
with open('channels_altcensored.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        
        at = at + 1
        if at < skip:
            continue
        if at > stop_at:
            break

        if os.path.exists(f"./data/{row[1]}.txt"):
            print(f"Já coletado: {row[1]}" )
            continue

        try:
            request = service.channels().list(
                    part='contentOwnerDetails,contentDetails,localizations,statistics,brandingSettings,topicDetails,id,status',
                    id=row[1]
                )

            response = request.execute()
            if response['pageInfo']['totalResults'] > 0:
                write_file(row[1], json.dumps(response['items'][0]))
            else: 
                erros.append(row[1])
        except:
            print(row[1])
            continue

write_file('erros', json.dumps(erros))