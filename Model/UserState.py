from google.appengine.ext import ndb


class UserStateEntity(ndb.Model):
    """docstring for StoryStep"""

    userId = ndb.IntegerProperty(required=True)
    state = ndb.StringProperty(required=True)
    value = ndb.KeyProperty(required=False)
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

    # nextPageOption2 = db.SelfReferenceProperty(collection_name="second_reference_set")
    # nextPageOption2Description = db.StringProperty()


class UserState(object):
    """docstring for StoryPage"""
    def __init__(self, userId, state="", value=None):
        if isinstance(userId, UserStateEntity):
            self._entity = userId
        else:
            self._entity = UserStateEntity(userId=userId, state=state, value=value)

        self._id = None
        self._userId = self._entity.userId
        self._state = self._entity.state
        self._value = self._entity.value

    #properties
    @property
    def userId(self):
        return self._userId

    @property
    def state(self):
        return self._state

    @property
    def value(self):
        return self._value




    @state.setter
    def state(self, val):
        self._state = val

    @value.setter
    def value(self, val):
        self._value = val


    def store(self):
        self._entity.put()
        #return self._entity.key().id()

    def getKeyId(self):
        return self._entity.key()

    @staticmethod
    def getMessageByKey(key):
        #return UserMessage(db.get(key))
        q = UserMessageEntity.all()
        q.filter("ID =", key)
        UserMessage(ndb.get(q.get())) #Lista por comprension


    @staticmethod
    def getStateByUserId(userId):
        query = UserStateEntity.query(UserStateEntity.userId == userId).order(-UserStateEntity.timestamp)
        #q.filter("userId =", userId)
        return UserState(query.get())
        #return [UserState(user_state_entity) for user_state_entity in query] #Lista por comprension
