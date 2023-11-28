```python
from datetime import datetime
from typing import List, Dict
from pydantic import BaseModel

class TimelineEventSchema(BaseModel):
    event_id: str
    event_name: str
    event_description: str
    event_date: datetime
    related_npcs: List[str]
    related_locations: List[str]

timeline_events: Dict[str, TimelineEventSchema] = {}

def logTimelineEvent(event_id: str, event_name: str, event_description: str, event_date: datetime, related_npcs: List[str], related_locations: List[str]) -> None:
    new_event = TimelineEventSchema(
        event_id=event_id,
        event_name=event_name,
        event_description=event_description,
        event_date=event_date,
        related_npcs=related_npcs,
        related_locations=related_locations
    )
    timeline_events[event_id] = new_event
```