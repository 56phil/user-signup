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


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
    <head>
        <link rel='stylesheet' type='text/css' href='/static/user-signup.css'/>
        <title>Signup</title>
    </head>
    <body>
        <h1>Sign Up</h1>
        <div class="container">
            <form>
"""

# html boilerplate for the bottom of every page
page_footer = """
            </form>
        </div>
    </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    """ for requests comming in to root
    """
    def get(self):
        user_name = """
        <label for='user_name'>User Name:&nbsp;
        </label>
        <input name='user_name' id='user_name' />
        <br>
        """

        password = """
        <label for='password'>Password:&nbsp;
        </label>
        <input name='password' id='password' />
        <br>
        """

        verify_pw = """
        <label for='verify_pw'>Verify:&nbsp;
        </label>
        <input name='verify_pw' id='verify_pw' />
        <br>
        """

        email = """
        <label for='email'>Email (Optonal):&nbsp;
        </label>
        <input name='email' id='email' />
        <br>
        """

        signup = """
        <input name='signup' id='signup' type='submit' value='Signup'/>
        """
        content = page_header + user_name + password + verify_pw + email +\
        signup + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
