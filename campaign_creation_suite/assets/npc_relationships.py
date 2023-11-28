```python
from campaign_creation_suite.utils import RelationshipSchema

npc_relationships = []

def establishRelationship(npc1, npc2, relationship_type):
    relationship = RelationshipSchema(npc1=npc1, npc2=npc2, relationship_type=relationship_type)
    npc_relationships.append(relationship)
    return relationship

def getRelationships(npc):
    return [relationship for relationship in npc_relationships if relationship.npc1 == npc or relationship.npc2 == npc]

def removeRelationship(relationship):
    if relationship in npc_relationships:
        npc_relationships.remove(relationship)
```