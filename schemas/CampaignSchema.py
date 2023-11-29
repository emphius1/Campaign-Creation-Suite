```python
from marshmallow import Schema, fields

class CampaignSchema(Schema):
    campaign_settings = fields.Dict()
    npc_list = fields.List(fields.Nested('NPCSchema'))
    story_arcs = fields.List(fields.Nested('StoryArcSchema'))
    adventures = fields.List(fields.Nested('AdventureSchema'))
    npc_roles = fields.List(fields.Nested('RoleSchema'))
    npc_objectives = fields.List(fields.Nested('ObjectiveSchema'))
    npc_relationships = fields.List(fields.Nested('RelationshipSchema'))
    timeline_events = fields.List(fields.Nested('TimelineEventSchema'))
    player_actions = fields.List(fields.Nested('PlayerActionSchema'))
    prebuilt_modules = fields.List(fields.Nested('ModuleSchema'))
```