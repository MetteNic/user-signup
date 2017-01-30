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

form = """
<form  method="post">
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
    <span>{5}</span>
    <br>
    <input type="submit" value="Submit"/>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
            blankForm = form.format("", "", "", "", "", "")
            self.response.write(blankForm)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        user_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        PASS_RE = re.compile("^.{3,20}$")
        EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
        is_there_error = False

        if not USER_RE.match(username):
            user_error = "That is not a valid username"
            is_there_error = True

        if not PASS_RE.match(password):
            password_error = "That is not a valid password"
            is_there_error = True

        if not password == verify:
            verify_error = "Passwords don't match"
            is_there_error = True

        if email:
            if not EMAIL_RE.match(email):
                email_error = "That's not a valid email"
                is_there_error = True

        submitted_form = form.format(username, user_error, password_error, verify_error, email, email_error)

        if is_there_error == True:
            self.response.write(submitted_form)

        else:
            self.redirect("/welcome?username=" + username)






class Welcome(webapp2.RequestHandler):

    def get(self):
        username = self.request.get("username")
        content = "Welcome " + username
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
