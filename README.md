<img align="center" src='./m3u8_downloader_banner.png'/>

# m3u8_downloader

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8a0bfb403d8b417ab605e4ca1fc4690c)](https://www.codacy.com/app/sgyzetrov/m3u8_downloader4XDF?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sgyzetrov/m3u8_downloader4XDF&amp;utm_campaign=Badge_Grade)

`.m3u8` video downloader used to download free class on [Neworiental Public Class ('新东方XDF微课堂')](http://weike.xdf.cn) and possibly others.

## What does it do?

Download `.m3u8` file's associated `.ts` files and join them into a `full.ts` file.

## How to use it?

One way to do it, is to start jupyter notebook and run all cell, it will then prompt you to input `.m3u8` URL, you can either input absolute path to your `.m3u8` file on your computer or the full URL link for `.m3u8` file on Internet. 
e.g. `http://cache.gensee.com/...omitted.../2018_04_24/Hn02H1YUyp_1524567489/hls/record.m3u8`

Then it will prompt you to input static part of the URL for `.ts` files on server (end with \'/\'), in most cases `.ts` files are in the same directory with `.m3u8` file, so inoput should be the same minus `.m3u8` part. 
e.g. `http://cache.gensee.com/...omitted.../2018_04_24/Hn02H1YUyp_1524567489/hls/`

**Lastly you need to input download path, if you use default path, enter 'default'. (my default download directory is `/Users/simonguo/Downloads/m3u8download`, you will need to change that in jupyter notebook). Or you can input you own preferable path.**

Once it starts downloading, you will see something like:

![example.png](https://github.com/sgyzetrov/m3u8_downloader4XDF/blob/master/example.png)

When download is complete there will be a `full.ts` file in download directory.

You can then rename `full.ts` to `**.mp4` (tested on mac 10.13.4, 10.13.5).

If you don't have jupyter notebook installed, well, one can always turn to good old fashion `.py` file.

Tested 07.16.2018 (mm/dd/yyyy), will work for videos on Zhihu.com, minor manual web sniffings required.

### How to download a video on Zhihu

Step1. pick your video

![zhihu_demo1.png](https://github.com/sgyzetrov/m3u8_downloader4XDF/blob/master/zhihu_demo1.png)

Step2. inspect elements to open video URL in new Tab

![zhihu_demo2.png](https://github.com/sgyzetrov/m3u8_downloader4XDF/blob/master/zhihu_demo2.png)

Step3. web sniffing to find the `.m3u8` link on Zhihu server

![zhihu_demo3.png](https://github.com/sgyzetrov/m3u8_downloader4XDF/blob/master/zhihu_demo3.png)

Step4. use the `.m3u8` link to download the video in m3u8_downloader4XDF

## Additional material

If you already downloaded `.ts` files on your own, and only need to join them into one `.ts` file, you can rename all `.ts` files into numeric order (e.g. `1.ts`, `2.ts`, ...), then modify number '716' in `join.sh` to the amount of `.ts` files in your own case and run `sh join.sh`. This shell script will help you join all `.ts` files into one `full.ts` file (tested on mac 10.13.4).

