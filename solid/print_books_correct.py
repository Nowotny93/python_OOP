from abc import ABC, abstractmethod

class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content

class MobileFormatter(BaseFormatter):
    def format(self, book: Book):
        return book.content[:20]

class DesktopFormatter():
    def format(self, book: Book):
        return book.content[:100]


class Printer:
    def get_book(self, book: Book, formater: BaseFormatter):
        print('Print...')
        return formater.format(book)

printer = Printer()
book = Book('Hello there asdsf 12312453453456456456')
formatter = MobileFormatter()
desktop_formatter = DesktopFormatter()
print(printer.get_book(book, formatter))
print(printer.get_book(book, desktop_formatter))