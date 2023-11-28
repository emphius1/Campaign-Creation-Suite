```python
from campaign_creation_suite.utils import StoryArcSchema

story_arcs = []

class StoryArc:
    def __init__(self, title, description, plot_points):
        self.title = title
        self.description = description
        self.plot_points = plot_points

    def to_dict(self):
        return StoryArcSchema().dump(self)

def createStoryArc(title, description, plot_points):
    new_story_arc = StoryArc(title, description, plot_points)
    story_arcs.append(new_story_arc.to_dict())
    return new_story_arc.to_dict()
```