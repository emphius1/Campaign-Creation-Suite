```python
from shared_dependencies.data_schemas import NPCSchema
from shared_dependencies.exported_variables import npc_list
from shared_dependencies.message_names import NPCCreated
from shared_dependencies.function_names import createNPC

class NPCCradle:
    def __init__(self):
        self.npc_schema = NPCSchema()
        self.npc_list = npc_list

    def create_npc(self, npc_data):
        new_npc = self.npc_schema.load(npc_data)
        self.npc_list.append(new_npc)
        self.notify_npc_created(new_npc)

    def notify_npc_created(self, npc):
        message = {
            "name": NPCCreated,
            "data": {
                "npc": npc
            }
        }
        self.send_message(message)

    def send_message(self, message):
        # This function will send the message to the appropriate destination.
        # The implementation of this function depends on the specific message passing or event system you are using.
        pass

npc_cradle = NPCCradle()

def createNPC(npc_data):
    npc_cradle.create_npc(npc_data)
```