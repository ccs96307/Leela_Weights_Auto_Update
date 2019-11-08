# -*- coding: utf-8 -*-
import zipfile
import os
import time
import requests


# Settings
GPU = 1
win64 = 1
url = ''
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

if GPU and win64:
    url = 'https://github.com/leela-zero/leela-zero/releases/download/v0.17/leela-zero-0.17-win64.zip'
elif GPU and not win64:
    url = 'https://github.com/leela-zero/leela-zero/releases/download/v0.17/leela-zero-0.17-win32.zip'
elif not GPU and win64:
    url = 'https://github.com/leela-zero/leela-zero/releases/download/v0.17/leela-zero-0.17-cpuonly-win64.zip'
elif not GPU and not win64:
    url = 'https://github.com/leela-zero/leela-zero/releases/download/v0.17/leela-zero-0.17-cpuonly-win32.zip'
else:
    print('Uable to download. Something error.')
    exit()


def downloader(url):
    startTime = time.time()
    state = 0

    try:
        r = requests.get(url, stream=True, headers=headers)
        size = 0
        chunkSize = 1024
        contentSize = int(r.headers['content-length'])
        print('[File Size]: %.2f MB' % (contentSize/chunkSize/1024))
        if 'leelaz.zip' in os.listdir('./'):
            state = 1
            raise FileExistsError

        with open('leelaz.zip', 'wb') as file:
            for data in r.iter_content(chunk_size=chunkSize):
                file.write(data)
                size += len(data)
                print('\r'+'[Download progress]:[%s%s]%.2f%%;' % ('█'*int(size*20/contentSize), ' ' * (20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

        print('Time:', time.time()-startTime, 's')

    except:
        if not state: print('Download erorr.')
        else: print('The file is existed.')


def unzip():
    with zipfile.ZipFile('leelaz.zip', 'r') as file:
        for f in file.namelist():
            file.extract(f, './')


if __name__ == '__main__':
    # downloader(url)
    unzip()
