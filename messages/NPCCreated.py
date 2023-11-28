class NPCCreated:
    def __init__(self, npc):
        self.npc = npc
        self.message = f"NPC {npc['name']} has been created."

    def display_message(self):
        print(self.message)