```python
from shared_dependencies.data_schemas import ObjectiveSchema
from shared_dependencies.exported_variables import npc_objectives

def defineObjective(objective_data):
    new_objective = ObjectiveSchema(**objective_data)
    npc_objectives.append(new_objective)
    return new_objective
```