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

    def process_delete_role(self):
        """
        Tests /delete/role/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_delete_schedule_server(self):
        """
        Tests /delete/schedule_server/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_delete_schedule(self):
        """
        Tests /delete/schedule/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_delete_tenant(self):
        """
        Tests /delete/tenant/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_delete_user(self):
        """
        Tests /delete/user/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_deregister_local_system(self):
        """
        Tests /deregister/local-system/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_deregister_remote_system(self):
        """
        Tests /deregister/remote-system/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_get_client(self):
        """
        Tests /get/client/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_get_role(self):
        """
        Tests /get/role/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_get_schedule_server(self):
        """
        Tests /get/schedule_server/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_get_schedule(self):
        """
        Tests /get/schedule/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_get_system(self):
        """
        Tests /get/system/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_get_tenant(self):
        """
        Tests /get/tenant/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_get_user(self):
        """
        Tests /get/user/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_all(self):
        """
        Tests /list/all

        :return: returns any errors
        """
        error = []
        return error

    def process_list_clients(self):
        """
        Tests /list/clients

        :return: returns any errors
        """
        error = []
        return error

    def process_list_roles(self):
        """
        Tests /list/roles

        :return: returns any errors
        """
        error = []
        return error

    def process_list_schedule_servers(self):
        """
        Tests /list/schedule_servers

        :return: returns any errors
        """
        error = []
        return error

    def process_list_schedules(self):
        """
        Tests /list/schedules

        :return: returns any errors
        """
        error = []
        return error

    def process_list_systems(self):
        """
        Tests /list/systems

        :return: returns any errors
        """
        error = []
        return error

    def process_list_tenants(self):
        """
        Tests /list/tenants

        :return: returns any errors
        """
        error = []
        return error

    def process_list_users(self):
        """
        Tests /list/users

        :return: returns any errors
        """
        error = []
        return error

    def process_list_client_schedules(self):
        """
        Tests /list/client/schedules/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_client_systems(self):
        """
        Tests /list/client/systems/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_role_users(self):
        """
        Tests /list/role/users/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_schedule_clients(self):
        """
        Tests /list/schedule/clients/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_system_clients(self):
        """
        Tests /list/system/clients/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_system_tenants(self):
        """
        Tests /list/system/tenants/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_tenant_systems(self):
        """
        Tests /list/tenant/systems/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_tenant_users(self):
        """
        Tests /list/tenant/users/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_user_roles(self):
        """
        Tests /list/user/roles/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_list_user_tenants(self):
        """
        Tests /list/user/tenants/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_purge_client(self):
        """
        Tests /purge/client/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_query(self):
        """
        Tests /query

        :return: returns any errors
        """
        error = []
        return error

    def process_register_local_system(self):
        """
        Tests /register/local-system/

        :return: returns any errors
        """
        error = []
        return error

    def process_register_remote_system(self):
        """
        Tests /register/remote-system/

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

    def test_process_delete_role(self):
        """
        Calls the test function for the delete_role action.
        """
        error = self.process_delete_role()
        for err in error:
            assert err == 0

    def test_process_delete_schedule_server(self):
        """
        Calls the test function for the delete_schedule_server action.
        """
        error = self.process_delete_schedule_server()
        for err in error:
            assert err == 0

    def test_process_delete_schedule(self):
        """
        Calls the test function for the delete_schedule action.
        """
        error = self.process_delete_schedule()
        for err in error:
            assert err == 0

    def test_process_delete_tenant(self):
        """
        Calls the test function for the delete_tenant action.
        """
        error = self.process_delete_tenant()
        for err in error:
            assert err == 0

    def test_process_delete_user(self):
        """
        Calls the test function for the delete_user action.
        """
        error = self.process_delete_user()
        for err in error:
            assert err == 0

    def test_process_favicon(self):
        """
        Calls the test function for the favicon action.
        """
        error = self.process_favicon()
        for err in error:
            assert err == 0
