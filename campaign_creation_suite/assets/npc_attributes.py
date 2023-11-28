```python
class NPCAttributes:
    def __init__(self, race, npc_class, thoughts, habits, biases, needs, alignments):
        self.race = race
        self.npc_class = npc_class
        self.thoughts = thoughts
        self.habits = habits
        self.biases = biases
        self.needs = needs
        self.alignments = alignments

    def get_attributes(self):
        return {
            'race': self.race,
            'class': self.npc_class,
            'thoughts': self.thoughts,
            'habits': self.habits,
            'biases': self.biases,
            'needs': self.needs,
            'alignments': self.alignments
        }

    def update_attribute(self, attribute, value):
        if hasattr(self, attribute):
            setattr(self, attribute, value)
        else:
            raise ValueError(f"Attribute {attribute} not found")

    def __str__(self):
        return str(self.get_attributes())
```