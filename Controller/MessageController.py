import webapp2
import json
from BotController import BotController
from telegram import Update
from telegram import TelegramError
from Model.StoryPage import StoryPage
from Model.UserState import UserState
from Model.Book import Book

__MYBOT__ =  BotController()

def getUpdateFromWebhookRequestBody(data):
    """Creates an Update object from the data sent from telegram server
        Args:
            update:
                the body of the telegram request

        Returns:
            Update object if the data sent was ok
            None object if it couldn't be created
    """
    updateJson = str(data)
    try:
        if updateJson != "":
            updateDictionary = json.loads(updateJson)
            return Update.de_json(updateDictionary)
    except:
        return None

class MessageController(webapp2.RequestHandler):
    """Process mesages sent by users"""
    def post(self):
        update = getUpdateFromWebhookRequestBody(self.request.body)
        if update is None:
            pass
            
        text = update.message.text
        if text.startswith("/start"):
            #pressent book list
            __MYBOT__.sendMessage(update.message.chat.id, "Bienvenido a la bibioteca de libros colaborativos...")
            __MYBOT__.sendMessage(update.message.chat.id, "Aqui tienes una lista de nuestra coleccion")

            book_list = Book .getBooks()
            lista = "\n".join([b.text for b in book_list])
            __MYBOT__.sendMessage(update.message.chat.id, "1.libro 1")#str(lista))

            UserState(update.message.from_user.id, "Iniciated").store()

        elif text.startswith("/read"):
            if text[5] == " ":
                #check book
                    #get initial page of book
                pass

        elif text.startswith("/new-book"):
            UserState(update.message.from_user.id, "Creating-New-Book").store()

            __MYBOT__.sendMessage(update.message.chat.id, "Dime el nombre de tu libro")

        elif text.startswith("/getMessage"):
            #pass
            retreivedMsg = "..."#str(UserMessage.getMessageByKey(text[8:]))
            __MYBOT__.sendMessage(update.message.chat.id, retreivedMsg)


        #elif not text.startswith("\/"):
        #    #check what the request is
        #    pass

        else:
            user_state = UserState.getStateByUserId(update.message.from_user.id)

            if user_state.state == "Creating-New-Book":
                new_book = Book(text)
                first_page = StoryPage("..TBD..")
                new_book.firstPage = first_page.key()
                new_book.store()
                __MYBOT__.sendMessage(update.message.chat.id, "Libro creado. A continuacion escriba la primer pagina")
                UserState(update.message.from_user.id, "Writing-Page", first_page.key()).store()

            elif user_state.state == "Writing-Page":
                page = StoryPage.getPageByKey(user_state.value)
                page.story = text
                page.store()
                UserState(update.message.from_user.id, "Page-Writen", page.key()).store()
                __MYBOT__.sendMessage(update.message.chat.id, "Pagina creada")



                

    def EcoUpdateMessage(update):
        """Answer back the same message the user sent
            Args
                update
                    Update object containing all the information
        """
        __MYBOT__.sendMessage(update.message.chat.id,update.message.text, reply_to_message_id=update.message.message_id)
