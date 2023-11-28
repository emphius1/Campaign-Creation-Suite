```python
from schemas.ObjectiveSchema import ObjectiveSchema

npc_objectives = []

def add_objective(npc_id, objective):
    new_objective = ObjectiveSchema(npc_id, objective)
    npc_objectives.append(new_objective)

def get_objectives(npc_id):
    return [objective for objective in npc_objectives if objective.npc_id == npc_id]

def remove_objective(npc_id, objective_id):
    global npc_objectives
    npc_objectives = [objective for objective in npc_objectives if not (objective.npc_id == npc_id and objective.id == objective_id)]
```