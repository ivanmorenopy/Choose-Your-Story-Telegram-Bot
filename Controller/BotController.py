import telegram
from threading import Lock, Thread
import webapp2



#from secrets import __TOKEN__
from SecretFolder.secrets import __TOKEN__


#No uso la clase singleton hasta que sepa como usarla correctamente
class Singleton(type):
	"""
	This is a thread-safe implementation of Singleton.
	"""

	_instance = None

	_lock = Lock()
	"""
	We now have a lock object that will be used to synchronize threads during
	first access to the Singleton.
	"""

	def __call__(cls, *args, **kwargs):
		# Now, imagine that the program has just been launched. Since there's no
		# Singleton instance yet, multiple threads can simultaneously pass the
		# previous conditional and reach this point almost at the same time. The
		# first of them will acquire lock and will proceed further, while the
		# rest will wait here.
		with cls._lock:
			# The first thread to acquire the lock, reaches this conditional,
			# goes inside and creates the Singleton instance. Once it leaves the
			# lock block, a thread that might have been waiting for the lock
			# release may then enter this section. But since the Singleton field
			# is already initialized, the thread won't create a new object.
			if not cls._instance:
				cls._instance = super().__call__(*args, **kwargs)
			return cls._instance


class BotController(webapp2.RequestHandler):
	#__metaclass__ = Singleton

	_instance = None    
	_lock = Lock()
	__MYBOT__ = None

	def __new__(cls):
		if BotController._instance is None:
			with BotController._lock:
				if BotController._instance is None:
					BotController._instance = super(BotController, cls).__new__(cls)
					BotController.__MYBOT__ = telegram.Bot(__TOKEN__())
		return BotController._instance



	def getUpdates(self,
					offset=None,
					limit=100,
					timeout=0):
		updates = None	
		try:
			updates = BotController.__MYBOT__.getUpdates(offset,limit,timeout)
		except TelegramError:
			updates = None
		finally:
			return updates



	def getWebhook(self):
		return BotController.__MYBOT__.getWebhook()

	def setWebhook(self, webhook_url):
		return BotController.__MYBOT__.setWebhook(webhook_url)

	def sendMessage(self,
                    chat_id,
                    text,
                    disable_web_page_preview=None,
                    reply_to_message_id=None,
                    reply_markup=None):        
        	return BotController.__MYBOT__.sendMessage(chat_id,
        												text,disable_web_page_preview,
        												reply_to_message_id,
        												reply_markup)