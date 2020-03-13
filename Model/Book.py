from google.appengine.ext import ndb
from Model.StoryPage import StoryPage
from CustomExceptions import DuplicateEntryError, NotFoundError


class BookEntity(ndb.Model):
    """For Internal Use Only"""

    name = ndb.StringProperty(required=True)
    firstPage = ndb.KeyProperty(required=False)



class Book(object):
    """docstring for Book"""
    def __init__(self, name="", firstPage=None):
        if isinstance(name, BookEntity):
            self._entity = name
        else:
            if BookEntity.query(BookEntity.name == name).get() is not None:
                raise DuplicateEntryError("Book already exists")
            firstPageKey = firstPage.key() if firstPage is not None else None
            self._entity = BookEntity(name=name, firstPage= firstPageKey)
        self._name = self._entity.name
        self._firstPage = self._entity.firstPage


    #properties
    @property
    def name(self):
        return self._name

    @property
    def firstPage(self):
        return Models.StoryPage.getPageByKey(self._firstPage.key)

    @firstPage.setter
    def firstPage(self,value):
        self._firstPage =  value.key()

    @property
    def key(self):
        return self._entity.key

    def store(self):
        self._entity.put()

    @staticmethod
    def getBooks():
        query = BookEntity.query()
        #q.filter("userId =", userId)
        return [Book(book_entity) for book_entity in query] #Lista por comprension

    @staticmethod
    def getfirstPageOfBookByName(name):
        query = BookEntity.query(BookEntity.name == name)
        obtained_book = query.get()
        if obtained_book is None:
            raise NotFoundError
        return StoryPage.getPageByKey(obtained_book.firstPage)  # Lista por comprension
