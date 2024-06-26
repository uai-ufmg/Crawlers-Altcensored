import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

def write_csv(folder, file, data, overwrite = True):
    dir = f"./data/{folder}"
    if not os.path.exists(dir):
        os.makedirs(dir)
    parameter = 'w' if overwrite else 'a'
    with open(f'{dir}/{file}.csv', parameter, encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file) 
        if data is not None:
            for d in data:
                writer.writerow(d)
        
default_url_preffix = r'https://socialblade.com/'
url_preffix = r'youtube/channel/'
default_url_suffix = r'/monthly'

blocked = []
blocked_file = "./data/block/0.csv"
if os.path.exists(blocked_file):
    with open(blocked_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            blocked.append(row[0])

driver = webdriver.Firefox()

skip = 1
stop_at = 100000
at = -1
with open('channels_altcensored.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        
        at = at + 1
        if at < skip:
            continue
        if at > stop_at:
            break

        if os.path.exists(f"./data/{row[1]}/0.csv"):
            print(f"Já coletado: {row[1]}" )
            continue

        if row[1] in blocked:
            print(f"Não coletado por bloqueio: {row[1]}" )
            continue
        

        url = default_url_preffix + url_preffix + row[1] + default_url_suffix

        try:
            driver.get(url)
        
            chart_quantity = driver.execute_script("return Highcharts.charts.length")
            if chart_quantity == 0:
                write_csv('block','0',[[row[1]]], overwrite=False)
                continue
            chart_title_array = []
            for chart_idx in range(chart_quantity):
                chart_title = driver.execute_script(f"return Highcharts.charts[{chart_idx}].title.textStr")
                data = driver.execute_script(f"return Highcharts.charts[{chart_idx}].options.series[0].data")
                write_csv(row[1],chart_idx,data)
                chart_title_array.append((chart_idx, chart_title))
            write_csv(row[1],"dados_coletados",chart_title_array)
        except:
            print(row[1])
            driver.close()
            time.sleep(10)
            driver = webdriver.Firefox()
            continue
driver.close()