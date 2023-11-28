```python
from shared_dependencies.data_schemas import PlayerActionSchema
from shared_dependencies.exported_variables import player_actions

def performPlayerAction(action_data):
    action = PlayerActionSchema(**action_data)
    player_actions.append(action)
    return {"message": "PlayerActionPerformed", "action": action}
```