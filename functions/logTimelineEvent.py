```python
from schemas.TimelineEventSchema import TimelineEventSchema

def logTimelineEvent(event_data):
    event = TimelineEventSchema(**event_data)
    timeline_events.append(event)
    print(f'TimelineEventLogged: {event_data["event_name"]}')
    return event
```