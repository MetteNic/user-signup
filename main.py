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
import re
import cgi

class MainHandler(webapp2.RequestHandler):
    def get(self):
            form = """
            <form action="/submit" method="post">
                <label>
                    Username
                    <input type="text" name="username" value="{0}"/>
                </label>
                <span>{1}</span>
                <br>
                <label>
                    Password
                    <input type="password" name="password" value = ""/>
                </label>
                <span>{2}</span>
                <br>
                <label>
                    Verify Password
                    <input type="password" name="verify" value = ""/>
                </label>
                <span>{3}</span>
                <br>
                <label>
                    Email(optional)
                    <input type="text" name="email" value ="{4}" />
                </label>
                <span>{4}</span>
                <br>
                <input type="submit" value="Submit"/>
            </form>
            """
            blankForm = form.format("", "", "", "", "")

            self.response.write(blankForm)




class Welcome(webapp2.RequestHandler):



    def post(self):

        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

        username = self.request.get("username")
        if not USER_RE.match(username):
            error ="invalid username"
            self.redirect("/?error=" + error)


        content = "welcome " + username
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/submit', Welcome)
], debug=True)
