```python
from marshmallow import Schema, fields

class RoleSchema(Schema):
    role_id = fields.Int(required=True)
    role_name = fields.Str(required=True)
    role_description = fields.Str(required=True)
    associated_npc = fields.List(fields.Int(), required=True)
```