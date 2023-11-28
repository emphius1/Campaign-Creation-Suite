```python
import random
from .utils import CampaignSchema

campaign_settings = []

def createCampaign(template_type="random"):
    if template_type == "random":
        campaign = generateRandomCampaign()
    elif template_type == "custom":
        campaign = generateCustomCampaign()
    elif template_type == "preset":
        campaign = generatePresetCampaign()
    else:
        raise ValueError("Invalid template type. Choose from 'random', 'custom', or 'preset'.")

    campaign_settings.append(campaign)
    return campaign

def generateRandomCampaign():
    campaign = CampaignSchema(
        lore = generateLore(),
        locations = generateLocations(),
        deities = generateDeities(),
        other_elements = generateOtherElements()
    )
    return campaign

def generateCustomCampaign():
    # This function will interact with the user interface to gather user inputs
    # For the sake of this example, we will return a placeholder campaign
    campaign = CampaignSchema(
        lore = "Custom Lore",
        locations = ["Custom Location 1", "Custom Location 2"],
        deities = ["Custom Deity 1", "Custom Deity 2"],
        other_elements = ["Custom Element 1", "Custom Element 2"]
    )
    return campaign

def generatePresetCampaign():
    # This function will load a preset campaign from the database
    # For the sake of this example, we will return a placeholder campaign
    campaign = CampaignSchema(
        lore = "Preset Lore",
        locations = ["Preset Location 1", "Preset Location 2"],
        deities = ["Preset Deity 1", "Preset Deity 2"],
        other_elements = ["Preset Element 1", "Preset Element 2"]
    )
    return campaign

def generateLore():
    # This function will generate random lore
    return "Random Lore"

def generateLocations():
    # This function will generate random locations
    return ["Random Location 1", "Random Location 2"]

def generateDeities():
    # This function will generate random deities
    return ["Random Deity 1", "Random Deity 2"]

def generateOtherElements():
    # This function will generate other random elements
    return ["Random Element 1", "Random Element 2"]
```