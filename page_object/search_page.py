from base.base_page import Base
from utils.logger_util import info_log, error_log


class SearchPage(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = 'https://www.baidu.com'
        self.el_input = '#kw'
        self.el_button = '#su'
        self.setting_button = '#s-usersetting-top'
        self.search_setting = '#s-user-setting-menu > div > a.setpref.first > span'
        self.save_setting_button = '#se-setting-7 > a.prefpanelgo.setting-btn.c-btn.c-btn-primary'

    def search(self, text):
        self.page.goto(self.url, timeout=60000)
        self.input(self.el_input, text)
        self.click(self.el_button)

    def setting(self):
        self.page.goto(self.url, timeout=60000)
        self.hover(self.setting_button)
        self.page.wait_for_selector(self.search_setting, timeout=60000)
        self.click(self.search_setting)
        self.click(self.save_setting_button)



