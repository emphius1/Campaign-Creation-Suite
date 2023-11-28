```python
class Terrain:
    def __init__(self, name, description, difficulty_level):
        self.name = name
        self.description = description
        self.difficulty_level = difficulty_level

    def get_terrain_info(self):
        return {
            "name": self.name,
            "description": self.description,
            "difficulty_level": self.difficulty_level
        }

def create_terrain(name, description, difficulty_level):
    new_terrain = Terrain(name, description, difficulty_level)
    return new_terrain.get_terrain_info()
```