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

import ast, os, pexpect, web

class Hemlock_REST():
    def __init__(self, port=8080, host="0.0.0.0"):
        # !! TODO check for environment variables for hemlock.py
        urls = (
            '/add/system/(.*)/tenant/(.*)', 'add',
            '/add/user/(.*)/role/(.*)', 'add',
            '/add/user/(.*)/tenant/(.*)', 'add',
            '/create/role', 'create',
            '/create/tenant', 'create',
            '/create/user', 'create',
            '/delete/role/(.*)', 'delete',
            '/delete/tenant/(.*)', 'delete',
            '/delete/user/(.*)', 'delete',
            '/deregister/local-system/(.*)', 'deregister',
            '/deregister/remote-system/(.*)', 'deregister',
            '/get/role/(.*)', 'get',
            '/get/system/(.*)', 'get',
            '/get/tenant/(.*)', 'get',
            '/get/user/(.*)', 'get',
            '/list/all', 'list1',
            '/list/roles', 'list1',
            '/list/systems', 'list1',
            '/list/tenants', 'list1',
            '/list/users', 'list1',
            '/list/role/users/(.*)', 'list2',
            '/list/system/tenants/(.*)', 'list2',
            '/list/tenant/systems/(.*)', 'list2',
            '/list/tenant/users/(.*)', 'list2',
            '/list/user/roles/(.*)', 'list2',
            '/list/user/tenants/(.*)', 'list2',
            '/register/local-system', 'register',
            '/register/remote-system', 'register',
            '/remove/system/(.*)/tenant/(.*)', 'remove',
            '/remove/user/(.*)/role/(.*)', 'remove',
            '/remove/user/(.*)/tenant/(.*)', 'remove',
            '/favicon.ico','favicon'
        )
        app = web.application(urls, globals())
        web.httpserver.runsimple(app.wsgifunc(), (host, port))

class favicon: 
    def GET(self): 
        f = open("static/favicon.ico", 'rb') 
        web.header("Content-Type","image/x-icon")
        return f.read()

class search:
    def GET(self, query):
        # !! TODO send query to elasticsearch
        # !! TODO parse response for ids
        # !! TODO send ids to couchbase
        # !! TODO return list of json objects
        return query

class fields:
    def GET(self):
        true = True
        false = False
        null = None
        mapping = urllib2.urlopen("http://localhost:9200/_mapping").read()
        mapping = json.loads(mapping)
        return sorted(mapping["hemlock"]["couchbaseDocument"]["properties"]["doc"]["properties"].keys())
        
class add:
    def GET(self, first, second):
        if "system" in web.ctx['fullpath']:
            cmd = "hemlock system-add-tenant --uuid "+first+" --tenant_id "+second
        elif "role" in web.ctx['fullpath']:
            cmd = "hemlock user-add-role --uuid "+first+" --role_id "+second
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-add-tenant --uuid "+first+" --tenant_id "+second
        return os.popen(cmd).read()

class create:
    def POST(self):
        data = web.data()
        data = ast.literal_eval(data)
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock role-create --name "+data['name']
            return os.popen(cmd).read()
        elif "tenant" in web.ctx['fullpath']:
            cmd = "hemlock tenant-create --name "+data['name']
            return os.popen(cmd).read()
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-create --name "+data['name']+" --username "+data['username']+" --email "+data['email']+" --role_id "+data['role_id']+" --tenant_id "+data['tenant_id']
            child = pexpect.spawn(cmd)
            child.expect('Password:')
            child.sendline(data['password'])
            return child.read()
        return

class delete:
    def GET(self, uuid):
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock role-delete --uuid "+uuid
        elif "system" in web.ctx['fullpath']:
            cmd = "hemlock system-delete --uuid "+uuid
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-delete --uuid "+uuid
        elif "tenant" in web.ctx['fullpath']:
            cmd = "hemlock tenant-delete --uuid "+uuid
        return os.popen(cmd).read()

class deregister:
    def GET(self, uuid):
        if "local" in web.ctx['fullpath']:
            cmd = "hemlock deregister-local-system --uuid "+uuid
        elif "remote" in web.ctx['fullpath']:
            cmd = "hemlock deregister-remote-system --uuid "+uuid
        return os.popen(cmd).read()

class get:
    def GET(self, uuid):
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock role-get --uuid "+uuid
        elif "system" in web.ctx['fullpath']:
            cmd = "hemlock system-get --uuid "+uuid
        elif "tenant" in web.ctx['fullpath']:
            cmd = "hemlock tenant-get --uuid "+uuid
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-get --uuid "+uuid
        return os.popen(cmd).read()

class list1:
    def GET(self):
        if "roles" in web.ctx['fullpath']:
            cmd = "hemlock role-list"
        if "systems" in web.ctx['fullpath']:
            cmd = "hemlock system-list"
        elif "tenants" in web.ctx['fullpath']:
            cmd = "hemlock tenant-list"
        elif "users" in web.ctx['fullpath']:
            cmd = "hemlock user-list"
        elif "all" in web.ctx['fullpath']:
            cmd = "hemlock list-all"
        return os.popen(cmd).read()

class list2:
    def GET(self, uuid):
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
        return os.popen(cmd).read()

class register:
    def POST(self):
        data = web.data()
        data = ast.literal_eval(data)
        if "local" in web.ctx['fullpath']:
            cmd = "hemlock register-local-system --name "+data['name']+" --data_type "+data['data_type']+" --description "+data['description']+" --tenant_id "+data['tenant_id']+" --hostname "+data['hostname']+" --endpoint "+data['endpoint']+" --poc_name "+data['poc_name']+" --poc_email "+data['poc_email']
        elif "remote" in web.ctx['fullpath']:
            cmd = "hemlock register-remote-system --name "+data['name']+" --data_type "+data['data_type']+" --description "+data['description']+" --tenant_id "+data['tenant_id']+" --hostname "+data['hostname']+" --port "+data['port']+" --remote_uri "+data['remote_uri']+" --poc_name "+data['poc_name']+" --poc_email "+data['poc_email']
        return os.popen(cmd).read()

class remove:
    def GET(self, first, second):
        if "role" in web.ctx['fullpath']:
            cmd = "hemlock user-remove-role --uuid "+first+" --role_id "+second
        if "system" in web.ctx['fullpath']:
            cmd = "hemlock system-remove-tenant --uuid "+first+" --tenant_id "+second
        elif "user" in web.ctx['fullpath']:
            cmd = "hemlock user-remove-tenant --uuid "+first+" --tenant_id "+second
        return os.popen(cmd).read()

if __name__ == "__main__":
    app.run()