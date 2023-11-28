```python
from marshmallow import Schema, fields

class CampaignSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    settings = fields.Dict(required=True)

class NPCSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    attributes = fields.Dict(required=True)
    depth = fields.Dict(required=True)

class StoryArcSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    plot_points = fields.List(fields.Str(), required=True)

class AdventureSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    story_arc_id = fields.Int(required=True)

class RoleSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    npc_id = fields.Int(required=True)

class ObjectiveSchema(Schema):
    id = fields.Int(required=True)
    description = fields.Str(required=True)
    npc_id = fields.Int(required=True)

class RelationshipSchema(Schema):
    id = fields.Int(required=True)
    npc_id_1 = fields.Int(required=True)
    npc_id_2 = fields.Int(required=True)
    relationship_type = fields.Str(required=True)

class TimelineEventSchema(Schema):
    id = fields.Int(required=True)
    description = fields.Str(required=True)
    campaign_id = fields.Int(required=True)

class PlayerActionSchema(Schema):
    id = fields.Int(required=True)
    description = fields.Str(required=True)
    campaign_id = fields.Int(required=True)

class ModuleSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    content = fields.Dict(required=True)
```