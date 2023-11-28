```python
from campaign_creation_suite.utils import AdventureSchema

adventures = []

def createAdventure(adventure_data):
    """
    Function to create a new adventure.
    """
    adventure = AdventureSchema(**adventure_data)
    adventures.append(adventure)
    return adventure

def getAdventure(adventure_id):
    """
    Function to get an adventure by its ID.
    """
    for adventure in adventures:
        if adventure.id == adventure_id:
            return adventure
    return None

def updateAdventure(adventure_id, updated_data):
    """
    Function to update an existing adventure.
    """
    adventure = getAdventure(adventure_id)
    if adventure:
        for key, value in updated_data.items():
            if hasattr(adventure, key):
                setattr(adventure, key, value)
        return adventure
    return None

def deleteAdventure(adventure_id):
    """
    Function to delete an adventure.
    """
    adventure = getAdventure(adventure_id)
    if adventure:
        adventures.remove(adventure)
        return True
    return False
```