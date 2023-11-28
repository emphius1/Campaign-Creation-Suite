```python
from shared_dependencies.data_schemas import RoleSchema
from shared_dependencies.exported_variables import npc_roles

def defineRole(role_name, role_description):
    new_role = RoleSchema(role_name, role_description)
    npc_roles.append(new_role)
    return new_role
```