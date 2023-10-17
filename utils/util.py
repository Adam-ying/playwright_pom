import os
from config.config import RunConfig


def del_tmp_file(path):
    base = RunConfig.BASE_DIR
    root_path = f'{base}\\{path}'
    file_list = os.listdir(root_path)
    for file in file_list:
        file_path = f'{root_path}\\{file}'
        os.remove(file_path)

