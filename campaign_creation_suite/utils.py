```python
import json
from campaign_creation_suite.assets import *

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_campaign_data():
    return load_json('campaign_settings.json')

def save_campaign_data(campaign_settings):
    save_json(campaign_settings, 'campaign_settings.json')

def load_npc_data():
    return load_json('npc_list.json')

def save_npc_data(npc_list):
    save_json(npc_list, 'npc_list.json')

def load_story_arc_data():
    return load_json('story_arcs.json')

def save_story_arc_data(story_arcs):
    save_json(story_arcs, 'story_arcs.json')

def load_adventure_data():
    return load_json('adventures.json')

def save_adventure_data(adventures):
    save_json(adventures, 'adventures.json')

def load_npc_roles_data():
    return load_json('npc_roles.json')

def save_npc_roles_data(npc_roles):
    save_json(npc_roles, 'npc_roles.json')

def load_npc_objectives_data():
    return load_json('npc_objectives.json')

def save_npc_objectives_data(npc_objectives):
    save_json(npc_objectives, 'npc_objectives.json')

def load_npc_relationships_data():
    return load_json('npc_relationships.json')

def save_npc_relationships_data(npc_relationships):
    save_json(npc_relationships, 'npc_relationships.json')

def load_timeline_events_data():
    return load_json('timeline_events.json')

def save_timeline_events_data(timeline_events):
    save_json(timeline_events, 'timeline_events.json')

def load_player_actions_data():
    return load_json('player_actions.json')

def save_player_actions_data(player_actions):
    save_json(player_actions, 'player_actions.json')

def load_prebuilt_modules_data():
    return load_json('prebuilt_modules.json')

def save_prebuilt_modules_data(prebuilt_modules):
    save_json(prebuilt_modules, 'prebuilt_modules.json')
```