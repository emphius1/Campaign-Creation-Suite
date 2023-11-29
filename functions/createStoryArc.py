```python
from schemas.StoryArcSchema import StoryArcSchema

def createStoryArc(title, description, objectives, npcs, timeline_events):
    new_story_arc = StoryArcSchema(title=title, description=description, objectives=objectives, npcs=npcs, timeline_events=timeline_events)
    story_arcs.append(new_story_arc)
    return new_story_arc
```