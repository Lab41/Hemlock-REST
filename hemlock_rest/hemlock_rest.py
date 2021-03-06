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
import sys
import urllib2
import web

class Hemlock_REST(object):
    """
    This class is responsible for initializing the urls and web server.
    """
    # !! TODO
    # need __new__ for tests, but fails to call __init__ when actually running
    def __new__(*args, **kw):
        if hasattr(sys, '_called_from_test'):
            print "don't call __init__"
        else: # pragma: no cover
            return object.__new__(*args, **kw)

    def __init__(self, port=3001, host="0.0.0.0"): # pragma: no cover
        # !! TODO check for environment variables for hemlock.py
        # !! TODO needs to be able to use no_couchbase flag
        urls = self.setup()
        app = web.application(urls, globals())
        web.httpserver.runsimple(app.wsgifunc(), (host, port))

    def setup(self):
        urls = (
            '/', 'root',
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
            '/register/local-system', 'register',
            '/register/remote-system', 'register',
            '/remove/client/(.*)/schedule/(.*)', 'remove',
            '/remove/schedule/(.*)/client/(.*)', 'remove',
            '/remove/system/(.*)/tenant/(.*)', 'remove',
            '/remove/user/(.*)/role/(.*)', 'remove',
            '/remove/user/(.*)/tenant/(.*)', 'remove',
            '/run/client/(.*)/(.*)', 'run',
            '/schedule/client', 'create',
            '/start/scheduler/(.*)', 'start',
            '/store/client', 'create',
            '/store/hemlock-server', 'create',
            '/version', 'version',
            '/favicon.ico','favicon'
        )
        return urls

class root:
    """
    This class is resposible for giving information about the rest server.
    """
    def GET(self):
        """
        GETs the information about the rest server and renders it.

        :return: returns the information
        """
        return "Hemlock RESTful Server."

class version:
    """
    This class is resposible for returing the version of the rest server.
    """
    def GET(self):
        """
        GETs the version of the rest server and renders it.

        :return: returns the version
        """
        return "0.1.6"

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

class start:
    """
    This class is responsible for starting the scheduler.
    """
    def GET(self):
        """
        Starts the schedule server on the server id specified.

        :return: returns the status of starting the scheduler
        """
        # !! TODO
        return

class query:
    """
    This class is responsible for all data query requests.
    """
    def __init__(self):
        self.data = "[]"
        try:
            self.data = web.data()
        except:
            print "failure"

    def POST(self):
        """
        POSTs the authentication for the query and returns the query respond
        specific to the user credentials provided.

        :return: returns the results of the query
        """
        try:
            self.data = ast.literal_eval(self.data)
            # !! TODO add no_couchbase flag
            cmd = "hemlock query-data --user "+self.data['user']+" --query "+self.data['query']
            child = pexpect.spawn(cmd)
            child.expect('Password:')
            child.sendline(self.data['password'])
            return child.read()
        except:
            return ""

class fields:
    """
    This class is responsible for all requests about data fields or schemas.
    """
    def GET(self):
        """
        GETs the schemas of all data that is stored in Hemlock.

        :return: returns the fields in all schemas stored in Hemlock
        """
        # !! TODO placeholder
        true = True
        false = False
        null = None
        try:
            mapping = urllib2.urlopen("http://localhost:9200/_mapping").read()
            mapping = json.loads(mapping)
            return sorted(mapping["hemlock"]["couchbaseDocument"]["properties"]["doc"]["properties"].keys())
        except:
            return ""

class add:
    """
    This class is responsible for all API actions that involve adding something
    to something else.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self, first, second):
        """
        Performs the add actions of the API.

        :param first: the uuid of the first part of the action
        :param second: the uuid of the second part of the action
        :return: returns the result of the action
        """
        cmd = ""
        try:
            if "system" in self.fullpath:
                cmd = "hemlock system-add-tenant --uuid "+first+" --tenant_id "+second
            elif "add/client" in self.fullpath:
                cmd = "hemlock client-add-schedule --uuid "+first+" --schedule_id "+second
            elif "add/schedule" in self.fullpath:
                cmd = "hemlock schedule-add-client --uuid "+first+" --client_id "+second
            elif "role" in self.fullpath:
                cmd = "hemlock user-add-role --uuid "+first+" --role_id "+second
            elif "user" in self.fullpath:
                cmd = "hemlock user-add-tenant --uuid "+first+" --tenant_id "+second
        except:
            print "failure"
        return os.popen(cmd).read()

class change:
    """
    This class is responsible for changing the server that a schedule runs on.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self, first, second):
        """
        Performs the change action of the API.

        :param first: the uuid of the schedule to change
        :param second: the uuid of the server the schedule is being changed to
        :return: returns the result of the action
        """
        cmd = ""
        try:
            if "server" in self.fullpath:
                cmd = "hemlock schedule-change-server --uuid "+first+" --schedule_server_id "+second
        except:
            print "failure"
        return os.popen(cmd).read()

