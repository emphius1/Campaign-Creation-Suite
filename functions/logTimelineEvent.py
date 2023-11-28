```python
from shared_dependencies.data_schemas import TimelineEventSchema
from shared_dependencies.exported_variables import timeline_events

def logTimelineEvent(event_data):
    event = TimelineEventSchema(**event_data)
    timeline_events.append(event)
    return {"message": "TimelineEventLogged", "event": event}
```