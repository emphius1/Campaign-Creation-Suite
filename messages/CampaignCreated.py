```python
class CampaignCreated:
    def __init__(self, campaign_data):
        self.name = campaign_data.get('name')
        self.description = campaign_data.get('description')
        self.campaign_settings = campaign_data.get('campaign_settings')

    def display_message(self):
        print(f"Campaign '{self.name}' has been created with the following settings: {self.campaign_settings}")
```