# m3u8_downloader4XDF

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![Python 2.7](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/)

`.m3u8` video downloader used to download free class on [Neworiental Public Class ('新东方XDF微课堂')](http://weike.xdf.cn) 

## What does it do?

Download `.m3u8` file's associated `.ts` files and join them into a `full.ts` file.

## How to use it?

Start jupyter notebook and run all cell, it will then prompt you to input `.m3u8` URL, you can either input absolute path on computer or full URL link on Internet. e.g. `http://cache.gensee.com/...omitted.../2018_04_24/Hn02H1YUyp_1524567489/hls/record.m3u8`

Then it will prompt you to input static part of the URL for `.ts` files on server (end with \'/\'), in most cases `.ts` files are in the case directory with `.m3u8` file, so inoput should be the same minus `.m3u8` part. e.g. `http://cache.gensee.com/...omitted.../2018_04_24/Hn02H1YUyp_1524567489/hls/`

**Lastly you need to input download path, if you use default path, enter 'default'. (my default download directory is `/Users/simonguo/Downloads/m3u8download`, you will need to change that in jupyter notebook). Or you can input you own preferable path.**

Once it starts downloading, you will see something like:

![example.png](https://github.com/sgyzetrov/m3u8_downloader4XDF/blob/master/example.png)

When download is complete there will be a `full.ts` file in download directory.

You can then rename `full.ts` to `**.mp4` (tested on mac 10.13.4).

