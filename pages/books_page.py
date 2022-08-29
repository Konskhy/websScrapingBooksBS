from bs4 import BeautifulSoup
from locators.books_page_locator import BooksPageLocator
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def book(self):
        locator = BooksPageLocator.BOOKS
        all_books = self.soup.select(locator)
        return [BookParser(b) for b in all_books]
