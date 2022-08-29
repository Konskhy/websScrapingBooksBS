import re

from locators.book_locator import BookLocator


class BookParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def title(self):
        locator = BookLocator.TITLE
        return self.parent.select_one(locator).attr['title']

    @property
    def rating(self):
        locator = BookLocator.RATING
        rating_classes = self.parent.select_one(locator).attr['class']
        rating = [x for x in rating_classes if x != 'star-rating'][0]
        return rating

    @property
    def price(self):
        locator = BookLocator.PRICE
        price_str = self.parent.select_one(locator).string
        pattern = "£([0-9]+\\.[0-9]+)"
        matcher = re.search(pattern, price_str)
        return float(matcher.group(1))

