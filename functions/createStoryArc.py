```python
from shared_dependencies.data_schemas import StoryArcSchema
from shared_dependencies.exported_variables import story_arcs

def createStoryArc(name, description, objectives, npcs, timeline_events):
    new_story_arc = StoryArcSchema(name, description, objectives, npcs, timeline_events)
    story_arcs.append(new_story_arc)
    return new_story_arc
```