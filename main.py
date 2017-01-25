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
    <link rel='stylesheet' type='text/css' href='/static/normalize.css'/>
    <link rel='stylesheet' type='text/css' href='/static/user-signup.css'/>
    <title>FlickList</title>
</head>
<body>
    <h1>Sign Up</h1><div class="container">
"""

# html boilerplate for the bottom of every page
page_footer = """
</div>
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    """ for requests comming in to root
    """
    def get(self):
        content = page_header + 'Hello world!' + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
