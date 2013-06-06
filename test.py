#!/usr/bin/python

import os, web
        
urls = (
    '/add/system/(.*)/tenant/(.*)', 'add',
    '/add/user/(.*)/tenant/(.*)', 'add',
    '/create/tenant', 'create',
    '/create/user', 'create',
    '/delete/tenant/(.*)', 'delete',
    '/delete/user/(.*)', 'delete',
    '/deregister/local-system/(.*)', 'deregister',
    '/deregister/remote-system/(.*)', 'deregister',
    '/get/system/(.*)', 'get',
    '/get/tenant/(.*)', 'get',
    '/get/user/(.*)', 'get',
    '/list/systems', 'list1',
    '/list/tenants', 'list1',
    '/list/users', 'list1',
    '/list/system/tenants/(.*)', 'list2',
    '/list/tenant/systems/(.*)', 'list2',
    '/list/tenant/users/(.*)', 'list2',
    '/list/user/tenants/(.*)', 'list2',
    '/register/local-system', 'register',
    '/register/remote-system', 'register',
    '/remove/system/(.*)/tenant/(.*)', 'remove',
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
        return "!"

class create:
    def POST(self):
        i = web.data()

class delete:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class deregister:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class get:
    def GET(self, name):
        if not name: 
            name = 'World'
        return web.ctx['fullpath']+'Hello, ' + name + '!'

class list1:
    def GET(self):
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
        elif "user" in web.ctx['fullpath'] and "tenants" in web.ctx['fullpath']:
            cmd = "python hemlock.py user-tenants-list --uuid "+uuid
        return os.popen(cmd).read()

class register:
    def POST(self):
        i = web.data()
        return i

class remove:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()

# !! TODO a better way would be to make hemlock.py a class and import the class/functions needed
