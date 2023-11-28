```python
from shared_dependencies.data_schemas import NPCSchema

npc_list = []

def add_npc(npc_data):
    npc = NPCSchema(**npc_data)
    npc_list.append(npc)
    return npc

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
            for key, value in updated_data.items():
                setattr(npc, key, value)
            return npc
    return None
```