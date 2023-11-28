```python
import json
from .utils import send_message
from .assets import npc_roles, npc_objectives, npc_relationships

campaign_settings = {}
npc_list = []
story_arcs = []
adventures = []

def load_campaign(campaign_data):
    global campaign_settings, npc_list, story_arcs, adventures
    campaign_settings = json.loads(campaign_data['settings'])
    npc_list = json.loads(campaign_data['npcs'])
    story_arcs = json.loads(campaign_data['story_arcs'])
    adventures = json.loads(campaign_data['adventures'])

def link_elements():
    for npc in npc_list:
        npc['role'] = npc_roles.get(npc['role_id'])
        npc['objective'] = npc_objectives.get(npc['objective_id'])
        npc['relationships'] = [npc_relationships.get(rel_id) for rel_id in npc['relationship_ids']]

    for arc in story_arcs:
        arc['adventures'] = [adventures.get(adventure_id) for adventure_id in arc['adventure_ids']]

def populate_world():
    for npc in npc_list:
        send_message('NPCCreated', npc)
    for arc in story_arcs:
        send_message('StoryArcCreated', arc)

def orchestrate_campaign(campaign_data):
    load_campaign(campaign_data)
    link_elements()
    populate_world()
```