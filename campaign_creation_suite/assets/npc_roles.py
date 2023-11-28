```python
class RoleSchema:
    def __init__(self, role_name, role_description):
        self.role_name = role_name
        self.role_description = role_description

npc_roles = []

def defineRole(role_name, role_description):
    new_role = RoleSchema(role_name, role_description)
    npc_roles.append(new_role)
    return new_role

def getRole(role_name):
    for role in npc_roles:
        if role.role_name == role_name:
            return role
    return None

def getAllRoles():
    return npc_roles

def deleteRole(role_name):
    global npc_roles
    npc_roles = [role for role in npc_roles if role.role_name != role_name]
```