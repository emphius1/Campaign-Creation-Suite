```python
from schemas.NPCSchema import NPCSchema
from shared_dependencies.exported_variables import npc_list
from messages.NPCCreated import NPCCreated

def createNPC(npc_data):
    new_npc = NPCSchema(**npc_data)
    npc_list.append(new_npc)
    NPCCreated(new_npc)
    return new_npc
```