
class DuplicateEntryError(Exception):
    """Raised when an entry already exists on the db"""
    pass

class NotFoundError(Exception):
    """Raised when a search finds no result"""
    pass