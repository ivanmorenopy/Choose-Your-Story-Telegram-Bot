import webapp2
#import os
import telegram
from google.appengine.ext.webapp.template import render
from Controller.BotController import BotController



class MainPageController(webapp2.RequestHandler):
	def get(self):
			__MYBOT__ = BotController()
			templateValues = {
				'updates': __MYBOT__.getUpdates(timeout=0) if __MYBOT__.getWebhook() == "" else None,
				'webhook_url': __MYBOT__.getWebhook()
			}
			mainPageTemplate = 'View/MainPage.html'
			self.response.write(render(mainPageTemplate, templateValues))

		##############################################################################
		# try:
		#	 updates = __MYBOT__.getUpdates(timeout=30)
		#	 for update in updates:
		#		 self.response.write("<p> UpdateId:"+ update.update_id.__str__() +" <strong>" + update.message.from_user.name + "</strong>: "+ update.message.text)

		# except telegram.error.TelegramError, e:
		#	 self.response.write(str(e))
		# except HTTPException:
		#	 # I've found this case happens when you try to
		#	 # use getUpdates() but the bot has a webhook url setted
		#	 # or when there are no updates
		#	 pass
		# self.response.write("<p> remote address " + str(self.request.remote_addr))
		# self.response.write("<p> webhook_url: " + __MYBOT__.getWebhook())