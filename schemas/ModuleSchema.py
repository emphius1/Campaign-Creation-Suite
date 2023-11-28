```python
from marshmallow import Schema, fields

class ModuleSchema(Schema):
    campaign_settings = fields.Nested('CampaignSchema', many=True)
    npc_list = fields.Nested('NPCSchema', many=True)
    story_arcs = fields.Nested('StoryArcSchema', many=True)
    adventures = fields.Nested('AdventureSchema', many=True)
    npc_roles = fields.Nested('RoleSchema', many=True)
    npc_objectives = fields.Nested('ObjectiveSchema', many=True)
    npc_relationships = fields.Nested('RelationshipSchema', many=True)
    timeline_events = fields.Nested('TimelineEventSchema', many=True)
    player_actions = fields.Nested('PlayerActionSchema', many=True)
    prebuilt_modules = fields.List(fields.String(), required=True)
```