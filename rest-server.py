#!/usr/bin/python

import ast, os, pexpect, web
        
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

class favicon: 
    def GET(self): 
        f = open("static/favicon.ico", 'rb') 
        web.header("Content-Type","image/x-icon")
        return f.read()

class add:
    def GET(self, first, second):
        if "system" in web.ctx['fullpath']:
            cmd = "python hemlock.py system-add-tenant --uuid "+first+" --tenant_id "+second
        elif "role" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-add-role --uuid "+first+" --role_id "+second
        elif "user" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-add-tenant --uuid "+first+" --tenant_id "+second
        return os.popen(cmd).read()

class create:
    def POST(self):
        data = web.data()
        data = ast.literal_eval(data)
        if "role" in web.ctx['fullpath']:
            cmd = "python hemlock.py role-create --name "+data['name']
            return os.popen(cmd).read()
        elif "tenant" in web.ctx['fullpath']:
            cmd = "python hemlock.py tenant-create --name "+data['name']
            return os.popen(cmd).read()
        elif "user" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-create --name "+data['name']+" --username "+data['username']+" --email "+data['email']+" --role_id "+data['role_id']+" --tenant_id "+data['tenant_id']
            child = pexpect.spawn(cmd)
            child.expect('Password:')
            child.sendline(data['password'])
            return child.read()
        return

class delete:
    def GET(self, uuid):
        if "role" in web.ctx['fullpath']:
            cmd = "python hemlock.py role-delete --uuid "+uuid
        elif "system" in web.ctx['fullpath']:
            cmd = "python hemlock.py system-delete --uuid "+uuid
        elif "user" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-delete --uuid "+uuid
        elif "tenant" in web.ctx['fullpath']:
            cmd = "python hemlock.py tenant-delete --uuid "+uuid
        return os.popen(cmd).read()

class deregister:
    def GET(self, uuid):
        if "local" in web.ctx['fullpath']:
            cmd = "python hemlock.py deregister-local-system --uuid "+uuid
        elif "remote" in web.ctx['fullpath']:
            cmd = "python hemlock.py deregister-remote-system --uuid "+uuid
        return os.popen(cmd).read()

class get:
    def GET(self, uuid):
        if "role" in web.ctx['fullpath']:
            cmd = "python hemlock.py role-get --uuid "+uuid
        elif "system" in web.ctx['fullpath']:
            cmd = "python hemlock.py system-get --uuid "+uuid
        elif "tenant" in web.ctx['fullpath']:
            cmd = "python hemlock.py tenant-get --uuid "+uuid
        elif "user" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-get --uuid "+uuid
        return os.popen(cmd).read()

class list1:
    def GET(self):
        if "roles" in web.ctx['fullpath']:
            cmd = "python hemlock.py role-list"
        if "systems" in web.ctx['fullpath']:
            cmd = "python hemlock.py system-list"
        elif "tenants" in web.ctx['fullpath']:
            cmd = "python hemlock.py tenant-list"
        elif "users" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-list"
        return os.popen(cmd).read()

class list2:
    def GET(self, uuid):
        if "system" in web.ctx['fullpath'] and "tenants" in web.ctx['fullpath']:
            cmd = "python hemlock.py system-tenants-list --uuid "+uuid
        elif "tenant" in web.ctx['fullpath'] and "systems" in web.ctx['fullpath']:
            cmd = "python hemlock.py tenant-systems-list --uuid "+uuid
        elif "tenant" in web.ctx['fullpath'] and "users" in web.ctx['fullpath']:
            cmd = "python hemlock.py tenant-users-list --uuid "+uuid
        elif "user" in web.ctx['fullpath'] and "roles" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-roles-list --uuid "+uuid
        elif "user" in web.ctx['fullpath'] and "tenants" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-tenants-list --uuid "+uuid
        return os.popen(cmd).read()

class register:
    def POST(self):
        data = web.data()
        data = ast.literal_eval(data)
        if "local" in web.ctx['fullpath']:
            cmd = "python hemlock.py register-local-system --name "+data['name']+" --data_type "+data['data_type']+" --description "+data['description']+" --tenant_id "+data['tenant_id']+" --hostname "+data['hostname']+" --endpoint "+data['endpoint']+" --poc_name "+data['poc_name']+" --poc_email "+data['poc_email']
        elif "remote" in web.ctx['fullpath']:
            cmd = "python hemlock.py register-remote-system --name "+data['name']+" --data_type "+data['data_type']+" --description "+data['description']+" --tenant_id "+data['tenant_id']+" --hostname "+data['hostname']+" --port "+data['port']+" --remote_uri "+data['remote_uri']+" --poc_name "+data['poc_name']+" --poc_email "+data['poc_email']
        return os.popen(cmd).read()

class remove:
    def GET(self, first, second):
        if "role" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-remove-role --uuid "+first+" --role_id "+second
        if "system" in web.ctx['fullpath']:
            cmd = "python hemlock.py system-remove-tenant --uuid "+first+" --tenant_id "+second
        elif "user" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-remove-tenant --uuid "+first+" --tenant_id "+second
        return os.popen(cmd).read()

if __name__ == "__main__":
    app.run()

# !! TODO a better way would be to make hemlock.py a class and import the class/functions needed
