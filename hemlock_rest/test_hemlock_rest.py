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
import os

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

    def process_add_user_role(self):
        """
        Tests /add/user/(.*)/role/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_add_user_tenant(self):
        """
        Tests /add/user/(.*)/tenant/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_change_schedule_server(self):
        """
        Tests /change/schedule/(.*)/server/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_create_role(self):
        """
        Tests /create/role

        :return: returns any errors
        """
        error = []
        return error

    def process_create_schedule_server(self):
        """
        Tests /create/schedule_server

        :return: returns any errors
        """
        error = []
        return error

    def process_create_tenant(self):
        """
        Tests /create/tenant

        :return: returns any errors
        """
        error = []
        return error

    def process_create_user(self):
        """
        Tests /create/user

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

    def test_start_rest_server(self):
        """
        Starts the hemlock_rest server for testing purposes
        """

        cmd = "hemlock-rest &"
        os.system(cmd)

    def test_process_add_client_schedule(self):
        """
        Calls the test function for the add_client_schedule action.
        """
        error = self.process_add_client_schedule()
        for err in error:
            assert err == 0

    def test_process_add_schedule_client(self):
        """
        Calls the test function for the add_schedule_client action.
        """
        error = self.process_add_schedule_client()
        for err in error:
            assert err == 0

    def test_process_add_system_tenant(self):
        """
        Calls the test function for the add_system_tenant action.
        """
        error = self.process_add_system_tenant()
        for err in error:
            assert err == 0

    def test_process_add_user_role(self):
        """
        Calls the test function for the add_user_role action.
        """
        error = self.process_add_user_role()
        for err in error:
            assert err == 0

    def test_process_add_user_tenant(self):
        """
        Calls the test function for the add_user_tenant action.
        """
        error = self.process_add_user_tenant()
        for err in error:
            assert err == 0

    def test_process_change_schedule_server(self):
        """
        Calls the test function for the change_schedule_server action.
        """
        error = self.process_change_schedule_server()
        for err in error:
            assert err == 0

    def test_process_create_role(self):
        """
        Calls the test function for the create_role action.
        """
        error = self.process_create_role()
        for err in error:
            assert err == 0

    def test_process_create_schedule_server(self):
        """
        Calls the test function for the create_schedule_server action.
        """
        error = self.process_create_schedule_server()
        for err in error:
            assert err == 0

    def test_process_create_tenant(self):
        """
        Calls the test function for the create_tenant action.
        """
        error = self.process_create_tenant()
        for err in error:
            assert err == 0

    def test_process_create_user(self):
        """
        Calls the test function for the create_user action.
        """
        error = self.process_create_user()
        for err in error:
            assert err == 0

    def test_process_favicon(self):
        """
        Calls the test function for the favicon action.
        """
        error = self.process_favicon()
        for err in error:
            assert err == 0
