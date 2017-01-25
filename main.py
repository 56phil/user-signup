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


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
    <head>
        <link rel='stylesheet' type='text/css' href='/static/user-signup.css'/>
        <title>Signup</title>
    </head>
    <body>
"""

# html boilerplate for the bottom of every page
page_footer = """
    </body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
PW_RE = re.compile(r"^.{3,20}$")

f_user_name = """
<div class="row">
<label for='user_name'>User Name:&nbsp;</label>
<input name='user_name' id='user_name' value=""/>
<span class="noerr">Not a valid user name</span>
</div>
"""

f_password = """
<br>
<div class="row">
<label for='password'>Password:&nbsp;</label>
<input name='password' id='password' type="password" value=""/>
<span class="noerr">Not a valid user password</span>
</div>
"""

f_verify_pw = """
<br>
<div class="row">
<label for='verify_pw'>Verify:&nbsp;</label>
<input name='verify_pw' id='verify_pw' type="password" value=""/>
<span class="noerr">Passwords don't match.</span>
</div>
"""

f_email = """
<br>
<div class="row">
<label for='email'>Email (Optonal):&nbsp;</label>
<input name='email' id='email' value=""/>
<span class="noerr">Not a valid user email</span>
</div>
"""

f_signup = """
<input name='signup' id='signup' type='submit' value='Signup'/>
"""


def is_valid_user_name(user):
    return USER_RE.match(user)


def is_valid_pw(pw):
    return PW_RE.match(pw)


def is_valid_email(email):
    if email:
        return EMAIL_RE.match(email)
    return True


class Validate(webapp2.RequestHandler):
    """ for requests comming in to root
    """
    def post(self):
        user_name = self.request.get("user_name")
        password = self.request.get("password")
        verify_pw = self.request.get("verify_pw")
        email = self.request.get("email")
        n_error = False

        content = page_header + """<h1>Sign Up</h1><div class="err_container"><form action="/sub" method="post">"""

        e_user_name = f_user_name
        if not is_valid_user_name(user_name):
            e_user_name = e_user_name.replace("noerr", "err")
            n_error = True
        t = 'value="{}"'.format(user_name)
        e_user_name = e_user_name.replace('value=""', t)
        content += e_user_name

        e_password = f_password
        if not is_valid_pw(password):
            e_password = e_password.replace("noerr", "err")
            n_error = True
        content += e_password

        e_verify_pw = f_verify_pw
        if not password == verify_pw:
            e_verify_pw = f_verify_pw.replace("noerr", "err")
            n_error = True
        content += e_verify_pw

        e_email = f_email
        if not is_valid_email(email):
            e_email = e_email.replace("noerr", "err")
            n_error = True
        t = 'value="{}"'.format(email)
        e_email = e_email.replace('value=""', t)
        content += e_email

        if n_error:
            self.response.write(content + f_signup + """</form></div>""" + page_footer)
        else:
            content = page_header + """<span class="welcome">Welcome """ + user_name + "</span>" + page_header
            self.response.write(content)


class MainHandler(webapp2.RequestHandler):
    """ for requests comming in to root
    """
    def get(self):
        content = page_header + """<h1>Sign Up</h1><div class="err_container"><form action="/sub" method="post">""" + \
                f_user_name + f_password + f_verify_pw + f_email +\
                f_signup + """</form></div>""" + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sub', Validate)
], debug=True)
