```python
from schemas.RelationshipSchema import RelationshipSchema

npc_relationships = []

def establishRelationship(npc1, npc2, relationship_type):
    relationship = RelationshipSchema(npc1, npc2, relationship_type)
    npc_relationships.append(relationship)
    return relationship
```