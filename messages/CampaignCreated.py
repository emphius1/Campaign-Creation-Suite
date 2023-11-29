class CampaignCreated:
    def __init__(self, campaign):
        self.campaign = campaign

    def __str__(self):
        return f"Campaign '{self.campaign['name']}' has been successfully created."