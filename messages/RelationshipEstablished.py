```python
class RelationshipEstablished:
    def __init__(self, npc1, npc2, relationship):
        self.npc1 = npc1
        self.npc2 = npc2
        self.relationship = relationship

    def display_message(self):
        print(f"Relationship established between {self.npc1} and {self.npc2} as {self.relationship}.")
```