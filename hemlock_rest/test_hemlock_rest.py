#!/usr/bin/env python
#
#   Copyright (c) 2013 In-Q-Tel, Inc/Lab41, All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Test module for hemlock_rest.py

Created on 22 October 2013
@author: Charlie Lewis
"""

import hemlock_rest

class TestClass:
    """
    Test class for hemlock_rest.py
    """
    def process_add_client_schedule(self):
        """
        Tests /add/client/(.*)/schedule/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    spin up a webserver once, then use that to call the various tests
        #    this should not be called in this function, but is just a reminder

        # going to have to  rethink how this is called for using with travis
        #a = hemlock_rest.Hemlock_REST()
        error = []
        return error

    def process_add_schedule_client(self):
        """
        Tests /add/schedule/(.*)/client/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_add_system_tenant(self):
        """
        Tests /add/system/(.*)/tenant/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_favicon(self):
        """
        Tests /favicon.ico

        :return: returns any errors
        """
        error = []
        return error

    def test_process_add_client_schedule(self):
        """
        Calls the test function for the add_client_schedule action.
        """
        error = self.process_add_client_schedule()
        for err in error:
            assert err == 0
