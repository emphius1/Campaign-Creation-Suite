```python
from marshmallow import Schema, fields

class NPCSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    role = fields.Str(required=True)
    objective = fields.Str(required=True)
    relationship = fields.Str(required=True)
    campaign_id = fields.Int(required=True)
```