```python
from shared_dependencies.exported_variables import campaign_settings, npc_list, story_arcs, adventures, npc_roles, npc_objectives, npc_relationships
from shared_dependencies.data_schemas import CampaignSchema, NPCSchema, StoryArcSchema, AdventureSchema, RoleSchema, ObjectiveSchema, RelationshipSchema
from shared_dependencies.message_names import CampaignCreated, NPCCreated, StoryArcCreated, AdventureCreated, RoleDefined, ObjectiveDefined, RelationshipEstablished

class CampaignOrchestrator:
    def __init__(self):
        self.campaign = None
        self.npcs = []
        self.story_arcs = []
        self.adventures = []
        self.roles = []
        self.objectives = []
        self.relationships = []

    def create_campaign(self, campaign_data):
        self.campaign = CampaignSchema(**campaign_data)
        campaign_settings.append(self.campaign)
        print(CampaignCreated)

    def create_npc(self, npc_data):
        npc = NPCSchema(**npc_data)
        self.npcs.append(npc)
        npc_list.append(npc)
        print(NPCCreated)

    def create_story_arc(self, story_arc_data):
        story_arc = StoryArcSchema(**story_arc_data)
        self.story_arcs.append(story_arc)
        story_arcs.append(story_arc)
        print(StoryArcCreated)

    def create_adventure(self, adventure_data):
        adventure = AdventureSchema(**adventure_data)
        self.adventures.append(adventure)
        adventures.append(adventure)
        print(AdventureCreated)

    def define_role(self, role_data):
        role = RoleSchema(**role_data)
        self.roles.append(role)
        npc_roles.append(role)
        print(RoleDefined)

    def define_objective(self, objective_data):
        objective = ObjectiveSchema(**objective_data)
        self.objectives.append(objective)
        npc_objectives.append(objective)
        print(ObjectiveDefined)

    def establish_relationship(self, relationship_data):
        relationship = RelationshipSchema(**relationship_data)
        self.relationships.append(relationship)
        npc_relationships.append(relationship)
        print(RelationshipEstablished)
```