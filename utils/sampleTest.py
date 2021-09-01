#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver


def login():
    driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")

    driver.delete_all_cookies()
    driver.get('https://www.baidu.com/')


if __name__ == '__main__':
    login()
