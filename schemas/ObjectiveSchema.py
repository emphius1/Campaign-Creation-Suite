```python
from marshmallow import Schema, fields

class ObjectiveSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    npc_id = fields.Int(required=True)
    status = fields.Str(required=True)
```