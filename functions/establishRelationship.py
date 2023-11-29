```python
from shared_dependencies.data_schemas import RelationshipSchema
from shared_dependencies.exported_variables import npc_relationships

def establishRelationship(npc1, npc2, relationship_type):
    new_relationship = RelationshipSchema(npc1=npc1, npc2=npc2, relationship_type=relationship_type)
    npc_relationships.append(new_relationship)
    return new_relationship
```