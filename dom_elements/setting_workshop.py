```python
class SettingWorkshop:
    def __init__(self):
        self.id = 'setting_workshop'
        self.campaign_settings = None
        self.npc_list = None
        self.story_arcs = None
        self.adventures = None
        self.npc_roles = None
        self.npc_objectives = None
        self.npc_relationships = None
        self.timeline_events = None
        self.player_actions = None
        self.prebuilt_modules = None

    def load_campaign_settings(self, campaign_settings):
        self.campaign_settings = campaign_settings

    def load_npc_list(self, npc_list):
        self.npc_list = npc_list

    def load_story_arcs(self, story_arcs):
        self.story_arcs = story_arcs

    def load_adventures(self, adventures):
        self.adventures = adventures

    def load_npc_roles(self, npc_roles):
        self.npc_roles = npc_roles

    def load_npc_objectives(self, npc_objectives):
        self.npc_objectives = npc_objectives

    def load_npc_relationships(self, npc_relationships):
        self.npc_relationships = npc_relationships

    def load_timeline_events(self, timeline_events):
        self.timeline_events = timeline_events

    def load_player_actions(self, player_actions):
        self.player_actions = player_actions

    def load_prebuilt_modules(self, prebuilt_modules):
        self.prebuilt_modules = prebuilt_modules
```