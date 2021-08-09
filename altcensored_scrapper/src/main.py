import requests
from app import file_manager
import re
from datetime import date
import time

request_cookies = {}
request_cookies["session"] = ".eJzNksuOgzAMRf_FaxYhQx_wLZUqDxiIlDooj6pV1X-fBErUx6bL2UTx9Y11bOcG7YjMpFsT2ENTy2pXQBfjF1mKvShAmxY1QQOThxSZSSsXs94GKoDx7PHXQXN7XMvoPB-CENR1ZGB1yCi3yKiz8pNKarzO1Vaxmm2eBmMVZnWTVMO9GoLFufYunf2GXPZsoye4MGdLqwzcM9xRcUeXN0T1Qbf0_jXf9QXPkfeKh3cess8cE9nT_5zUWv6x-VJUi8Z0iWGP2sVd-5FO6SNoNYwJJLWXH8himekqbKu6lvc_TKPNDQ.YPTh4g.tAm6maTYyMBVvvlR-dFadwK2Mkw"

request_headers_list = {
    'Host': 'www.altcensored.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

data = date.today().strftime("%Y%m%d")
i = 1
while True:
    print(i)
    request = requests.get('https://www.altcensored.com/page/' + str(i), headers=request_headers_list, cookies=request_cookies)
    
    if request.status_code != 200:
        break

    pattern = 'href=\"/watch'    
    all_matches = re.findall(pattern, request.text) 
    
    if len(all_matches) > 0:
        file_manager.write_data(request.text,"video/" + "/list/" +  date.today().strftime("%Y%m%d"), str(i) + ".txt")
        i += 1
    else:
        break

