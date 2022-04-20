import sys
from time import sleep
import requests
import re
import json
import time

f = open(sys.argv[1], 'r')
text = f.read()
lines = text.split('\n')

f = open(sys.argv[1], "a")

for save_url in lines:
    finished = False
    while not finished:
        data = {
            'url': save_url,
            'capture_all': 'on'
        }
        response = requests.post("https://web.archive.org/save/" + save_url, data)
        status_code = response.status_code
        if status_code == 429:
            retry_after = response.headers['Retry-After']
            sleep(int(retry_after))
            continue
        if status_code == 200:
            spn2 = re.search('spn.watchJob\("spn2-([\d\w]*)"', response.text).group(1)
            pending = True
            while pending:
                spn2_response = requests.get("https://web.archive.org/save/status/spn2-" + spn2 + "?_t=" + str(time.time())).json()
                if spn2_response["status"] != "pending":
                    pending = False
                    finished = True
                    if spn2_response["status"] == "success":
                        lines.remove(save_url)
                        f.seek(0)
                        f.truncate()
                        f.write('\n'.join(lines))
                        print("saved: " + save_url)
                    else:
                        print("not saved: " + save_url)
                        print("reason: " + spn2_response["message"])
                    continue
                sleep(5)
            continue
        print("Something went wrong with the request: " + str(status_code) + " " + save_url)
        print("Retrying... If this message presits contact support")

print("All items processed")