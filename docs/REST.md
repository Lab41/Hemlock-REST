```
'/add/system/(.*)/tenant/(.*)'
     example usage:
                   curl http://server.fqdn:9001/add/system/59822f6b-4646-4dd8-9be9-038c2988375a/tenant/aa317893-6df2-4af6-88a5-3f395dfb0786
                   +-----------+--------------------------------------+
                   | Property  |                Value                 |
                   +-----------+--------------------------------------+
                   | tenant_id | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   |   uuid    | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   +-----------+--------------------------------------+
                   Took 0.0286719799042 seconds to complete.
```
```
'/add/user/(.*)/role/(.*)'
     example usage:
                   curl http://server.fqdn:9001/add/user/7e25110d-b9aa-4d03-9540-776e1bf44c2a/role/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a
                   +----------+--------------------------------------+
                   | Property |                Value                 |
                   +----------+--------------------------------------+
                   | role_id  | cdf10182-b0e0-4f3c-a47a-ba09a005eb5a |
                   |   uuid   | 7e25110d-b9aa-4d03-9540-776e1bf44c2a |
                   +----------+--------------------------------------+
                   Took 0.473670005798 seconds to complete.
```
```
'/add/user/(.*)/tenant/(.*)'
     example usage:
                   curl http://server.fqdn:9001/add/user/7e25110d-b9aa-4d03-9540-776e1bf44c2a/tenant/aa317893-6df2-4af6-88a5-3f395dfb0786
                   +-----------+--------------------------------------+
                   | Property  |                Value                 |
                   +-----------+--------------------------------------+
                   | tenant_id | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   |   uuid    | 7e25110d-b9aa-4d03-9540-776e1bf44c2a |
                   +-----------+--------------------------------------+
                   Took 2.99998903275 seconds to complete.

'/create/role'
     example usage:
                   curl -i -H "Content-Type: application/json" -X POST -d '{"name": "role1"}' http://server.fqdn:9001/create/role
                   +----------+--------------------------------------+
                   | Property |                Value                 |
                   +----------+--------------------------------------+
                   |   name   |                role1                 |
                   |   uuid   | cdf10182-b0e0-4f3c-a47a-ba09a005eb5a |
                   | created  |         2013-06-10 22:51:21          |
                   +----------+--------------------------------------+
```
```
'/create/tenant'
     example usage:
                   curl -i -H "Content-Type: application/json" -X POST -d '{"name": "tenant1"}' http://server.fqdn:9001/create/tenant
                   +----------+--------------------------------------+
                   | Property |                Value                 |
                   +----------+--------------------------------------+
                   |   name   |               tenant1                |
                   |   uuid   | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   | created  |         2013-06-10 22:51:38          |
                   +----------+--------------------------------------+
```
```
'/create/user'
     example usage:
                   curl -i -H "Content-Type: application/json" -X POST -d '{"name": "user1", "password": "asdf", "username": "username1", "email": "user1@email.com", "role_id": "cdf10182-b0e0-4f3c-a47a-ba09a005eb5a", "tenant_id": "aa317893-6df2-4af6-88a5-3f395dfb0786"}' http://server.fqdn:9001/create/user
                   +-----------+--------------------------------------+
                   | Property  |                Value                 |
                   +-----------+--------------------------------------+
                   |   name    |                user1                 |
                   | tenant_id | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   |  role_id  | cdf10182-b0e0-4f3c-a47a-ba09a005eb5a |
                   | username  |              username1               |
                   |   email   |           user1@email.com            |
                   | password  |                 asdf                 |
                   |   uuid    | 7e25110d-b9aa-4d03-9540-776e1bf44c2a |
                   |  created  |         2013-06-10 22:52:10          |
                   +-----------+--------------------------------------+
                   Took 6.69842886925 seconds to complete.
```
```
'/delete/role/(.*)'
     example usage:
                   curl http://server.fqdn:9001/delete/role/c6565168-4a8c-439a-ba4e-b4557189d456
                   Took 0.154651165009 seconds to complete.
```
```
'/delete/tenant/(.*)'
     example usage:
                   curl http://server.fqdn:9001/delete/tenant/c6565168-4a8c-439a-ba4e-b4557189d456
                   Took 0.154651165009 seconds to complete.
```
```
'/delete/user/(.*)'
     example usage:
                   curl http://server.fqdn:9001/delete/user/c6565168-4a8c-439a-ba4e-b4557189d456
                   Took 0.154651165009 seconds to complete.
```
```
'/deregister/local-system/(.*)'
     example usage:
                   curl http://server.fqdn:9001/deregister/local-system/c6565168-4a8c-439a-ba4e-b4557189d456
                   Took 0.154651165009 seconds to complete.
```
```
'/deregister/remote-system/(.*)'
     example usage:
                   curl http://server.fqdn:9001/deregister/remote-system/c6565168-4a8c-439a-ba4e-b4557189d456
                   Took 0.154651165009 seconds to complete.
```
```
'/get/role/(.*)'
     example usage:
                   curl http://server.fqdn:9001/get/role/f6df614c-4f5f-4498-8905-57069813e78e
                   +----------+--------------------------------------+
                   | Property |                Value                 |
                   +----------+--------------------------------------+
                   |    id    |                  1                   |
                   |   uuid   | f6df614c-4f5f-4498-8905-57069813e78e |
                   |   name   |                role1                 |
                   | created  |         2013-06-10 21:53:27          |
                   +----------+--------------------------------------+
                   Took 0.0146381855011 seconds to complete.
```
```
'/get/system/(.*)'
     example usage:
                   curl http://server.fqdn:9001/get/system/860caa68-d11f-4f58-9cf4-7ead839ef7fe  
                   +--------------+--------------------------------------+
                   |   Property   |                Value                 |
                   +--------------+--------------------------------------+
                   |      id      |                  1                   |
                   |     uuid     | 860caa68-d11f-4f58-9cf4-7ead839ef7fe |
                   |     name     |               system1                |
                   |  data_type   |                 text                 |
                   | description  |             description1             |
                   |   endpoint   |                 None                 |
                   |   hostname   |              hostname1               |
                   |     port     |                 1234                 |
                   |  remote_uri  |          http://remote.uri/          |
                   |   poc_name   |                name1                 |
                   |  poc_email   |            poc@email.com             |
                   |    remote    |                  1                   |
                   |   created    |         2013-06-10 21:59:20          |
                   | updated_data |                 None                 |
                   +--------------+--------------------------------------+
                   Took 6.94356203079 seconds to complete.
```
```
'/get/tenant/(.*)'
     example usage:
                   curl http://server.fqdn:9001/get/tenant/62b8a809-e868-43ce-8365-cf96ecb8dd8f
                   +----------+--------------------------------------+
                   | Property |                Value                 |
                   +----------+--------------------------------------+
                   |    id    |                  1                   |
                   |   uuid   | 62b8a809-e868-43ce-8365-cf96ecb8dd8f |
                   |   name   |               tenant1                |
                   | created  |         2013-06-10 21:38:07          |
                   +----------+--------------------------------------+
                   Took 0.0149369239807 seconds to complete.
```
```
'/get/user/(.*)'
     example usage:
                   curl http://server.fqdn:9001/get/user/7e25110d-b9aa-4d03-9540-776e1bf44c2a
                   +----------+--------------------------------------+
                   | Property |                Value                 |
                   +----------+--------------------------------------+
                   |    id    |                  1                   |
                   |   uuid   | 7e25110d-b9aa-4d03-9540-776e1bf44c2a |
                   |   name   |                user1                 |
                   | username |              username1               |
                   |  email   |           user1@email.com            |
                   | created  |         2013-06-10 22:52:10          |
                   +----------+--------------------------------------+
                   Took 0.0186581611633 seconds to complete.
```
```
'/list/all'
     example usage:
                   curl http://server.fqdn:9001/list/all (no results)
                   {}
                   Took 0.0129628181458 seconds to complete.

                   curl http://server.fqdn:9001/list/all (one or more results)
                  {
                   "users_tenants": [
                               {
                                    "tenant_id": "602d5b58-cce9-4040-91dd-a2b2f0e954af",
                                    "user_id": "c8e6cbcc-c657-4de9-a02a-c8121f1a11a1"
                               },
                               {
                                    "tenant_id": "602d5b58-cce9-4040-91dd-a2b2f0e954af",
                                    "user_id": "91e7c621-ba88-4f2c-a78e-8f6a8a79105c"
                               }
                    ],
                    "users": [
                               {
                                    "username": "lkberj",
                                    "name": "asdf",
                                    "created": "2013-08-13 23:29:29",
                                    "id": "1",
                                    "email": "asdlkfj@aldskfj.com",
                                    "uuid": "c8e6cbcc-c657-4de9-a02a-c8121f1a11a1"
                               },
                               {
                                    "username": "lkberj",
                                    "name": "asdf",
                                    "created": "2013-08-13 23:44:47",
                                    "id": "2",
                                    "email": "asdlkfj@aldskfj.com",
                                    "uuid": "91e7c621-ba88-4f2c-a78e-8f6a8a79105c"
                               }
                    ],
                    "roles": [
                               {
                                    "created": "2013-08-13 23:25:12",
                                    "id": "1",
                                    "name": "role1",
                                    "uuid": "e39d6ac4-dfc7-46de-b048-7ff4884d3018"
                               },
                               {
                                    "created": "2013-08-13 23:44:19",
                                    "id": "2",
                                    "name": "role2",
                                    "uuid": "c7eb6f3b-9277-46e7-89e3-f3d59ab7e561"
                               }
                    ],
                    "users_roles": [
                               {
                                    "user_id": "c8e6cbcc-c657-4de9-a02a-c8121f1a11a1",
                                    "role_id": "e39d6ac4-dfc7-46de-b048-7ff4884d3018"
                               },
                               {
                                    "user_id": "91e7c621-ba88-4f2c-a78e-8f6a8a79105c",
                                    "role_id": "c7eb6f3b-9277-46e7-89e3-f3d59ab7e561"
                               }
                    ],
                    "systems": [
                               {
                                    "endpoint": "None",
                                    "poc_email": "asdf@alkdfj.com",
                                    "description": "desc",
                                    "data_type": "data",
                                    "created": "2013-08-13 23:27:03",
                                    "hostname": "asdf",
                                    "poc_name": "foo bar",
                                    "uuid": "4991f644-e94d-472e-8526-c7f08a656735",
                                    "port": "123",
                                    "remote": "1",
                                    "remote_uri": "http://localhost/",
                                    "updated_data": "2013-08-19 16:22:19",
                                    "id": "1",
                                    "name": "system4"
                               }
                    ],
                    "tenants": [
                               {
                                    "created": "2013-08-13 23:25:06",
                                    "id": "1",
                                    "name": "tenant1",
                                    "uuid": "602d5b58-cce9-4040-91dd-a2b2f0e954af"
                               },
                               {
                                    "created": "2013-08-13 23:46:50",
                                    "id": "2",
                                    "name": "tenant2",
                                    "uuid": "b92c03bc-ab3f-4994-8148-5d5eb3e7cc65"
                               }
                    ],
                    "systems_tenants": [
                               {
                                    "tenant_id": "602d5b58-cce9-4040-91dd-a2b2f0e954af",
                                    "system_id": "4991f644-e94d-472e-8526-c7f08a656735"
                               }
                    ]
                   }
                   Took 0.0146169662476 seconds to complete.
```
```
'/list/roles'
     example usage:
                   curl http://server.fqdn:9001/list/roles (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0129628181458 seconds to complete.

                   curl http://server.fqdn:9001/list/roles (one or more results)
                   +-------+--------------------------------------+
                   | Name  |                 UUID                 |
                   +-------+--------------------------------------+
                   | role1 | f6df614c-4f5f-4498-8905-57069813e78e |
                   | role2 | 4c2d02ce-3832-4baa-9eb6-30526f99d98c |
                   +-------+--------------------------------------+
                   Took 0.0146169662476 seconds to complete.
```
```
'/list/systems'
     example usage:
                   curl http://server.fqdn:9001/list/systems (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0129628181458 seconds to complete.

                   curl http://server.fqdn:9001/list/systems (one or more results)
                   +---------+--------------------------------------+
                   |  Name   |                 UUID                 |
                   +---------+--------------------------------------+
                   | system1 | 860caa68-d11f-4f58-9cf4-7ead839ef7fe |
                   | system2 | dfa1b604-36da-4089-80fc-7f25b2381355 |
                   +---------+--------------------------------------+
                   Took 0.0143511295319 seconds to complete.
```
```
'/list/tenants'
     example usage:
                   curl http://server.fqdn:9001/list/tenants (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0129628181458 seconds to complete.

                   curl http://server.fqdn:9001/list/tenants (one or more results)
                   +---------+--------------------------------------+
                   |  Name   |                 UUID                 |
                   +---------+--------------------------------------+
                   | tenant1 | 62b8a809-e868-43ce-8365-cf96ecb8dd8f |
                   | tenant2 | 022b54d8-5440-44d2-96b2-09766b8513d8 |
                   +---------+--------------------------------------+
                   Took 0.0141260623932 seconds to complete.
```
```
'/list/users'
     example usage:
                   curl http://server.fqdn:9001/list/users (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0129628181458 seconds to complete.

                   curl http://server.fqdn:9001/list/users (one or more results)
                   +-------+--------------------------------------+
                   | Name  |                 UUID                 |
                   +-------+--------------------------------------+
                   | user1 | 7e25110d-b9aa-4d03-9540-776e1bf44c2a |
                   | user2 | d196cd3f-87af-4187-a5d2-dcd54066fbd5 |
                   +-------+--------------------------------------+
                   Took 0.0138659477234 seconds to complete.
```
```
'/list/role/users/(.*)'
     example usage:
                   curl http://server.fqdn:9001/list/role/users/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0130469799042 seconds to complete.

                   curl http://server.fqdn:9001/list/role/users/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a (one or more results)
                   +--------------------------------------+
                   |                User ID               |
                   +--------------------------------------+
                   | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   | afbd7a79-74a1-4692-9c00-c31f4dd81a9f |
                   +--------------------------------------+
                   Took 0.0118811130524 seconds to complete.
```
```
'/list/system/tenants/(.*)'
     example usage:
                   curl http://server.fqdn:9001/list/system/tenants/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0130469799042 seconds to complete.

                   curl http://server.fqdn:9001/list/system/tenants/59822f6b-4646-4dd8-9be9-038c2988375a (one or more results)
                   +--------------------------------------+
                   |              Tenant ID               |
                   +--------------------------------------+
                   | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   | aa317893-6df2-4af6-88a5-3f395dfb0786 |
                   | afbd7a79-74a1-4692-9c00-c31f4dd81a9f |
                   +--------------------------------------+
                   Took 0.0118811130524 seconds to complete.
```
```
'/list/tenant/systems/(.*)'
     example usage:
                   curl http://server.fqdn:9001/list/tenant/systems/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0130469799042 seconds to complete.

                   curl http://server.fqdn:9001/list/tenant/systems/aa317893-6df2-4af6-88a5-3f395dfb0786 (one or more results)
                   +--------------------------------------+
                   |              System ID               |
                   +--------------------------------------+
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   +--------------------------------------+
                   Took 0.0118811130524 seconds to complete.
```
```
'/list/tenant/users/(.*)'
     example usage:
                   curl http://server.fqdn:9001/list/tenant/users/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0130469799042 seconds to complete.

                   curl http://server.fqdn:9001/list/tenant/users/aa317893-6df2-4af6-88a5-3f395dfb0786 (one or more results)
                   +--------------------------------------+
                   |                User ID               |
                   +--------------------------------------+
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   +--------------------------------------+
                   Took 0.0118811130524 seconds to complete.
```
```
'/list/user/roles/(.*)'
     example usage:
                   curl http://server.fqdn:9001/list/user/roles/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0130469799042 seconds to complete.

                   curl http://server.fqdn:9001/list/user/roles/aa317893-6df2-4af6-88a5-3f395dfb0786 (one or more results)
                   +--------------------------------------+
                   |                Role ID               |
                   +--------------------------------------+
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   +--------------------------------------+
                   Took 0.0118811130524 seconds to complete.
```
```
'/list/user/tenants/(.*)'
     example usage:
                   curl http://server.fqdn:9001/list/user/tenants/cdf10182-b0e0-4f3c-a47a-ba09a005eb5a (no results)
                   +----------+-------+
                   | Property | Value |
                   +----------+-------+
                   +----------+-------+
                   Took 0.0130469799042 seconds to complete.

                   curl http://server.fqdn:9001/list/user/tenants/aa317893-6df2-4af6-88a5-3f395dfb0786 (one or more results)
                   +--------------------------------------+
                   |              Tenant ID               |
                   +--------------------------------------+
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   | 59822f6b-4646-4dd8-9be9-038c2988375a |
                   +--------------------------------------+
                   Took 0.0118811130524 seconds to complete.
```
```
'/register/local-system'
     example usage:
                   curl -i -H "Content-Type: application/json" -X POST -d '{"name" :"system2", "data_type" :"text", "description" :"description1", "tenant_id" :"afbd7a79-74a1-4692-9c00-c31f4dd81a9f", "hostname" :"hostname1", "endpoint" :"http://hemlock.uri/", "poc_name":"name1","poc_email" :"poc@email.com"}' http://server.fqdn:9001/register/local-system
                   +-------------+--------------------------------------+
                   |  Property   |                Value                 |
                   +-------------+--------------------------------------+
                   |  tenant_id  | afbd7a79-74a1-4692-9c00-c31f4dd81a9f |
                   |  data_type  |                 text                 |
                   |  hostname   |              hostname1               |
                   |  poc_name   |                name1                 |
                   | description |             description1             |
                   |    name     |               system2                |
                   |  poc_email  |            poc@email.com             |
                   |  endpoint   |         http://hemlock.uri/          |
                   |    uuid     | d3462370-20d3-458d-9e1e-c58de39ececf |
                   |   created   |         2013-06-13 16:24:42          |
                   |   remote    |                  0                   |
                   +-------------+--------------------------------------+
                   Took 0.0981459617615 seconds to complete.
```
```
'/register/remote-system'
     example usage:
                   curl -i -H "Content-Type: application/json" -X POST -d '{"name" :"system1", "data_type" :"text", "description" :"description1", "tenant_id" :"62b8a809-e868-43ce-8365-cf96ecb8dd8f", "hostname" :"hostname1", "port" :"1234", "remote_uri" :"http://remote.uri/", "poc_name":"name1","poc_email" :"poc@email.com"}' http://server.fqdn:9001/register/remote-system
                   +-------------+--------------------------------------+
                   |  Property   |                Value                 |
                   +-------------+--------------------------------------+
                   |  tenant_id  | 62b8a809-e868-43ce-8365-cf96ecb8dd8f |
                   |  data_type  |                 text                 |
                   |  hostname   |              hostname1               |
                   |  poc_name   |                name1                 |
                   |    port     |                 1234                 |
                   | description |             description1             |
                   | remote_uri  |          http://remote.uri/          |
                   |    name     |               system1                |
                   |  poc_email  |            poc@email.com             |
                   |    uuid     | 860caa68-d11f-4f58-9cf4-7ead839ef7fe |
                   |   created   |         2013-06-10 21:59:20          |
                   |   remote    |                  1                   |
                   +-------------+--------------------------------------+
                   Took 12.7739210129 seconds to complete.
```
```
'/remove/system/(.*)/tenant/(.*)'
     example usage:
                   curl http://server.fqdn:9001/remove/system/c6565168-4a8c-439a-ba4e-b4557189d456/tenant/860caa68-d11f-4f58-9cf4-7ead839ef7fe
                   Took 0.154651165009 seconds to complete.
```
```
'/remove/user/(.*)/role/(.*)'
     example usage:
                   curl http://server.fqdn:9001/remove/user/c6565168-4a8c-439a-ba4e-b4557189d456/role/860caa68-d11f-4f58-9cf4-7ead839ef7fe
                   Took 0.154651165009 seconds to complete.
```
```
'/remove/user/(.*)/tenant/(.*)'
     example usage:
                   curl http://server.fqdn:9001/remove/user/c6565168-4a8c-439a-ba4e-b4557189d456/tenant/860caa68-d11f-4f58-9cf4-7ead839ef7fe
                   Took 0.154651165009 seconds to complete.
```
```
bad urls will return 'not found'
```
