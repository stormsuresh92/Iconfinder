from requests_html import HTMLSession
import os
from tqdm import tqdm
import time


s = HTMLSession()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
    }

key = input('Enter your keyword here: ')
cur_dir = os.getcwd()
out = cur_dir + f'/{key}'
if not os.path.exists(out):
    os.mkdir(out)

url = f'https://www.iconfinder.com/search?q={key}&price=free'
r = s.get(url, headers=headers)
icons = r.html.find('div.icon-preview  ')
for icon in tqdm(icons):
    try:
        images = icon.find('img.d-block ', first=True).attrs['src']
        image = s.get(images, stream=True)
        name = os.path.basename(images)
        with open(out + '/' + name, 'wb') as f:
            f.write(image.content)
    except:
        pass

input()
