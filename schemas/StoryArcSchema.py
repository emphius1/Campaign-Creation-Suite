```python
from marshmallow import Schema, fields

class StoryArcSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    npcs_involved = fields.List(fields.Int(), required=True)
    related_adventures = fields.List(fields.Int(), required=True)
    timeline_events = fields.List(fields.Int(), required=True)
```