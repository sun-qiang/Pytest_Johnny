#!/usr/bin/env python3

# -*- coding:utf-8 -*-
import os
import re
import pytest
import allure
from utils.logger import log
from utils.readConfig import ini
from pageObject.searchpage import SearchPage


@allure.feature("AdminTool_Select_All_CLients")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        search.get_url(ini.url)

    @allure.story("搜索selenium结果用例")
    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        log.info(result)
        assert result

    @allure.story("测试搜索候选用例")
    def test_002(self, drivers):
        """测试搜索候选"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        log.info(list(search.imagine))
        assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    #    pytest.main(['/Users/qiang.sun/PycharmProjects/AdminTool_Select_All_Clients/testCase/test_search.py'])
    pytest.main(['/Users/qiang.sun/PycharmProjects/AdminTool_Select_All_Clients/testCase/test_search.py', '--alluredir',
                 './allure'])
    os.system('allure serve allure')
