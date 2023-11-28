```python
# Importing required schemas
from schemas.RoleSchema import RoleSchema

# npc_roles list to store all NPC roles
npc_roles = []

def add_role(role):
    """
    Function to add a new role to the npc_roles list
    """
    new_role = RoleSchema(role)
    npc_roles.append(new_role)
    return new_role

def get_role(role_name):
    """
    Function to get a role from the npc_roles list
    """
    for role in npc_roles:
        if role.name == role_name:
            return role
    return None

def remove_role(role_name):
    """
    Function to remove a role from the npc_roles list
    """
    for role in npc_roles:
        if role.name == role_name:
            npc_roles.remove(role)
            return True
    return False
```