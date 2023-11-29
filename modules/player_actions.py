```python
from schemas.PlayerActionSchema import PlayerActionSchema

player_actions = []

def add_player_action(action):
    player_action = PlayerActionSchema(action)
    player_actions.append(player_action)

def get_player_actions():
    return player_actions

def remove_player_action(action_id):
    global player_actions
    player_actions = [action for action in player_actions if action.id != action_id]
```