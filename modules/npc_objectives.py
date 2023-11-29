```python
from schemas.ObjectiveSchema import ObjectiveSchema

npc_objectives = []

def defineObjective(npc_id, objective):
    new_objective = ObjectiveSchema(npc_id, objective)
    npc_objectives.append(new_objective)
    return new_objective
```