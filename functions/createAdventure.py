```python
from shared_dependencies.data_schemas import AdventureSchema
from shared_dependencies.exported_variables import adventures

def createAdventure(adventure_data):
    new_adventure = AdventureSchema(**adventure_data)
    adventures.append(new_adventure)
    return new_adventure
```