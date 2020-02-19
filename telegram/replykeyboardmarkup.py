#!/usr/bin/env python


import json
from .replymarkup import ReplyMarkup


class ReplyKeyboardMarkup(ReplyMarkup):
    def __init__(self,
                 keyboard,
                 resize_keyboard=None,
                 one_time_keyboard=None,
                 selective=None):
        """Args:
            keyboard:
                Array of array of strings representing the list buttons for each row

            resize_keyboard:
                Boolean Optional. Requests clients to resize the keyboard vertically for optimal fit
                (e.g., make the keyboard smaller if there are just two rows of buttons).
                Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.

            one_time_keyboard:
                Boolean	Optional. Requests clients to hide the keyboard as soon as it's been used. Defaults to false.

            selective:
            	Boolean	Optional. Use this parameter if you want to show the keyboard to specific users only. Targets:
                1) users that are @mentioned in the text of the Message object;
                2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.

                Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language.
                Other users in the group don't see the keyboard.

            """
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    @staticmethod
    def de_json(data):
        return ReplyKeyboardMarkup(keyboard=data.get('keyboard', None),
                                   resize_keyboard=data.get(
                                       'resize_keyboard', None
                                       ),
                                   one_time_keyboard=data.get(
                                       'one_time_keyboard', None
                                       ),
                                   selective=data.get('selective', None))

    def to_json(self):
        json_data = {'keyboard': self.keyboard}
        if self.resize_keyboard:
            json_data['resize_keyboard'] = self.resize_keyboard
        if self.one_time_keyboard:
            json_data['one_time_keyboard'] = self.one_time_keyboard
        if self.selective:
            json_data['selective'] = self.selective
        return json.dumps(json_data)
