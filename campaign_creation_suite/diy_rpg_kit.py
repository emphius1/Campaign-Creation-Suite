```python
from shared_dependencies.data_schemas import CampaignSchema
from shared_dependencies.exported_variables import campaign_settings
from shared_dependencies.message_names import CampaignCreated
from shared_dependencies.function_names import createCampaign

class DIYRPGKit:
    def __init__(self):
        self.dom_element_id = 'diy_rpg_kit'
        self.campaign_schema = CampaignSchema()
        self.campaign_settings = campaign_settings

    def create_campaign(self, terrain, climate, major_events, character_development):
        new_campaign = self.campaign_schema.create(terrain, climate, major_events, character_development)
        self.campaign_settings.append(new_campaign)
        self.send_message(CampaignCreated, new_campaign)
        return new_campaign

    def adjust_parameters(self, campaign, terrain=None, climate=None, major_events=None, character_development=None):
        if terrain:
            campaign['terrain'] = terrain
        if climate:
            campaign['climate'] = climate
        if major_events:
            campaign['major_events'] = major_events
        if character_development:
            campaign['character_development'] = character_development
        self.send_message(CampaignCreated, campaign)
        return campaign

    def send_message(self, message_name, data):
        # This function will send a message to other components of the application.
        # The implementation of this function depends on the specific messaging system used in the application.
        pass

diy_rpg_kit = DIYRPGKit()
```