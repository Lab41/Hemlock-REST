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
This module is the web server for running the REST API of Hemlock.

Created on 20 August 2013
@author: Charlie Lewis
"""

import ast
import os
import pexpect
import web

class Hemlock_REST():
    """
    This class is responsible for initializing the urls and web server.
    """
    def __init__(self, port=8080, host="0.0.0.0"):
        # !! TODO check for environment variables for hemlock.py
        urls = (
            '/add/client/(.*)/schedule/(.*)', 'add',
            '/add/schedule/(.*)/client/(.*)', 'add',
            '/add/system/(.*)/tenant/(.*)', 'add',
            '/add/user/(.*)/role/(.*)', 'add',
            '/add/user/(.*)/tenant/(.*)', 'add',
            '/change/schedule/(.*)/server/(.*)', 'change',
            '/create/role', 'create',
            '/create/schedule_server', 'create',
            '/create/tenant', 'create',
            '/create/user', 'create',
            '/delete/role/(.*)', 'delete',
            '/delete/schedule_server/(.*)', 'delete',
            '/delete/schedule/(.*)', 'delete',
            '/delete/tenant/(.*)', 'delete',
            '/delete/user/(.*)', 'delete',
            '/deregister/local-system/(.*)', 'deregister',
            '/deregister/remote-system/(.*)', 'deregister',
            '/get/client/(.*)', 'get',
            '/get/role/(.*)', 'get',
            '/get/schedule_server/(.*)', 'get',
            '/get/schedule/(.*)', 'get',
            '/get/system/(.*)', 'get',
            '/get/tenant/(.*)', 'get',
            '/get/user/(.*)', 'get',
            '/list/all', 'list1',
            '/list/clients', 'list1',
            '/list/roles', 'list1',
            '/list/schedule_servers', 'list1',
            '/list/schedules', 'list1',
            '/list/systems', 'list1',
            '/list/tenants', 'list1',
            '/list/users', 'list1',
            '/list/client/schedules/(.*)', 'list2',
            '/list/client/systems/(.*)', 'list2',
            '/list/role/users/(.*)', 'list2',
            '/list/schedule/clients/(.*)', 'list2',
            '/list/system/clients/(.*)', 'list2',
            '/list/system/tenants/(.*)', 'list2',
            '/list/tenant/systems/(.*)', 'list2',
            '/list/tenant/users/(.*)', 'list2',
            '/list/user/roles/(.*)', 'list2',
            '/list/user/tenants/(.*)', 'list2',
            '/purge/client/(.*)', 'delete',
            '/query', 'query',
            '/run/client/(.*)/(.*)', 'run',
            '/register/local-system', 'register',
            '/register/remote-system', 'register',
            '/remove/client/(.*)/schedule/(.*)', 'remove',
            '/remove/schedule/(.*)/client/(.*)', 'remove',
            '/remove/system/(.*)/tenant/(.*)', 'remove',
            '/remove/user/(.*)/role/(.*)', 'remove',
            '/remove/user/(.*)/tenant/(.*)', 'remove',
            '/schedule/client', 'create',
            '/store/client', 'create',
            '/store/hemlock-server', 'create',
            '/favicon.ico','favicon'
        )
        app = web.application(urls, globals())
        web.httpserver.runsimple(app.wsgifunc(), (host, port))

class favicon:
    """
    This class is responsible for rendering the favicon.
    """
    def GET(self):
        """
        GETs the favicon for http requests.

        :return: returns the favicon
        """
        f = open("static/favicon.ico", 'rb')
        web.header("Content-Type","image/x-icon")
        return f.read()

class query:
    """
    This class is responsible for all data query requests.
    """
    def POST(self):
        """
        POSTs the authentication for the query and returns the query respond
        specific to the user credentials provided.

        :return: returns the results of the query
        """
        data = web.data()
        data = ast.literal_eval(data)
        cmd = "hemlock query-data --user "+data['user']+" --query "+data['query']
        child = pexpect.spawn(cmd)
        child.expect('Password:')
        child.sendline(data['password'])
        return child.read()

class fields:
    """
    This class is responsible for all requests about data fields or schemas.
    """
    def GET(self):
        """
        GETs the schemas of all data that is stored in Hemlock.

        :return: returns the fields in all schemas stored in Hemlock
        """
        true = True
        false = False
        null = None
        mapping = urllib2.urlopen("http://localhost:9200/_mapping").read()
        mapping = json.loads(mapping)
        return sorted(mapping["hemlock"]["couchbaseDocument"]["properties"]["doc"]["properties"].keys())

class add:
    """
    This class is responsible for all API actions that involve adding something
    to something else.
    """
    def GET(self, first, second):
        """
        Performs the add actions of the API.

        :param first: the uuid of the first part of the action
        :param second: the uuid of the second part of the action
        :return: returns the result of the action
        """
        if "system" in web.ctx['fullpath']:
            cmd = "hemlock system-add-tenant --uuid "+first+" --tenant_id "+second
        elif "add/client" in web.ctx['fullpath']:
            cmd = "hemlock client-add-schedule --uuid "+first+" --schedule_id "+second
        elif "add/schedule" in web.ctx['fullpath']:
            cmd = "hemlock schedule-add-client --uuid "+first+" --client_id "+second
        elif "role" in web.ctx['fullpath']:
            cmd = "hemlock user-add-role --uuid "+first+" --role_id "+second
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-add-tenant --uuid "+first+" --tenant_id "+second
        return os.popen(cmd).read()

class change:
    """
    This class is responsible for changing the server that a schedule runs on.
    """
    def GET(self, first, second):
        """
        Performs the change action of the API.

        :param first: the uuid of the schedule to change
        :param second: the uuid of the server the schedule is being changed to
        :return: returns the result of the action
        """
        if "server" in web.ctx['fullpath']:
            cmd = "hemlock schedule-change-server --uuid "+first+" --schedule_server_id "+second
        return os.popen(cmd).read()

class create:
    """
    This class is responsible for all API actions that involve creating
    someting.
    """
    def POST(self):
        """
        POSTs the create actions of the API.

        :return: returns the result of the action
        """
        data = web.data()
        data = ast.literal_eval(data)
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock role-create --name "+data['name']
            return os.popen(cmd).read()
        elif "schedule_server" in web.ctx['fullpath']:
            cmd = "hemlock schedule-server-create --name "+data['name']
            return os.popen(cmd).read()
        elif "tenant" in web.ctx['fullpath']:
            cmd = "hemlock tenant-create --name "+data['name']
            return os.popen(cmd).read()
        elif "schedule" in web.ctx['fullpath']:
            cmd = "hemlock client-schedule --name "+data['name']+" --minute "+data['minute']+" --hour "+data['hour']+" --day_of_month "+data['day_of_month']+" --month "+data['month']+" --day_of_week "+data['day_of_week']+" --client_id "+data['client_id']
            return os.popen(cmd).read()
        elif "client" in web.ctx['fullpath']:
            cmd = "hemlock client-store --name "+data['name']+" --type "+data['type']+" --system_id "+data['system_id']+" --credential_file "+data['credential_file']
            return os.popen(cmd).read()
        elif "hemlock-server" in web.ctx['fullpath']:
            cmd = "hemlock hemlock-server-store --credential_file "+data['credential_file']
            return os.popen(cmd).read()
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-create --name "+data['name']+" --username "+data['username']+" --email "+data['email']+" --role_id "+data['role_id']+" --tenant_id "+data['tenant_id']
            child = pexpect.spawn(cmd)
            child.expect('Password:')
            child.sendline(data['password'])
            return child.read()
        return

class delete:
    """
    This class is responsible for all API actions that involve deleting
    something.
    """
    def GET(self, uuid):
        """
        Performs the delete actions of the API.

        :param uuid: the uuid of the item being deleted
        :return: returns the result of the action
        """
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock role-delete --uuid "+uuid
        elif "schedule_server" in web.ctx['fullpath']:
            cmd = "hemlock schedule-server-delete --uuid "+uuid
        elif "system" in web.ctx['fullpath']:
            cmd = "hemlock system-delete --uuid "+uuid
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-delete --uuid "+uuid
        elif "tenant" in web.ctx['fullpath']:
            cmd = "hemlock tenant-delete --uuid "+uuid
        elif "schedule" in web.ctx['fullpath']:
            cmd = "hemlock schedule-delete --uuid "+uuid
        elif "client" in web.ctx['fullpath']:
            cmd = "hemlock client-purge --uuid "+uuid
        return os.popen(cmd).read()

class deregister:
    """
    This class is responsible for deregistering systems.
    """
    def GET(self, uuid):
        """
        Performs the deregister action of the API.

        :param uuid: the uuid of the system being deregistered
        :return: returns the result of the action
        """
        if "local" in web.ctx['fullpath']:
            cmd = "hemlock deregister-local-system --uuid "+uuid
        elif "remote" in web.ctx['fullpath']:
            cmd = "hemlock deregister-remote-system --uuid "+uuid
        return os.popen(cmd).read()

class get:
    """
    This class is responsible for all API actions that involve getting
    something.
    """
    def GET(self, uuid):
        """
        Performs the get actions of the API.

        :param uuid: the uuid of the item to get
        :return: returns the result of the action
        """
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock role-get --uuid "+uuid
        elif "schedule_server" in web.ctx['fullpath']:
            cmd = "hemlock schedule-server-get --uuid "+uuid
        elif "system" in web.ctx['fullpath']:
            cmd = "hemlock system-get --uuid "+uuid
        elif "tenant" in web.ctx['fullpath']:
            cmd = "hemlock tenant-get --uuid "+uuid
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-get --uuid "+uuid
        elif "client" in web.ctx['fullpath']:
            cmd = "hemlock client-get --uuid "+uuid
        elif "schedule" in web.ctx['fullpath']:
            cmd = "hemlock schedule-get --uuid "+uuid
        return os.popen(cmd).read()

class list1:
    """
    This class is responsible for all API actions that involve listing
    a type of something.
    """
    def GET(self):
        """
        Performs the list actions of the API for a given type.

        :returns: returns the results of the action
        """
        if "roles" in web.ctx['fullpath']:
            cmd = "hemlock role-list"
        elif "schedule_server" in web.ctx['fullpath']:
            cmd = "hemlock schedule-server-list"
        elif "systems" in web.ctx['fullpath']:
            cmd = "hemlock system-list"
        elif "tenants" in web.ctx['fullpath']:
            cmd = "hemlock tenant-list"
        elif "users" in web.ctx['fullpath']:
            cmd = "hemlock user-list"
        elif "clients" in web.ctx['fullpath']:
            cmd = "hemlock client-list"
        elif "schedules" in web.ctx['fullpath']:
            cmd = "hemlock schedule-list"
        elif "all" in web.ctx['fullpath']:
            cmd = "hemlock list-all"
        return os.popen(cmd).read()

class list2:
    """
    This class is responsible for all API actions that involve listing
    something specific to something else.
    """
    def GET(self, uuid):
        """
        Performs the list actions of the API specific to a given something.

        :param uuid: the uuid of the specific item to get a list relative to
        :return: returns the results of the action
        """
        if "system" in web.ctx['fullpath'] and "tenants" in web.ctx['fullpath']:
            cmd = "hemlock system-tenants-list --uuid "+uuid
        elif "tenant" in web.ctx['fullpath'] and "systems" in web.ctx['fullpath']:
            cmd = "hemlock tenant-systems-list --uuid "+uuid
        elif "tenant" in web.ctx['fullpath'] and "users" in web.ctx['fullpath']:
            cmd = "hemlock tenant-users-list --uuid "+uuid
        elif "user" in web.ctx['fullpath'] and "roles" in web.ctx['fullpath']:
            cmd = "hemlock user-roles-list --uuid "+uuid
        elif "role" in web.ctx['fullpath'] and "users" in web.ctx['fullpath']:
            cmd = "hemlock role-users-list --uuid "+uuid
        elif "user" in web.ctx['fullpath'] and "tenants" in web.ctx['fullpath']:
            cmd = "hemlock user-tenants-list --uuid "+uuid
        elif "client" in web.ctx['fullpath'] and "schedules" in web.ctx['fullpath']:
            cmd = "hemlock client-schedules-list --uuid "+uuid
        elif "client" in web.ctx['fullpath'] and "systems" in web.ctx['fullpath']:
            cmd = "hemlock client-systems-list --uuid "+uuid
        elif "schedule" in web.ctx['fullpath'] and "clients" in web.ctx['fullpath']:
            cmd = "hemlock schedule-clients-list --uuid "+uuid
        elif "system" in web.ctx['fullpath'] and "clients" in web.ctx['fullpath']:
            cmd = "hemlock system-clients-list --uuid "+uuid
        return os.popen(cmd).read()

class register:
    """
    This class is responsble for registering a system.
    """
    def POST(self):
        """
        Performs the register action of the API.

        :return: returns the result of the action
        """
        data = web.data()
        data = ast.literal_eval(data)
        if "local" in web.ctx['fullpath']:
            cmd = "hemlock register-local-system --name "+data['name']+" --data_type "+data['data_type']+" --description "+data['description']+" --tenant_id "+data['tenant_id']+" --hostname "+data['hostname']+" --endpoint "+data['endpoint']+" --poc_name "+data['poc_name']+" --poc_email "+data['poc_email']
        elif "remote" in web.ctx['fullpath']:
            cmd = "hemlock register-remote-system --name "+data['name']+" --data_type "+data['data_type']+" --description "+data['description']+" --tenant_id "+data['tenant_id']+" --hostname "+data['hostname']+" --port "+data['port']+" --remote_uri "+data['remote_uri']+" --poc_name "+data['poc_name']+" --poc_email "+data['poc_email']
        return os.popen(cmd).read()

class remove:
    """
    This class is responsible for all API actions that involve removing
    something.
    """
    def GET(self, first, second):
        """
        Performs the remove actions of the API.

        :param first: the uuid of the first part of the action
        :param second: the uuid of the second part of the action
        :return: returns the result of the action
        """
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock user-remove-role --uuid "+first+" --role_id "+second
        if "system" in web.ctx['fullpath']:
            cmd = "hemlock system-remove-tenant --uuid "+first+" --tenant_id "+second
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-remove-tenant --uuid "+first+" --tenant_id "+second
        elif "remove/client" in web.ctx['fullpath']:
            cmd = "hemlock client-remove-schedule --uuid "+first+" --schedule_id "+second
        elif "remove/schedule" in web.ctx['fullpath']:
            cmd = "hemlock schedule-remove-client --uuid "+first+" --client_id "+second
        return os.popen(cmd).read()

class run:
    """
    This class is responsible for performing a run action of the API.
    """
    def GET(self, first, second):
        # !! TODO this needs to be updated and tested
        """
        Performs the run action of the API.

        :param first: the uuid of the client to run
        :param second: the client type that is to run
        :returns: returns the result of the action
        """
        cmd = "hemlock client-run --uuid "+first+" --client "+second
        return os.popen(cmd).read()

if __name__ == "__main__":
    hemlock_rest = Hemlock_REST()
    hemlock_rest.app.run()
