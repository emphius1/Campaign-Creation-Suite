```python
from schemas.NPCSchema import NPCSchema

npc_list = []

def add_npc(npc_data):
    npc = NPCSchema(**npc_data)
    npc_list.append(npc)

def get_npc(npc_id):
    for npc in npc_list:
        if npc.id == npc_id:
            return npc
    return None

def remove_npc(npc_id):
    global npc_list
    npc_list = [npc for npc in npc_list if npc.id != npc_id]

def update_npc(npc_id, updated_data):
    for npc in npc_list:
        if npc.id == npc_id:
            npc.update(**updated_data)
            return npc
    return None
```