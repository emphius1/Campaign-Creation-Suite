```python
import json
from .utils import AIWritingAssistant
from .assets.story_arcs import StoryArcSchema
from .assets.adventures import AdventureSchema

story_arcs = []
adventures = []

def createStoryArc(title, plot_points, tags=[]):
    global story_arcs
    story_arc = StoryArcSchema(title=title, plot_points=plot_points, tags=tags)
    story_arcs.append(story_arc)
    return story_arc

def createAdventure(title, story_arc, tags=[]):
    global adventures
    adventure = AdventureSchema(title=title, story_arc=story_arc, tags=tags)
    adventures.append(adventure)
    return adventure

def getAIWritingAssistantFeedback(text):
    assistant = AIWritingAssistant()
    feedback = assistant.getFeedback(text)
    return feedback

def saveStoryArcsToFile():
    with open('story_arcs.json', 'w') as f:
        json.dump([arc.to_dict() for arc in story_arcs], f)

def saveAdventuresToFile():
    with open('adventures.json', 'w') as f:
        json.dump([adventure.to_dict() for adventure in adventures], f)

def loadStoryArcsFromFile():
    global story_arcs
    with open('story_arcs.json', 'r') as f:
        story_arcs = [StoryArcSchema.from_dict(arc) for arc in json.load(f)]

def loadAdventuresFromFile():
    global adventures
    with open('adventures.json', 'r') as f:
        adventures = [AdventureSchema.from_dict(adventure) for adventure in json.load(f)]
```