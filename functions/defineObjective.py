```python
from shared_dependencies.data_schemas import ObjectiveSchema
from shared_dependencies.exported_variables import npc_objectives

def defineObjective(npc_id, objective):
    new_objective = ObjectiveSchema(npc_id=npc_id, objective=objective)
    npc_objectives.append(new_objective)
    return new_objective
```