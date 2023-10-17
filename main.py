# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("https://www.baidu.com/")
#     print(page.title())
#     browser.close()


# import os
#
# base_dir = os.path.dirname(os.path.abspath(__file__))
# print(base_dir)


# import os
#
# directory = "D:\\code\\playwright_pom\\temps"
#
# if os.access(directory, os.W_OK):
#     print(f"You have write permission for directory: {directory}")
# else:
#     print(f"You do not have write permission for directory: {directory}")