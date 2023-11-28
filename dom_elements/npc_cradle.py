```python
from shared_dependencies.exported_variables import npc_list
from shared_dependencies.data_schemas import NPCSchema
from shared_dependencies.message_names import NPCCreated
from shared_dependencies.function_names import createNPC

class NPCCradle:
    def __init__(self):
        self.element_id = "npc_cradle"
        self.npc_list = npc_list

    def create_npc(self, npc_data):
        new_npc = createNPC(npc_data, NPCSchema)
        self.npc_list.append(new_npc)
        self.send_message(NPCCreated, new_npc)

    def send_message(self, message_name, data):
        print(f"{message_name}: {data}")
```