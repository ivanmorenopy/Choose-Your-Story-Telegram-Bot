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
