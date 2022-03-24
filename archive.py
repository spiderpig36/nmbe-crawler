import sys
from time import sleep
import requests

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
            finished = True
            lines.remove(save_url)
            f.seek(0)
            f.truncate()
            f.write('\n'.join(lines))
            print("saved: " + save_url)
            continue
        print("something went wrong: " + status_code + " " + save_url)
        print("Retrying... If this message presits contact support")

print("All items processed")