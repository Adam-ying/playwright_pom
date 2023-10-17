import sys
import allure
import pytest
from playwright.sync_api import sync_playwright, Dialog
from page_object.search_page import SearchPage
from os.path import dirname, abspath
from utils.logger_util import info_log, error_log

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestSearch:

    def setup_method(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        info_log('=======================启动新页面=======================')
        self.page = self.browser.new_page()
        self.sp = SearchPage(self.page)

    def teardown_method(self):
        self.browser.close()
        self.playwright.stop()
        info_log('=======================关闭页面=======================')

    @allure.story('测试百度搜索')
    def test_baidu_search(self):
        try:
            info_log('=======================百度搜索开始=======================')
            self.sp.search(text='playwright')
            self.page.wait_for_selector('#\\31  > h3')
            assert self.page.title() == 'playwright_百度搜索'
        except AssertionError:
            error_log('=======================测试搜索失败=======================')
            raise
        info_log('=======================百度搜索结束=======================')

    @allure.story('测试百度设置栏')
    def test_save_setting(self):
        try:
            info_log('=======================百度设置开始=======================')
            self.sp.setting()
            def on_dialog(dialog: Dialog):
                assert dialog.type == 'alert'
                assert dialog.message == '已经记录下你的使用偏好'
                dialog.accept()

            self.page.on("dialog", on_dialog)

        except AssertionError:
            error_log('=======================百度设置出现问题=======================')
        info_log('=======================百度设置结束=======================')
    @allure.story('用于测试')
    def test_zzzz1(self):
        try:
            assert 2 + 1 == 4
        except AssertionError:
            error_log('=======================测试最后的错误=======================')

    @allure.story('用于最后')
    def test_zzzz2(self):
        try:
            assert 2 + 2 == 4
        except AssertionError:
            error_log('=======================测试最后的错误=======================')

if __name__ == '__main__':
    pytest.main(["-vs", "--alluredir", "D:\\code\\playwright_pom\\temps"])
