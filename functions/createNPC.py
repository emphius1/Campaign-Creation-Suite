```python
from shared_dependencies.data_schemas import NPCSchema
from shared_dependencies.exported_variables import npc_list
from shared_dependencies.message_names import NPCCreated

def createNPC(npc_data):
    new_npc = NPCSchema(**npc_data)
    npc_list.append(new_npc)
    print(NPCCreated.format(new_npc.name))
    return new_npc
```