import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

def write_csv(folder, file, data):
    dir = f"./data/{folder}"
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/{file}.csv', 'w', encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file) 
        if data is not None:
            for d in data:
                writer.writerow(d)
        
default_url_preffix = r'https://socialblade.com/'
url_preffix = r'youtube/channel/'
default_url_suffix = r'/monthly'

skip = 74
at = -1
with open('channels_altcensored.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        at = at + 1
        if at < skip:
            continue

        url = default_url_preffix + url_preffix + row[1] + default_url_suffix

        driver = webdriver.Firefox()
        try:
            driver.get(url)
        
            chart_quantity = driver.execute_script("return Highcharts.charts.length")
            chart_title_array = []
            for chart_idx in range(chart_quantity):
                chart_title = driver.execute_script(f"return Highcharts.charts[{chart_idx}].title.textStr")
                data = driver.execute_script(f"return Highcharts.charts[{chart_idx}].options.series[0].data")
                write_csv(row[1],chart_idx,data)
                chart_title_array.append((chart_idx, chart_title))
            write_csv(row[1],"dados_coletados",chart_title_array)
            driver.close()
        except:
            print(row[1])
            time.sleep(10)
            continue