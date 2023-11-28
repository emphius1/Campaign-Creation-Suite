```python
from campaign_creation_suite.utils import ModuleSchema

prebuilt_modules = []

class PrebuiltModule:
    def __init__(self, name, description, content):
        self.name = name
        self.description = description
        self.content = content

    def to_dict(self):
        return ModuleSchema().dump(self)

def importModule(module):
    prebuilt_modules.append(module)
    return module

# Sample prebuilt modules
sample_module_1 = PrebuiltModule(
    name="The Dragon's Lair",
    description="A high-level adventure module featuring a fearsome dragon.",
    content={
        "npcs": ["Dragon", "Captive Princess", "Village Elder"],
        "locations": ["Dragon's Lair", "Village", "Forest"],
        "events": ["Dragon Attack", "Rescue Mission", "Victory Feast"]
    }
)

sample_module_2 = PrebuiltModule(
    name="The Lost City",
    description="An exploration module set in a long-lost city swallowed by the jungle.",
    content={
        "npcs": ["Guide", "Ghost King", "Jungle Creatures"],
        "locations": ["Jungle", "Lost City", "Ghost King's Palace"],
        "events": ["City Discovery", "Ghost King's Curse", "Lifting the Curse"]
    }
)

# Import the sample modules
importModule(sample_module_1.to_dict())
importModule(sample_module_2.to_dict())
```