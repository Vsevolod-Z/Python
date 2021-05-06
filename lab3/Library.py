import Book


class Library(object):

    book_id = 0

    def __init__(self, number, address):
        self._number = number
        self._address = address
        self._collections = []
        Library.book_id = len(self._collections)

    def __iadd__(self, new_book):
        new_book._id = len(self._collections)
        self._collections += [new_book]
        return  self

    def __iter__(self):
        for book in self._collections:
            yield book