```python
import json
from .utils import PlayerActionSchema, CampaignSchema

class ButterflyEffectEngine:
    def __init__(self):
        self.player_actions = []
        self.campaign_settings = {}

    def load_campaign(self, campaign_file):
        with open(campaign_file, 'r') as file:
            self.campaign_settings = json.load(file, cls=CampaignSchema)

    def log_player_action(self, player_action):
        validated_action = PlayerActionSchema().load(player_action)
        self.player_actions.append(validated_action)
        self.update_campaign()

    def update_campaign(self):
        for action in self.player_actions:
            if action['type'] == 'NPC_INTERACTION':
                self.update_npc(action)
            elif action['type'] == 'ENVIRONMENT_CHANGE':
                self.update_environment(action)
            elif action['type'] == 'STORY_PROGRESS':
                self.update_story(action)

    def update_npc(self, action):
        affected_npc = next((npc for npc in self.campaign_settings['npc_list'] if npc['id'] == action['npc_id']), None)
        if affected_npc:
            affected_npc['status'] = action['new_status']

    def update_environment(self, action):
        affected_location = next((loc for loc in self.campaign_settings['locations'] if loc['id'] == action['location_id']), None)
        if affected_location:
            affected_location['status'] = action['new_status']

    def update_story(self, action):
        affected_story_arc = next((arc for arc in self.campaign_settings['story_arcs'] if arc['id'] == action['story_arc_id']), None)
        if affected_story_arc:
            affected_story_arc['status'] = action['new_status']

    def save_campaign(self, campaign_file):
        with open(campaign_file, 'w') as file:
            json.dump(self.campaign_settings, file, cls=CampaignSchema)
```