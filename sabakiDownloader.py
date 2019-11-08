# -*- coding: utf-8 -*-
"""
If there are later version existed, the application that you download will remind you.
"""
import os
import time
import platform
import requests


# Settings
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def downloader(url):
    startTime = time.time()
    state = 0

    try:
        r = requests.get(url, stream=True, headers=headers)
        size = 0
        chunkSize = 1024
        contentSize = int(r.headers['content-length'])
        print('[File Size]: %.2f MB' % (contentSize/chunkSize/1024))
        if 'sabaki.exe' in os.listdir('./'):
            state = 1
            raise FileExistsError

        with open('sabaki.exe', 'wb') as file:
            for data in r.iter_content(chunk_size=chunkSize):
                file.write(data)
                size += len(data)
                print('\r'+'[Download progress]:[%s%s]%.2f%%;' % ('█'*int(size*20/contentSize), ' ' * (20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

        print('Time:', time.time()-startTime, 's')

    except:
        if not state: print('Download erorr.')
        else: print('The file is existed.')


if __name__ == '__main__':
    url = 'https://github.com/SabakiHQ/Sabaki/releases/download/v0.43.3/sabaki-v0.43.3-win-x64-setup.exe'
    downloader(url)
    os.system('sabaki.exe')

