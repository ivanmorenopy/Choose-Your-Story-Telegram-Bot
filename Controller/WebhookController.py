import webapp2
from BotController import BotController
import os

from secrets import (__TOKEN__,
                    __DEV_URL__,
                    __PROD_URL__,
                    __SERVER_TYPE__)

class WebhookController(webapp2.RequestHandler):
    def get(self):
        """Manages webhook status

            If request has  variable newstatus as 'start' it enables the service
            If request has  variable newstatus as 'stop' or any other it disables the service
        """
        __MYBOT__ = BotController()
        

        if self.request.get("request") == "changestatus":
            newStatus = self.request.get("newstatus")
            if newStatus == "start":
                serverURL = __DEV_URL__ if __SERVER_TYPE__ == "Dev" else __PROD_URL__
                __MYBOT__.setWebhook(serverURL + "/webhook-"+__TOKEN__)
                self.response.write("started")
            elif newStatus == "stop":
                __MYBOT__.setWebhook("")
                self.response.write("stoped")
        if self.request.get("request") == "url":
            webhookUrl = __MYBOT__.getWebhook()
            self.response.write(webhookUrl if webhookUrl != '' else ' NOT using webhook')