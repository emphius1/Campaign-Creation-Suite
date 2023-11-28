```python
from marshmallow import Schema, fields

class CampaignSchema(Schema):
    campaign_id = fields.Str(required=True)
    campaign_name = fields.Str(required=True)
    campaign_settings = fields.Nested('CampaignSettingsSchema', many=True)
    npc_list = fields.Nested('NPCSchema', many=True)
    story_arcs = fields.Nested('StoryArcSchema', many=True)
    adventures = fields.Nested('AdventureSchema', many=True)
    npc_roles = fields.Nested('RoleSchema', many=True)
    npc_objectives = fields.Nested('ObjectiveSchema', many=True)
    npc_relationships = fields.Nested('RelationshipSchema', many=True)
    timeline_events = fields.Nested('TimelineEventSchema', many=True)
    player_actions = fields.Nested('PlayerActionSchema', many=True)
    prebuilt_modules = fields.Nested('ModuleSchema', many=True)
```