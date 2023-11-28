```python
from marshmallow import Schema, fields

class StoryArcSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    npcs_involved = fields.List(fields.Nested('NPCSchema'), required=True)
    related_adventures = fields.List(fields.Nested('AdventureSchema'), required=True)
    timeline_events = fields.List(fields.Nested('TimelineEventSchema'), required=True)
```