class create:
    """
    This class is responsible for all API actions that involve creating
    someting.
    """
    def __init__(self):
        self.data = ""
        self.fullpath = ""
        try:
            self.data = web.data()
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def POST(self):
        """
        POSTs the create actions of the API.

        :return: returns the result of the action
        """
        cmd = ""
        try:
            self.data = ast.literal_eval(self.data)
            if "role" in self.fullpath:
                cmd = "hemlock role-create --name "+self.data['name']
                return os.popen(cmd).read()
            elif "schedule_server" in self.fullpath:
                cmd = "hemlock schedule-server-create --name "+self.data['name']
                return os.popen(cmd).read()
            elif "tenant" in self.fullpath:
                cmd = "hemlock tenant-create --name "+self.data['name']
                return os.popen(cmd).read()
            elif "schedule" in self.fullpath:
                cmd = "hemlock client-schedule --name "+self.data['name']+" --minute "+self.data['minute']+" --hour "+self.data['hour']+" --day_of_month "+self.data['day_of_month']+" --month "+self.data['month']+" --day_of_week "+self.data['day_of_week']+" --client_id "+self.data['client_id']
                return os.popen(cmd).read()
            elif "client" in self.fullpath:
                # !! TODO add no_coucnhase flag
                cmd = "hemlock client-store --name "+self.data['name']+" --type "+self.data['type']+" --system_id "+self.data['system_id']+" --credential_file "+self.data['credential_file']
                return os.popen(cmd).read()
            elif "hemlock-server" in self.fullpath:
                cmd = "hemlock hemlock-server-store --credential_file "+self.data['credential_file']
                return os.popen(cmd).read()
            elif "user" in self.fullpath:
                cmd = "hemlock user-create --name "+self.data['name']+" --username "+self.data['username']+" --email "+self.data['email']+" --role_id "+self.data['role_id']+" --tenant_id "+self.data['tenant_id']
                child = pexpect.spawn(cmd)
                child.expect('Password:')
                child.sendline(self.data['password'])
                return child.read()
        except:
            print "failure"
        return

class delete:
    """
    This class is responsible for all API actions that involve deleting
    something.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self, uuid):
        """
        Performs the delete actions of the API.

        :param uuid: the uuid of the item being deleted
        :return: returns the result of the action
        """
        cmd = ""
        try:
            if "role" in self.fullpath:
                cmd = "hemlock role-delete --uuid "+uuid
            elif "schedule_server" in self.fullpath:
                cmd = "hemlock schedule-server-delete --uuid "+uuid
            elif "system" in self.fullpath:
                cmd = "hemlock system-delete --uuid "+uuid
            elif "user" in self.fullpath:
                cmd = "hemlock user-delete --uuid "+uuid
            elif "tenant" in self.fullpath:
                cmd = "hemlock tenant-delete --uuid "+uuid
            elif "schedule" in self.fullpath:
                cmd = "hemlock schedule-delete --uuid "+uuid
            elif "client" in self.fullpath:
                cmd = "hemlock client-purge --uuid "+uuid
        except:
            print "failure"
        return os.popen(cmd).read()

class deregister:
    """
    This class is responsible for deregistering systems.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self, uuid):
        """
        Performs the deregister action of the API.

        :param uuid: the uuid of the system being deregistered
        :return: returns the result of the action
        """
        cmd = ""
        try:
            if "local" in self.fullpath:
                cmd = "hemlock deregister-local-system --uuid "+uuid
            elif "remote" in self.fullpath:
                cmd = "hemlock deregister-remote-system --uuid "+uuid
        except:
            print "failure"
        return os.popen(cmd).read()

class get:
    """
    This class is responsible for all API actions that involve getting
    something.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self, uuid):
        """
        Performs the get actions of the API.

        :param uuid: the uuid of the item to get
        :return: returns the result of the action
        """
        cmd = ""
        try:
            if "role" in self.fullpath:
                cmd = "hemlock role-get --uuid "+uuid
            elif "schedule_server" in self.fullpath:
                cmd = "hemlock schedule-server-get --uuid "+uuid
            elif "system" in self.fullpath:
                cmd = "hemlock system-get --uuid "+uuid
            elif "tenant" in self.fullpath:
                cmd = "hemlock tenant-get --uuid "+uuid
            elif "user" in self.fullpath:
                cmd = "hemlock user-get --uuid "+uuid
            elif "client" in self.fullpath:
                cmd = "hemlock client-get --uuid "+uuid
            elif "schedule" in self.fullpath:
                cmd = "hemlock schedule-get --uuid "+uuid
        except:
            print "failure"
        return os.popen(cmd).read()

class list1:
    """
    This class is responsible for all API actions that involve listing
    a type of something.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self):
        """
        Performs the list actions of the API for a given type.

        :returns: returns the results of the action
        """
        cmd = ""
        try:
            if "roles" in self.fullpath:
                cmd = "hemlock role-list"
            elif "schedule_server" in self.fullpath:
                cmd = "hemlock schedule-server-list"
            elif "systems" in self.fullpath:
                cmd = "hemlock system-list"
            elif "tenants" in self.fullpath:
                cmd = "hemlock tenant-list"
            elif "users" in self.fullpath:
                cmd = "hemlock user-list"
            elif "clients" in self.fullpath:
                cmd = "hemlock client-list"
            elif "schedules" in self.fullpath:
                cmd = "hemlock schedule-list"
            elif "all" in self.fullpath:
                cmd = "hemlock list-all"
        except:
            print "failure"
        return os.popen(cmd).read()

