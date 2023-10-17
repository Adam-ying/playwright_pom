
class Base:
    def __init__(self, page):
        self.page = page

    def locator(self, loc):
        return self.page.locator(loc)

    def click(self, loc):
        self.locator(loc).click()

    def input(self, loc, text):
        self.locator(loc).fill(text)

    def hover(self, loc):
        self.locator(loc).hover()
