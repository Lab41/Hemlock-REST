#!/usr/bin/python

import os, web
        
urls = (
    '/deregister-local-system', 'deregister_local_system',
    '/deregister-remote-system', 'deregister_remote_system',
    '/register-local-system', 'register_local_system',
    '/register-remote-system', 'register_remote_system',
    '/system-add-tenant', 'system_add_tenant',
    '/system-get', 'system_get',
    '/system-list', 'system_list',
    '/system-remove-tenant', 'system_remove_tenant',
    '/system-tenants-list', 'system_tenants_list',
    '/tenant-create', 'tenant_create',
    '/tenant-delete', 'tenant_delete',
    '/tenant-get', 'tenant_get',
    '/tenant-list', 'tenant_list',
    '/tenant-systems-list', 'tenant_systems_list',
    '/tenant-users-list', 'tenant_users_list',
    '/user-add-tenant', 'user_add_tenant',
    '/user-create', 'user_create',
    '/user-delete', 'user_delete',
    '/user-get', 'user_get',
    '/user-list', 'user_list',
    '/user-remove-tenant', 'user_remove_tenant',
    '/user-tenants-list', 'user_tenants_list'
)
app = web.application(urls, globals())

class deregister_local_system:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class deregister_remote_system:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class register_local_system:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class register_remote_system:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class system_add_tenant:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class system_get:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class system_list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class system_remove_tenant:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class system_tenants_list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class tenant_create:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class tenant_delete:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class tenant_get:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class tenant_list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class tenant_systems_list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class tenant_users_list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class user_add_tenant:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class user_create:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class user_delete:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class user_get:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class user_list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class user_remove_tenant:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class user_tenants_list:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
