# -*- coding:utf-8 -*-
import gzip
import shutil
import requests
import time
import re


# Never use this function, in case for need
# def gzip_target():
#     with open(r'weights.txt', 'rb') as f_in, gzip.open('test.gz', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)


def get_the_web_content():
    r = requests.get('https://zero.sjeng.org/')
    if r.status_code == requests.codes.ok:
        print('OK')
    else:
        print('Something Error!')
    open('./LeelaZero_HTML.txt', 'w+', encoding='utf-8').write(r.text)


# download the target file and display a progressbar
def downloader(url, version, datetime):
    start = time.time()
    size = 0
    response = requests.get(url, stream=True)
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    #print(content_size)

    if response.status_code == 200:
        print('[File version]: ', version)
        print('[File size]: %0.2f MB' % (content_size / chunk_size / 1024))
        with open('weights.gz', 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                print('\r'+'[Download progress]:[%s%s]%.2f%%;' % ('█' * int(size * 20 / content_size), ' ' * (20 - int(size * 20 / content_size)), float(size / content_size * 100)), end='')
    end = time.time()
    print('\n'+'Donwload finished!')
    print('Download time:%.2f s' % (end-start))
    version_list_text = 'download date:' + str(time.localtime(time.time()).tm_year) + '-' + str(time.localtime(time.time()).tm_mon) + '-' + str(time.localtime(time.time()).tm_mday) + ' ' + str(time.localtime(time.time()).tm_hour) + ':' + str(time.localtime(time.time()).tm_min) + ':' + str(time.localtime(time.time()).tm_sec) + '------------------' + str(version) + ':' + datetime + ':' + url + '\n'
    open('download_version_list.txt', 'a+', encoding='utf-8').write(version_list_text)


# display all version
def display_all_version():
    content = open('./LeelaZero_HTML.txt', 'r', encoding='utf-8').read()
    results = re.findall('<tr><td>.+', content)
    version = len(results)

    for result in results:
        version -= 1
        datetime = re.findall('\d{4}\-\d{2}\-\d{2}', result)[0]
        text = re.findall('/networks.+', result)[0]
        text = re.sub('\.gz.+', '.gz', text)
        print(datetime, '版本號: ', version)
        print(text, '\n')


def display_all_version_reverse():
    content = open('./LeelaZero_HTML.txt', 'r', encoding='utf-8').read()
    results = re.findall('<tr><td>.+', content)
    results.reverse()
    version = 0

    for result in results:
        version += 1
        datetime = re.findall('\d{4}\-\d{2}\-\d{2}', result)[0]
        text = re.findall('/networks.+', result)[0]
        text = re.sub('\.gz.+', '.gz', text)
        print(datetime, 'Version: ', version)
        print(text, '\n')


# select the weights version you want
def select_the_version(vn):
    content = open('./LeelaZero_HTML.txt', 'r', encoding='utf-8').read()
    results = re.findall('<tr><td>.+', content)
    version = len(results)

    if vn < 0 or vn > version-1:
        print('The selected version is not exist.')
    else:
        for result in results:
            version -= 1
            datetime = re.findall('\d{4}\-\d{2}\-\d{2}', result)[0]
            text = re.findall('/networks.+', result)[0]
            text = re.sub('\.gz.+', '.gz', text)

            if version == vn:
                url = 'https://zero.sjeng.org' + text
                downloader(url, version, datetime)
                break


# auto upgrade
def auto_update():
    content = open('./LeelaZero_HTML.txt', 'r', encoding='utf-8').read()
    results = re.findall('<tr><td>.+', content)
    version = len(results)

    for result in results:
        version -= 1
        datetime = re.findall('\d{4}\-\d{2}\-\d{2}', result)[0]
        text = re.findall('/networks.+', result)[0]
        text = re.sub('\.gz.+', '.gz', text)
        url = 'https://zero.sjeng.org' + text
        downloader(url, version, datetime)
        break


if __name__ == '__main__':
    get_the_web_content()
    auto_update()
    # select_the_version(202)


