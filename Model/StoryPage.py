from google.appengine.ext import ndb


class StoryPageEntity(ndb.Model):
    """docstring for StoryStep"""

    story = ndb.TextProperty(required=True)
    #pageOfBook = ndb.IntegerProperty(required=True)

    nextPageOption1 = ndb.KeyProperty(kind="StoryPageEntity")
    nextPageOption1Description = ndb.StringProperty()

    nextPageOption2 = ndb.KeyProperty(kind="StoryPageEntity")
    nextPageOption2Description = ndb.StringProperty()



class StoryPage(object):
    """docstring for StoryPage"""
    def __init__(self, story, next1=None, description1="", next2=None, description2=""):
        if isinstance(story, StoryPageEntity):
            self._entity = story
        else:
            self._entity = StoryPageEntity(story=story, #pageOfBook=pageOfBook
                            nextPageOption1=next1, nextPageOption1Description=description1,
                            nextPageOption2=next2, nextPageOption2Description=description2)
        self.nextPageOption1 = self._entity.nextPageOption1
        self.nextPageOption2 = self._entity.nextPageOption2
        self.nextPageOption1Description = self._entity.nextPageOption1Description
        self.nextPageOption2Description = self._entity.nextPageOption2Description
        self.story = self._entity.story
        #self.pageOfBook = self._entity.pageOfBook


    #properties
    @property
    def nextPageOption1(self):
        return self._entity.nextPageOption1

    @property
    def nextPageOption2(self):
        return self._entity.nextPageOption2

    @property
    def nextPageOption1Description(self):
        return self._entity.nextPageOption1Description

    @property
    def nextPageOption2Description(self):
        return self._entity.nextPageOption2Description

    @property
    def story(self):
        return self._entity.story



    #properties setters
    @nextPageOption1.setter
    def nextPageOption1(self, value):
        """value must be an instance of StoryPage"""
        self._entity.nextPageOption1 = value


    @nextPageOption2.setter
    def nextPageOption2(self, value):
        self._entity.nextPageOption2 = value


    @nextPageOption1Description.setter
    def nextPageOption1Description(self, value):
        self._entity.nextPageOption1Description = value

    @nextPageOption2Description.setter
    def nextPageOption2Description(self, value):
        self._entity.nextPageOption2Description = value

    @story.setter
    def story(self, value):
        self._entity.story = value

    def key(self):
        return self._entity.key


    def store(self):
        self._entity.put()



    @staticmethod
    def getPageByKey(StoryPageEntityKey):
        return StoryPage(ndb.Key(urlsafe=StoryPageEntityKey.urlsafe()).get())

    @staticmethod
    def getPageByPageNumberOfBook(book, pageNumber):
        pass
