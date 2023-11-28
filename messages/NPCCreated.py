```python
class NPCCreated:
    def __init__(self, npc):
        self.npc = npc
        self.message_name = "NPCCreated"

    def get_message(self):
        return {
            "message_name": self.message_name,
            "npc": self.npc
        }
```