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
import shlex
import subprocess

class TestClass():
    def process_root(self):
        """
        Tests /

        :return: returns any errors
        """
        error = []
        return error

    def process_version(self):
        """
        Tests /version

        :return: returns any errors
        """
        error = []
        return error

    def process_add_client_schedule(self):
        """
        Tests /add/client/(.*)/schedule/(.*)

        :return: returns any errors
        """
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
        # !! TODO
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/create/role")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_create_schedule_server(self):
        """
        Tests /create/schedule_server

        :return: returns any errors
        """
        # !! TODO
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/create/schedule_server")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_create_tenant(self):
        """
        Tests /create/tenant

        :return: returns any errors
        """
        # !! TODO
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/create/tenant")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_create_user(self):
        """
        Tests /create/user

        :return: returns any errors
        """
        # !! TODO
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/create/user")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_delete_role(self):
        """
        Tests /delete/role/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a role first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/delete/role/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_delete_schedule_server(self):
        """
        Tests /delete/schedule_server/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a schedule_server first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/delete/schedule_server/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_delete_schedule(self):
        """
        Tests /delete/schedule/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a schedule first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/delete/schedule/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_delete_tenant(self):
        """
        Tests /delete/tenant/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a tenant first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/delete/tenant/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_delete_user(self):
        """
        Tests /delete/user/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a user first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/delete/user/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_deregister_local_system(self):
        """
        Tests /deregister/local-system/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    register a local system first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/deregister/local-system/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_deregister_remote_system(self):
        """
        Tests /deregister/remote-system/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    register a remote system first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/deregister/remote-system/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_get_client(self):
        """
        Tests /get/client/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a client first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/get/client/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_get_role(self):
        """
        Tests /get/role/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a role first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/get/role/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_get_schedule_server(self):
        """
        Tests /get/schedule_server/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a schedule_server first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/get/schedule_server/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_get_schedule(self):
        """
        Tests /get/schedule/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a schedule first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/get/schedule/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_get_system(self):
        """
        Tests /get/system/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a system first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/get/system/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_get_tenant(self):
        """
        Tests /get/tenant/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a tenant first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/get/tenant/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_get_user(self):
        """
        Tests /get/user/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a user first
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/get/user/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_all(self):
        """
        Tests /list/all

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/all")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_clients(self):
        """
        Tests /list/clients

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/clients")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_roles(self):
        """
        Tests /list/roles

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/roles")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_schedule_servers(self):
        """
        Tests /list/schedule_servers

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/schedule_servers")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_schedules(self):
        """
        Tests /list/schedules

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/schedules")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_systems(self):
        """
        Tests /list/systems

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/systems")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_tenants(self):
        """
        Tests /list/tenants

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/tenants")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_users(self):
        """
        Tests /list/users

        :return: returns any errors
        """
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/users")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_client_schedules(self):
        """
        Tests /list/client/schedules/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a client
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/client/schedules/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_client_systems(self):
        """
        Tests /list/client/systems/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a client
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/client/systems/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_role_users(self):
        """
        Tests /list/role/users/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a role
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/role/users/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_schedule_clients(self):
        """
        Tests /list/schedule/clients/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a schedule
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/schedule/clients/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_system_clients(self):
        """
        Tests /list/system/clients/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a system
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/system/clients/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_system_tenants(self):
        """
        Tests /list/system/tenants/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a system
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/system/tenants/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_tenant_systems(self):
        """
        Tests /list/tenant/systems/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a tenant
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/tenant/systems/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_tenant_users(self):
        """
        Tests /list/tenant/users/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a tenant
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/tenant/users/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_user_roles(self):
        """
        Tests /list/user/roles/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a user
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/user/roles/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

    def process_list_user_tenants(self):
        """
        Tests /list/user/tenants/(.*)

        :return: returns any errors
        """
        # !! TODO
        #    create a user
        cmd = shlex.split("/usr/bin/curl http://localhost:8080/list/user/tenants/asdf")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        error = []
        if err:
            error.append(err)
        return error, out

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

    def process_remove_client_schedule(self):
        """
        Tests /remove/client/(.*)/schedule/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_remove_schedule_client(self):
        """
        Tests /remove/schedule/(.*)/client/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_remove_system_tenant(self):
        """
        Tests /remove/system/(.*)/tenant/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_remove_user_role(self):
        """
        Tests /remove/user/(.*)/role/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_remove_user_tenant(self):
        """
        Tests /remove/user/(.*)/tenant/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_run_client(self):
        """
        Tests /run/client/(.*)/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_schedule_client(self):
        """
        Tests /schedule/client

        :return: returns any errors
        """
        error = []
        return error

    def process_start_scheduler(self):
        """
        Tests /start/scheduler/(.*)

        :return: returns any errors
        """
        error = []
        return error

    def process_store_client(self):
        """
        Tests /store/client

        :return: returns any errors
        """
        error = []
        return error

    def process_store_hemlock_server(self):
        """
        Tests /store/hemlock-server

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

    def test_instantiate(self):
        """
        Tests instantiate instances of api functions
        """
        a = hemlock_rest.Hemlock_REST().__new__(hemlock_rest.Hemlock_REST)
        a.setup()
        a = hemlock_rest.root()
        a.GET()
        a = hemlock_rest.version()
        a.GET()
        a = hemlock_rest.favicon()
        # !! TODO
        # hardcoded filename is causing this to fail
        #a.GET()
        a = hemlock_rest.start()
        a.GET()
        a = hemlock_rest.query()
        a.POST()
        a = hemlock_rest.fields()
        a.GET()
        a = hemlock_rest.add()
        a.GET("first", "second")
        a = hemlock_rest.change()
        a.GET("first", "second")
        a = hemlock_rest.create()
        a.fullpath = "role"
        a.data = "{'name':'foo'}"
        a.POST()
        a.fullpath = "schedule_server"
        a.data = "{'name':'foo'}"
        a.POST()
        a.fullpath = "tenant"
        a.data = "{'name':'foo'}"
        a.POST()
        a.fullpath = "schedule"
        a.data = "{'name':'foo', 'minute':'1', 'hour':'1', 'day_of_month':'1', 'month':'1', 'day_of_week':'1', 'client_id':'asdf'}"
        a.POST()
        a.fullpath = "client"
        a.data = "{'name':'foo', 'type':'asdf', 'system_id':'asdf', 'credential_file':'asdf'}"
        a.POST()
        a.fullpath = "hemlock-server"
        a.data = "{'credential_file':'foo'}"
        a.POST()
        a.fullpath = "user"
        a.data = "{'name':'foo', 'username':'asdf', 'email':'asdf', 'role_id':'asdf', 'tenant_id':'asdf'}"
        a.POST()
        a = hemlock_rest.delete()
        a.fullpath = "role"
        a.GET("uuid")
        a.fullpath = "schedule_server"
        a.GET("uuid")
        a.fullpath = "system"
        a.GET("uuid")
        a.fullpath = "user"
        a.GET("uuid")
        a.fullpath = "tenant"
        a.GET("uuid")
        a.fullpath = "schedule"
        a.GET("uuid")
        a.fullpath = "client"
        a.GET("uuid")
        a = hemlock_rest.deregister()
        a.fullpath = "local"
        a.GET("uuid")
        a.fullpath = "remote"
        a.GET("uuid")
        a = hemlock_rest.get()
        a.fullpath = "role"
        a.GET("uuid")
        a.fullpath = "schedule_server"
        a.GET("uuid")
        a.fullpath = "system"
        a.GET("uuid")
        a.fullpath = "tenant"
        a.GET("uuid")
        a.fullpath = "user"
        a.GET("uuid")
        a.fullpath = "client"
        a.GET("uuid")
        a.fullpath = "schedule"
        a.GET("uuid")
        a = hemlock_rest.list1()
        a.fullpath = "roles"
        a.GET()
        a.fullpath = "schedule_server"
        a.GET()
        a.fullpath = "systems"
        a.GET()
        a.fullpath = "tenants"
        a.GET()
        a.fullpath = "users"
        a.GET()
        a.fullpath = "clients"
        a.GET()
        a.fullpath = "schedules"
        a.GET()
        a.fullpath = "all"
        a.GET()
        a = hemlock_rest.list2()
        a.fullpath = "system tenants"
        a.GET("uuid")
        a.fullpath = "systems tenant"
        a.GET("uuid")
        a.fullpath = "users tenant"
        a.GET("uuid")
        a.fullpath = "user tenants"
        a.GET("uuid")
        a.fullpath = "user roles"
        a.GET("uuid")
        a.fullpath = "users role"
        a.GET("uuid")
        a.fullpath = "client schedules"
        a.GET("uuid")
        a.fullpath = "clients schedule"
        a.GET("uuid")
        a.fullpath = "client systems"
        a.GET("uuid")
        a.fullpath = "clients system"
        a.GET("uuid")
        a = hemlock_rest.register()
        a.fullpath = "local"
        a.data = "{'name':'foo', 'data_type':'asdf', 'description':'asdf', 'tenant_id':'asdf', 'hostname':'asdf', 'endpoint':'asdf', 'poc_name':'asdf', 'poc_email':'asdf'}"
        a.POST()
        a.fullpath = "remote"
        a.data = "{'name':'foo', 'data_type':'asdf', 'description':'asdf', 'tenant_id':'asdf', 'hostname':'asdf', 'port':'asdf', 'remote_uri':'asdf', 'poc_name':'asdf', 'poc_email':'asdf'}"
        a.POST()
        a = hemlock_rest.remove()
        a.fullpath = "roles"
        a.GET("first", "second")
        a.fullpath = "system"
        a.GET("first", "second")
        a.fullpath = "user"
        a.GET("first", "second")
        a.fullpath = "remove/client"
        a.GET("first", "second")
        a.fullpath = "remove/schedule"
        a.GET("first", "second")
        a = hemlock_rest.run()
        a.GET("first", "second")

    def test_start_rest_server(self):
        """
        Starts the hemlock_rest server for testing purposes
        """
        cmd = "hemlock-rest &"
        os.system(cmd)

    def test_process_root(self):
        """
        Calls the test function for the root action.
        """
        error = self.process_root()
        for err in error:
            assert err == 0

    def test_process_version(self):
        """
        Calls the test function for the version action.
        """
        error = self.process_version()
        for err in error:
            assert err == 0

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
        error, out = self.process_create_role()
        for err in error:
            assert err == 0

    def test_process_create_schedule_server(self):
        """
        Calls the test function for the create_schedule_server action.
        """
        error, out = self.process_create_schedule_server()
        for err in error:
            assert err == 0

    def test_process_create_tenant(self):
        """
        Calls the test function for the create_tenant action.
        """
        error, out = self.process_create_tenant()
        for err in error:
            assert err == 0

    def test_process_create_user(self):
        """
        Calls the test function for the create_user action.
        """
        error, out = self.process_create_user()
        for err in error:
            assert err == 0

    def test_process_delete_role(self):
        """
        Calls the test function for the delete_role action.
        """
        error, out = self.process_delete_role()
        for err in error:
            assert err == 0

    def test_process_delete_schedule_server(self):
        """
        Calls the test function for the delete_schedule_server action.
        """
        error, out = self.process_delete_schedule_server()
        for err in error:
            assert err == 0

    def test_process_delete_schedule(self):
        """
        Calls the test function for the delete_schedule action.
        """
        error, out = self.process_delete_schedule()
        for err in error:
            assert err == 0

    def test_process_delete_tenant(self):
        """
        Calls the test function for the delete_tenant action.
        """
        error, out = self.process_delete_tenant()
        for err in error:
            assert err == 0

    def test_process_delete_user(self):
        """
        Calls the test function for the delete_user action.
        """
        error, out = self.process_delete_user()
        for err in error:
            assert err == 0

    def test_process_deregister_local_system(self):
        """
        Calls the test function for the deregister_local_system action.
        """
        error, out = self.process_deregister_local_system()
        for err in error:
            assert err == 0

    def test_process_deregister_remote_system(self):
        """
        Calls the test function for the deregister_remote_system action.
        """
        error, out = self.process_deregister_remote_system()
        for err in error:
            assert err == 0

    def test_process_get_client(self):
        """
        Calls the test function for the get_client action.
        """
        error, out = self.process_get_client()
        for err in error:
            assert err == 0

    def test_process_get_role(self):
        """
        Calls the test function for the get_role action.
        """
        error, out = self.process_get_role()
        for err in error:
            assert err == 0

    def test_process_get_schedule_server(self):
        """
        Calls the test function for the get_schedule_server action.
        """
        error, out = self.process_get_schedule_server()
        for err in error:
            assert err == 0

    def test_process_get_schedule(self):
        """
        Calls the test function for the get_schedule action.
        """
        error, out = self.process_get_schedule()
        for err in error:
            assert err == 0

    def test_process_get_system(self):
        """
        Calls the test function for the get_system action.
        """
        error, out = self.process_get_system()
        for err in error:
            assert err == 0

    def test_process_get_tenant(self):
        """
        Calls the test function for the get_tenant action.
        """
        error, out = self.process_get_tenant()
        for err in error:
            assert err == 0

    def test_process_get_user(self):
        """
        Calls the test function for the get_user action.
        """
        error, out = self.process_get_user()
        for err in error:
            assert err == 0

    def test_process_list_all(self):
        """
        Calls the test function for the list_all action.
        """
        error, out = self.process_list_all()
        for err in error:
            assert err == 0

    def test_process_list_clients(self):
        """
        Calls the test function for the list_clients action.
        """
        error, out = self.process_list_clients()
        for err in error:
            assert err == 0

    def test_process_list_roles(self):
        """
        Calls the test function for the list_roles action.
        """
        error, out = self.process_list_roles()
        for err in error:
            assert err == 0

    def test_process_list_schedule_servers(self):
        """
        Calls the test function for the list_schedule_servers action.
        """
        error, out = self.process_list_schedule_servers()
        for err in error:
            assert err == 0

    def test_process_list_schedules(self):
        """
        Calls the test function for the list_schedules action.
        """
        error, out = self.process_list_schedules()
        for err in error:
            assert err == 0

    def test_process_list_systems(self):
        """
        Calls the test function for the list_systems action.
        """
        error, out = self.process_list_systems()
        for err in error:
            assert err == 0

    def test_process_list_tenants(self):
        """
        Calls the test function for the list_tenants action.
        """
        error, out = self.process_list_tenants()
        for err in error:
            assert err == 0

    def test_process_list_users(self):
        """
        Calls the test function for the list_users action.
        """
        error, out = self.process_list_users()
        for err in error:
            assert err == 0

    def test_process_list_client_schedules(self):
        """
        Calls the test function for the list_client_schedules action.
        """
        error, out = self.process_list_client_schedules()
        for err in error:
            assert err == 0

    def test_process_list_client_systems(self):
        """
        Calls the test function for the list_client_systems action.
        """
        error, out = self.process_list_client_systems()
        for err in error:
            assert err == 0

    def test_process_list_role_users(self):
        """
        Calls the test function for the list_role_users action.
        """
        error, out = self.process_list_role_users()
        for err in error:
            assert err == 0

    def test_process_list_schedule_clients(self):
        """
        Calls the test function for the list_schedule_clients action.
        """
        error, out = self.process_list_schedule_clients()
        for err in error:
            assert err == 0

    def test_process_list_system_clients(self):
        """
        Calls the test function for the list_system_clients action.
        """
        error, out = self.process_list_system_clients()
        for err in error:
            assert err == 0

    def test_process_list_system_tenants(self):
        """
        Calls the test function for the list_system_tenants action.
        """
        error, out = self.process_list_system_tenants()
        for err in error:
            assert err == 0

    def test_process_list_tenant_systems(self):
        """
        Calls the test function for the list_tenant_systems action.
        """
        error, out = self.process_list_tenant_systems()
        for err in error:
            assert err == 0

    def test_process_list_tenant_users(self):
        """
        Calls the test function for the list_tenant_users action.
        """
        error, out = self.process_list_tenant_users()
        for err in error:
            assert err == 0

    def test_process_list_user_roles(self):
        """
        Calls the test function for the list_user_roles action.
        """
        error, out = self.process_list_user_roles()
        for err in error:
            assert err == 0

    def test_process_list_user_tenants(self):
        """
        Calls the test function for the list_user_tenants action.
        """
        error, out = self.process_list_user_tenants()
        for err in error:
            assert err == 0

    def test_process_purge_client(self):
        """
        Calls the test function for the purge_client action.
        """
        error = self.process_purge_client()
        for err in error:
            assert err == 0

    def test_process_query(self):
        """
        Calls the test function for the query action.
        """
        error = self.process_query()
        for err in error:
            assert err == 0

    def test_process_register_local_system(self):
        """
        Calls the test function for the register_local_system action.
        """
        error = self.process_register_local_system()
        for err in error:
            assert err == 0

    def test_process_register_remote_system(self):
        """
        Calls the test function for the register_remote_system action.
        """
        error = self.process_register_remote_system()
        for err in error:
            assert err == 0

    def test_process_remove_client_schedule(self):
        """
        Calls the test function for the remove_client_schedule action.
        """
        error = self.process_remove_client_schedule()
        for err in error:
            assert err == 0

    def test_process_remove_schedule_client(self):
        """
        Calls the test function for the remove_schedule_client action.
        """
        error = self.process_remove_schedule_client()
        for err in error:
            assert err == 0

    def test_process_remove_system_tenant(self):
        """
        Calls the test function for the remove_system_tenant action.
        """
        error = self.process_remove_system_tenant()
        for err in error:
            assert err == 0

    def test_process_remove_user_role(self):
        """
        Calls the test function for the remove_user_role action.
        """
        error = self.process_remove_user_role()
        for err in error:
            assert err == 0

    def test_process_remove_user_tenant(self):
        """
        Calls the test function for the remove_user_tenant action.
        """
        error = self.process_remove_user_tenant()
        for err in error:
            assert err == 0

    def test_process_run_client(self):
        """
        Calls the test function for the run_client action.
        """
        error = self.process_run_client()
        for err in error:
            assert err == 0

    def test_process_schedule_client(self):
        """
        Calls the test function for the schedule_client action.
        """
        error = self.process_schedule_client()
        for err in error:
            assert err == 0

    def test_process_start_scheduler(self):
        """
        Calls the test function for the start_scheduler action.
        """
        error = self.process_start_scheduler()
        for err in error:
            assert err == 0

    def test_process_store_client(self):
        """
        Calls the test function for the store_client action.
        """
        error = self.process_store_client()
        for err in error:
            assert err == 0

    def test_process_store_hemlock_server(self):
        """
        Calls the test function for the store_hemlock_server action.
        """
        error = self.process_store_hemlock_server()
        for err in error:
            assert err == 0

    def test_process_favicon(self):
        """
        Calls the test function for the favicon action.
        """
        error = self.process_favicon()
        for err in error:
            assert err == 0
