```python
class Climate:
    def __init__(self, name, description, effects):
        self.name = name
        self.description = description
        self.effects = effects

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_effects(self):
        return self.effects

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_effects(self, effects):
        self.effects = effects

    def display_climate(self):
        return {
            "name": self.get_name(),
            "description": self.get_description(),
            "effects": self.get_effects()
        }
```