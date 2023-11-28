```python
from shared_dependencies.data_schemas import StoryArcSchema, AdventureSchema
from shared_dependencies.exported_variables import story_arcs, adventures
from shared_dependencies.message_names import StoryArcCreated, AdventureCreated
from shared_dependencies.function_names import createStoryArc, createAdventure

class ArchAndQuill:
    def __init__(self):
        self.story_arcs = story_arcs
        self.adventures = adventures

    def create_story_arc(self, story_arc_data):
        new_story_arc = StoryArcSchema(**story_arc_data)
        self.story_arcs.append(new_story_arc)
        return StoryArcCreated

    def create_adventure(self, adventure_data):
        new_adventure = AdventureSchema(**adventure_data)
        self.adventures.append(new_adventure)
        return AdventureCreated

    def get_story_arcs(self):
        return self.story_arcs

    def get_adventures(self):
        return self.adventures

arch_and_quill = ArchAndQuill()

def createStoryArc(story_arc_data):
    return arch_and_quill.create_story_arc(story_arc_data)

def createAdventure(adventure_data):
    return arch_and_quill.create_adventure(adventure_data)
```