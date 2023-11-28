```python
from dataclasses import dataclass

@dataclass
class PlayerAction:
    action_id: str
    action_description: str
    action_consequence: str
    action_timestamp: str

player_actions = []

def performPlayerAction(action_id, action_description, action_consequence, action_timestamp):
    new_action = PlayerAction(action_id, action_description, action_consequence, action_timestamp)
    player_actions.append(new_action)
    return new_action
```