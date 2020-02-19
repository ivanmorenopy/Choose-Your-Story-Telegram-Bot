from google.appengine.ext import ndb


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
            self._entity = BookEntity(name=name, firstPage=firstPage._entity.key)
        self._name = self._entity.name
        self._firstPage = self._entity.firstPage


    #properties
    @property
    def name(self):
        return self._name

    @property
    def firstPage(self):
        return Models.StoryPage.getPageByKey(self._firstPage.key)

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
