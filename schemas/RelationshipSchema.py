```python
from marshmallow import Schema, fields

class RelationshipSchema(Schema):
    npc1 = fields.Str(required=True)
    npc2 = fields.Str(required=True)
    relationship_type = fields.Str(required=True)
    relationship_details = fields.Str(required=True)
```