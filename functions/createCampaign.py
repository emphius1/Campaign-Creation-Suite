```python
from schemas.CampaignSchema import CampaignSchema
from shared_dependencies.exported_variables import campaign_settings
from messages.CampaignCreated import CampaignCreated

def createCampaign(name, description, setting):
    new_campaign = CampaignSchema(name, description, setting)
    campaign_settings.append(new_campaign)
    CampaignCreated(new_campaign)
```