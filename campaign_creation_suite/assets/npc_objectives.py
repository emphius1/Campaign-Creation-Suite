```python
class ObjectiveSchema:
    def __init__(self, objective_id, objective_name, objective_description):
        self.objective_id = objective_id
        self.objective_name = objective_name
        self.objective_description = objective_description

npc_objectives = []

def defineObjective(objective_id, objective_name, objective_description):
    new_objective = ObjectiveSchema(objective_id, objective_name, objective_description)
    npc_objectives.append(new_objective)
    return new_objective

def getObjective(objective_id):
    for objective in npc_objectives:
        if objective.objective_id == objective_id:
            return objective
    return None

def updateObjective(objective_id, objective_name=None, objective_description=None):
    objective = getObjective(objective_id)
    if objective:
        if objective_name:
            objective.objective_name = objective_name
        if objective_description:
            objective.objective_description = objective_description
        return True
    return False

def deleteObjective(objective_id):
    global npc_objectives
    npc_objectives = [objective for objective in npc_objectives if objective.objective_id != objective_id]
```