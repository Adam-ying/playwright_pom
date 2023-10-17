import pytest
from utils.util import del_tmp_file
import os
from config.config import RunConfig
from utils.logger_util import info_log, error_log

@pytest.fixture(scope='session', autouse=True)
def generate_allure_report(request):
    del_tmp_file(path='temps')
    yield
    os.system(f'allure generate {RunConfig.BASE_DIR}\\temps -o {RunConfig.BASE_DIR}\\reports --clean')

@pytest.fixture(scope='session', autouse=True)
def logging_info():
    info_log("开始测试✨✨✨！")
    yield
    info_log("测试结束，生成测试报告💕 💕 💕 ！")