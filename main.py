#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from Controller.MainPageController import MainPageController
from Controller.WebhookController import WebhookController
from Controller.MessageController import MessageController

from secrets import __TOKEN__




#matches the sub-urls to the correct Handler
app = webapp2.WSGIApplication([
    ('/', MainPageController),
    ('/webhook-'+__TOKEN__(), MessageController),
    ('/webhook-controller', WebhookController)
], debug=True)
