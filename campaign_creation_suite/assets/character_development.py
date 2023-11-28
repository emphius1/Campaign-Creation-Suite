```python
class CharacterDevelopment:
    def __init__(self):
        self.character_development = []

    def add_character_development(self, character_development):
        self.character_development.append(character_development)

    def get_character_development(self):
        return self.character_development

class CharacterDevelopmentSchema:
    def __init__(self, name, description, impact):
        self.name = name
        self.description = description
        self.impact = impact

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "impact": self.impact
        }
```