```python
from marshmallow import Schema, fields

class AdventureSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    objectives = fields.List(fields.Nested('ObjectiveSchema'), required=True)
    npcs = fields.List(fields.Nested('NPCSchema'), required=True)
    timeline_events = fields.List(fields.Nested('TimelineEventSchema'), required=True)
    player_actions = fields.List(fields.Nested('PlayerActionSchema'), required=True)
```