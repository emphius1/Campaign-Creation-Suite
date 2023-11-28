```python
from marshmallow import Schema, fields

class PlayerActionSchema(Schema):
    action_id = fields.Str(required=True)
    player_id = fields.Str(required=True)
    action_type = fields.Str(required=True)
    action_details = fields.Dict(required=True)
    timestamp = fields.DateTime(required=True)
```