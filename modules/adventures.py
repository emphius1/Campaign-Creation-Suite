```python
from schemas.AdventureSchema import AdventureSchema

adventures = []

def createAdventure(adventure_data):
    new_adventure = AdventureSchema(**adventure_data)
    adventures.append(new_adventure)
    return new_adventure
```