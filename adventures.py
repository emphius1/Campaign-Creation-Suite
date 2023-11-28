```python
from shared_dependencies.data_schemas import AdventureSchema
from shared_dependencies.message_names import AdventureCreated
from shared_dependencies.function_names import createAdventure

adventures = []

def add_adventure(adventure_data):
    new_adventure = AdventureSchema(**adventure_data)
    adventures.append(new_adventure)
    print(AdventureCreated.format(new_adventure.name))

def get_adventure(adventure_name):
    for adventure in adventures:
        if adventure.name == adventure_name:
            return adventure
    return None

def remove_adventure(adventure_name):
    adventure = get_adventure(adventure_name)
    if adventure:
        adventures.remove(adventure)
        print('Adventure {} removed.'.format(adventure_name))
    else:
        print('Adventure {} not found.'.format(adventure_name))

def update_adventure(adventure_name, updated_data):
    adventure = get_adventure(adventure_name)
    if adventure:
        for key, value in updated_data.items():
            setattr(adventure, key, value)
        print('Adventure {} updated.'.format(adventure_name))
    else:
        print('Adventure {} not found.'.format(adventure_name))

def list_adventures():
    for adventure in adventures:
        print(adventure.name)
```