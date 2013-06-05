#!/usr/bin/python

import web

# !! TODO calls to implement:
#        'deregister-local-system' : deregister_local_system,
#        'deregister-remote-system' : deregister_remote_system,
#        'register-local-system' : register_local_system,
#        'register-remote-system' : register_remote_system,
#        'system-add-tenant' : system_add_tenant,
#        'system-get' : system_get,
#        'system-list' : system_list,
#        'system-remove-tenant' : system_remove_tenant,
#        'system-tenants-list' : system_tenants_list,
#        'tenant-create' : tenant_create,
#        'tenant-delete' : tenant_delete,
#        'tenant-get' : tenant_get,
#        'tenant-list' : tenant_list,
#        'tenant-systems-list' : tenant_systems_list,
#        'tenant-users-list' : tenant_users_list,
#        'user-add-tenant' : user_add_tenant,
#        'user-create' : user_create,
#        'user-delete' : user_delete,
#        'user-get' : user_get,
#        'user-list' : user_list,
#        'user-remove-tenant' : user_remove_tenant,
#        'user-tenants-list' : user_tenants_list
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
