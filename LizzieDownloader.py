# -*- coding: utf-8 -*-
import zipfile
import os
import time
import requests


# Settings
GPU = 1
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

if GPU:
    url = 'https://github.com/featurecat/lizzie/releases/download/0.7.2/Lizzie.0.7.2.Windows.x64.GPU.zip'
elif not GPU:
    url = 'https://github.com/featurecat/lizzie/releases/download/0.7.2/Lizzie.0.7.2.Windows.x64.CPU.zip'
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
        if 'Lizzie.zip' in os.listdir('./'):
            state = 1
            raise FileExistsError

        with open('Lizzie.zip', 'wb') as file:
            for data in r.iter_content(chunk_size=chunkSize):
                file.write(data)
                size += len(data)
                print('\r'+'[Download progress]:[%s%s]%.2f%%;' % ('█'*int(size*20/contentSize), ' ' * (20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

        print('Time:', time.time()-startTime, 's')

    except:
        if not state: print('Download erorr.')
        else: print('The file is existed.')


def unzip():
    with zipfile.ZipFile('Lizzie.zip', 'r') as file:
        for f in file.namelist():
            file.extract(f, './')


if __name__ == '__main__':
    # downloader(url)
    # unzip()