```python
from schemas.RoleSchema import RoleSchema

npc_roles = []

def add_role(role):
    new_role = RoleSchema(role)
    npc_roles.append(new_role)
    return new_role

def get_role(role_id):
    for role in npc_roles:
        if role.id == role_id:
            return role
    return None

def remove_role(role_id):
    for role in npc_roles:
        if role.id == role_id:
            npc_roles.remove(role)
            return True
    return False
```