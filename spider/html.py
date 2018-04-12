#! python3
# coding=utf-8
__author__ = 'Duke'

import requests
import re


class HtmlSpider():
    def __init__(self, url):
        self.url = url
        self.headers = {'Accept-Encoding': 'gzip, deflate, br',
                        'connection': 'Keep-Alive',
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

    def find(self, key):
        data = self.reqHtmlContent()
        link_list = re.findall(key, data)
        for url in link_list:
            print (url)

    def reqHtmlContent(self):
        response = requests.get(self.url, headers=self.headers)
        return response.text


if __name__ == "__main__":
    pc = HtmlSpider('https://www.bilibili.com/video/av15845272/')
    pc.find(r"href='(http.*\.avi)'")
