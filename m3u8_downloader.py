
# coding: utf-8

"""
Auther: Guo Yang <guoyang@webmail.hzau.edu.cn>
Version: 0.1.1
"""

import os
import sys
import requests
import m3u8

def  check_path(_path):
    # check if download path exit
    if os.path.isdir(_path) or os.path.isabs(_path):
        # check if download path is empty
        if not os.listdir(_path):
            return _path

        else:

            print('>>>[-] folder not empty, continue?')
            flag = input('>>>[*] Yes:1 No:2 \n>>>[+] : ')

            try:
                if flag == '1':
                    return _path
                else:
                    _path = input('>>>[+] input download path:\n>>>[+] : ')
                    check_path(_path)
                    
            except Exception as e:
                print(e)
                exit(0)

    else:
        os.makedirs(_path)
        return _path



def m3u8_video_download(m3u8_url, url_static, _path='/Users/simonguo/Downloads/m3u8download'):
    m3u8_obj = m3u8.load(m3u8_url)
    full_web_url = []
    for file in m3u8_obj.files:
        # print(file)
        full_web_url.append(url_static + file)
    os.chdir(_path)
    print('>>>[+] downloading...')
    print('-' * 60)
    error_get = []
    
    file_No = 0
    
    for _url in full_web_url:
        # option 1: .ts files are stored using its original name on server
        # movie_name = _url.split('/')[11] # in my case name part is at 12th place in URL (sep with '/')        
        try:
            # 'Connection':'close' prevent port's occupation
            # timeout=30    prevent timeout  from being too long
            movie = requests.get(_url, headers = {'Connection':'close'}, timeout=60)
            # option 2: rename .ts files into numeric order like 1.ts, 2.ts, ... good for join
            file_No += 1
            movie_name = str(file_No)+'.ts'
            with open(movie_name, 'wb') as movie_content:
                movie_content.writelines(movie)  
            # option 1: output current file's name
            # print('>>>[+] File ', movie_name, ' in total ', len(full_web_url), ' files\tdone')
            # option 2: output progress bar 
            prograss = file_No * 50 / len(full_web_url)
            sys.stdout.write('\r>>>[+] progress: [%s%s] %d/%d files done' %('|' * round(prograss), (' ' * (50-round(prograss))), file_No, len(full_web_url)))
            sys.stdout.flush()
        # catch exceptionï¼Œlog bad request
        except:
            error_get.append(_url)
            continue
    if error_get:
        print('Warning: Total of %d request(s) failed, Retrying...' % len(file_list))
        print('-' * 60)
        download_movie(error_get, _path)
    # all file good, output msg
    else:
        print('\n>>>[+] Download successfully!!!')
    # join .ts files
    for filename in range(1, len(full_web_url)+1):
        os.system('cat ' + str(filename) + '.ts >> full.ts')



if __name__ == '__main__':
    try:

        _m3u8_url = input('>>>[+] input .m3u8 URL (absolute path on computer or full URL link on Internet):\n>>>[+] : ')
        _url_static = input('>>>[+] input static URL for .ts files on server (end with \'/\'):\n>>>[+] : ')
        _download_path = input('>>>[+] input download path (default path is \'default\'): \n>>>[+] : ')

        if _download_path == 'default':
            m3u8_video_download(_m3u8_url, _url_static)
        else:
            _download_path_checked = check_path(_download_path)
            m3u8_video_download(_m3u8_url, _url_static, _download_path_checked)   

    except Exception as e:
        print(e)

