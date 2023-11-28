```python
class MajorEvent:
    def __init__(self, name, description, impact):
        self.name = name
        self.description = description
        self.impact = impact

major_events = []

def create_major_event(name, description, impact):
    event = MajorEvent(name, description, impact)
    major_events.append(event)
    return event

def get_major_event(name):
    for event in major_events:
        if event.name == name:
            return event
    return None

def update_major_event(name, description=None, impact=None):
    event = get_major_event(name)
    if event is not None:
        if description is not None:
            event.description = description
        if impact is not None:
            event.impact = impact
        return True
    return False

def delete_major_event(name):
    event = get_major_event(name)
    if event is not None:
        major_events.remove(event)
        return True
    return False
```