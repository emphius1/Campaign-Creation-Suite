```python
from schemas.PlayerActionSchema import PlayerActionSchema
from messages.PlayerActionPerformed import PlayerActionPerformed

def performPlayerAction(action_data):
    action = PlayerActionSchema(**action_data)
    player_actions.append(action)
    PlayerActionPerformed.emit(action)
    return action
```