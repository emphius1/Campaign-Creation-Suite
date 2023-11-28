```python
from schemas.TimelineEventSchema import TimelineEventSchema

timeline_events = []

def add_event(event):
    if isinstance(event, TimelineEventSchema):
        timeline_events.append(event)
    else:
        raise TypeError("Event must be of type TimelineEventSchema")

def get_all_events():
    return timeline_events

def get_event_by_id(event_id):
    for event in timeline_events:
        if event.id == event_id:
            return event
    return None

def remove_event(event_id):
    for event in timeline_events:
        if event.id == event_id:
            timeline_events.remove(event)
            return True
    return False
```