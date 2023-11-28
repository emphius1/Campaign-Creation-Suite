```python
from schemas.StoryArcSchema import StoryArcSchema

story_arcs = []

def createStoryArc(title, description, objectives, npcs, timeline_events):
    new_story_arc = StoryArcSchema(title, description, objectives, npcs, timeline_events)
    story_arcs.append(new_story_arc)
    return new_story_arc
```