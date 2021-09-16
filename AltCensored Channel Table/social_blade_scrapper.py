import csv
import requests


headers = {}
headers['authority'] = r"socialblade.com"
headers['method'] = r"GET"
headers['scheme'] = r"https"
headers['accept'] = r"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers['accept-language'] = r"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
headers['cache-control'] = r"max-age=0"
headers['sec-ch-ua'] = r'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
headers['sec-ch-ua-mobile'] = r"?0"
headers['sec-fetch-dest'] = r"document"
headers['sec-fetch-mode'] = r"navigate"
headers['sec-fetch-site'] = r"same-origin"
headers['upgrade-insecure-requests'] = r"1"
headers['user-agent'] = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
headers['cookie'] = r"_dlt=1; _dlt=1; _ga=GA1.2.1498557786.1627331772; __auc=5ff07e8c17ae48841aaa33253d4; __qca=P0-1969319539-1627331773344; _pbjs_userid_consent_data=3524755945110770; __gads=ID=4d5f13f4aa3815fb:T=1627331782:S=ALNI_MYXXgGpgH5bNfth4rg364PSqacmqg; cf_clearance=db74122149a6a36506d8f7d6c8a2f6874165e0d5-1629220384-0-150; _gid=GA1.2.1726575831.1630357564; __asc=3fbe4d1e17b98e22b03d5727bb0; _dlt=1; PHPSESSXX=4f0auaod1bkue2hgjn3h3f6lue; _clck=1mcvvur|1|eub|0; cto_bundle=uMCwL19kUVM3QjUlMkJxU0tQWnVOOEtVMTIydnNJS0oyZHh3JTJGT2tDNTl4dld1SFdiR04lMkYybmtmRlklMkJiZTVZb2U2MFd5YTgweXJIZzlCMGFyVHBDYUVmayUyQjhYdmFzVjRYSWkyaTlrNkxRWXJFZ1RuNXRPSjE5bERKQUxuME1MV1VRdzFabENPUGV0d1pFcEdpWVJhYU8lMkZqZUxmWVElM0QlM0Q; _clsk=1gbba5i|1630360699035|2|1|b.clarity.ms/collect; lngtd-sdp=7"

    
def download_file(url, local_filename, headers):
    folder_text = "data/text/"
    folder_content = "data/content/"
    with requests.get(url, headers=headers) as r:
        if r.status_code == 200:
            with open(folder_text + local_filename, 'w', encoding="utf-8") as f:
                f.write(r.text)
            with open(folder_content + local_filename, 'wb') as f:
                f.write(r.content)
        else:
            print(f"Error: {r.status_code} {url}")

    return local_filename



default_url_preffix = r'https://socialblade.com/'
url_preffix = r'youtube/channel/'
default_url_suffix = r'/monthly'

with open('channels_altcensored.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        url = default_url_preffix + url_preffix + row[1] + default_url_suffix
        headers['path'] = url_preffix + row[1] + default_url_suffix
        headers['referer'] = url
        download_file(url, row[1], headers )