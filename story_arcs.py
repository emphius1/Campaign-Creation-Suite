```python
from schemas.StoryArcSchema import StoryArcSchema

story_arcs = []

def createStoryArc(name, description, objectives, npcs, timeline_events):
    new_story_arc = StoryArcSchema(name, description, objectives, npcs, timeline_events)
    story_arcs.append(new_story_arc)
    return new_story_arc
```