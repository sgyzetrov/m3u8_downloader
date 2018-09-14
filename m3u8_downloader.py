
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
    # 判断存储路径是否存在
    if os.path.isdir(_path) or os.path.isabs(_path):
        # 判断存储路径是否为空
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
        # 选项1: .ts视频保存在本地的名称为本身在服务器上的名称
        # movie_name = _url.split('/')[11] # 针对具体问题，这里文件名是在url以‘/’分割后的第12个位置，故取index 12-1 [因为index从0开始]        
        try:
            # 'Connection':'close' 防止请求端口占用
            # timeout=30    防止请求时间超长连接
            movie = requests.get(_url, headers = {'Connection':'close'}, timeout=60)
            # 选项2: 按照数字顺序重命名，利于合并        
            file_No += 1
            movie_name = str(file_No)+'.ts'
            with open(movie_name, 'wb') as movie_content:
                movie_content.writelines(movie)  
            # 选项1: 打印当前下载文件
            # print('>>>[+] File ', movie_name, ' in total ', len(full_web_url), ' files\tdone')
            # 选项2: 打印直观进度条
            prograss = file_No * 50 / len(full_web_url)
            sys.stdout.write('\r>>>[+] progress: [%s%s] %d/%d files done' %('|' * round(prograss), (' ' * (50-round(prograss))), file_No, len(full_web_url)))
            sys.stdout.flush()
        # 捕获异常，记录失败请求
        except:
            error_get.append(_url)
            continue
    if error_get:
        print('Warning: Total of %d request(s) failed, Retrying...' % len(file_list))
        print('-' * 60)
        download_movie(error_get, _path)
    # 如果没有不成功的请求就结束
    else:
        print('\n>>>[+] Download successfully!!!')
    # 合并.ts文件
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