class list2:
    """
    This class is responsible for all API actions that involve listing
    something specific to something else.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self, uuid):
        """
        Performs the list actions of the API specific to a given something.

        :param uuid: the uuid of the specific item to get a list relative to
        :return: returns the results of the action
        """
        cmd = ""
        try:
            if "system" in self.fullpath and "tenants" in self.fullpath:
                cmd = "hemlock system-tenants-list --uuid "+uuid
            elif "tenant" in self.fullpath and "systems" in self.fullpath:
                cmd = "hemlock tenant-systems-list --uuid "+uuid
            elif "tenant" in self.fullpath and "users" in self.fullpath:
                cmd = "hemlock tenant-users-list --uuid "+uuid
            elif "user" in self.fullpath and "roles" in self.fullpath:
                cmd = "hemlock user-roles-list --uuid "+uuid
            elif "role" in self.fullpath and "users" in self.fullpath:
                cmd = "hemlock role-users-list --uuid "+uuid
            elif "user" in self.fullpath and "tenants" in self.fullpath:
                cmd = "hemlock user-tenants-list --uuid "+uuid
            elif "client" in self.fullpath and "schedules" in self.fullpath:
                cmd = "hemlock client-schedules-list --uuid "+uuid
            elif "client" in self.fullpath and "systems" in self.fullpath:
                cmd = "hemlock client-systems-list --uuid "+uuid
            elif "schedule" in self.fullpath and "clients" in self.fullpath:
                cmd = "hemlock schedule-clients-list --uuid "+uuid
            elif "system" in self.fullpath and "clients" in self.fullpath:
                cmd = "hemlock system-clients-list --uuid "+uuid
        except:
            print "failure"
        return os.popen(cmd).read()

class register:
    """
    This class is responsble for registering a system.
    """
    def __init__(self):
        self.data = ""
        self.fullpath = ""
        try:
            self.data = web.data()
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def POST(self):
        """
        Performs the register action of the API.

        :return: returns the result of the action
        """
        cmd = ""
        try:
            self.data = ast.literal_eval(self.data)
            if "local" in self.fullpath:
                cmd = "hemlock register-local-system --name "+self.data['name']+" --data_type "+self.data['data_type']+" --description "+self.data['description']+" --tenant_id "+self.data['tenant_id']+" --hostname "+self.data['hostname']+" --endpoint "+self.data['endpoint']+" --poc_name "+self.data['poc_name']+" --poc_email "+self.data['poc_email']
            elif "remote" in self.fullpath:
                cmd = "hemlock register-remote-system --name "+self.data['name']+" --data_type "+self.data['data_type']+" --description "+self.data['description']+" --tenant_id "+self.data['tenant_id']+" --hostname "+self.data['hostname']+" --port "+self.data['port']+" --remote_uri "+self.data['remote_uri']+" --poc_name "+self.data['poc_name']+" --poc_email "+self.data['poc_email']
        except:
            print "failure"
        return os.popen(cmd).read()

class remove:
    """
    This class is responsible for all API actions that involve removing
    something.
    """
    def __init__(self):
        self.fullpath = ""
        try:
            self.fullpath = web.ctx['fullpath']
        except:
            print "failure"

    def GET(self, first, second):
        """
        Performs the remove actions of the API.

        :param first: the uuid of the first part of the action
        :param second: the uuid of the second part of the action
        :return: returns the result of the action
        """
        cmd = ""
        try:
            if "role" in self.fullpath:
                cmd = "hemlock user-remove-role --uuid "+first+" --role_id "+second
            if "system" in self.fullpath:
                cmd = "hemlock system-remove-tenant --uuid "+first+" --tenant_id "+second
            elif "user" in self.fullpath:
                cmd = "hemlock user-remove-tenant --uuid "+first+" --tenant_id "+second
            elif "remove/client" in self.fullpath:
                cmd = "hemlock client-remove-schedule --uuid "+first+" --schedule_id "+second
            elif "remove/schedule" in self.fullpath:
                cmd = "hemlock schedule-remove-client --uuid "+first+" --client_id "+second
        except:
            print "failure"
        return os.popen(cmd).read()

class run:
    """
    This class is responsible for performing a run action of the API.
    """
    def GET(self, first, second):
        # !! TODO add no_coucnhase flag
        # !! TODO this needs to be updated and tested
        """
        Performs the run action of the API.

        :param first: the uuid of the client to run
        :param second: the client type that is to run
        :returns: returns the result of the action
        """
        cmd = "hemlock client-run --uuid "+first+" --client "+second
        return os.popen(cmd).read()

if __name__ == "__main__": # pragma: no cover
    hemlock_rest = Hemlock_REST()
    hemlock_rest.app.run()
