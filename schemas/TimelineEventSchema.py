```python
from marshmallow import Schema, fields

class TimelineEventSchema(Schema):
    event_id = fields.Int(required=True)
    event_name = fields.Str(required=True)
    event_description = fields.Str(required=True)
    event_time = fields.DateTime(required=True)
    related_npc = fields.Nested('NPCSchema', many=True)
    related_story_arc = fields.Nested('StoryArcSchema')
    related_adventure = fields.Nested('AdventureSchema')
    player_actions = fields.Nested('PlayerActionSchema', many=True)
```