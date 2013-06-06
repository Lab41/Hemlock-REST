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
    '/remove/user/(.*)/tenant/(.*)', 'remove'
)
app = web.application(urls, globals())

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
        cmd = "python hemlock.py user-list"
        a = os.popen(cmd).read()
        return 'Hello, ' + name + '!'

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
