```python
from shared_dependencies.data_schemas import PlayerActionSchema
from shared_dependencies.message_names import PlayerActionPerformed
from shared_dependencies.function_names import performPlayerAction

player_actions = []

def add_player_action(action_data):
    action = PlayerActionSchema(**action_data)
    player_actions.append(action)
    performPlayerAction(action)
    print(PlayerActionPerformed, action)

def get_player_actions():
    return player_actions
```