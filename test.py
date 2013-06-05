#!/usr/bin/python

import os, web
        
urls = (
    '/add/system/(.*)/tenant', 'add',
    '/add/user/(.*)/tenant', 'add',
    '/create/tenant', 'create',
    '/create/user', 'create',
    '/delete/tenant/(.*)', 'delete',
    '/delete/user/(.*)', 'delete',
    '/deregister/local-system/(.*)', 'deregister',
    '/deregister/remote-system/(.*)', 'deregister',
    '/get/system/(.*)', 'get',
    '/get/tenant/(.*)', 'get',
    '/get/user/(.*)', 'get',
    '/list/systems', 'list',
    '/list/tenants', 'list',
    '/list/users', 'list',
    '/list/system/tenants/(.*)', 'list',
    '/list/tenant/systems/(.*)', 'list',
    '/list/tenant/users/(.*)', 'list',
    '/list/user/tenants/(.*)', 'list',
    '/register/local-system', 'register',
    '/register/remote-system', 'register',
    '/remove/system/(.*)/tenant/(.*)', 'remove',
    '/remove/user/(.*)/tenant/(.*)', 'remove'
)
app = web.application(urls, globals())

class deregister:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class register:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class add:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class get:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class remove:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class create:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class delete:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
