```python
from pydantic import BaseModel
from typing import List, Optional

class CampaignSchema(BaseModel):
    name: str
    description: str
    adventures: List[str]

class NPCSchema(BaseModel):
    name: str
    role: str
    objective: str
    relationships: List[str]

class StoryArcSchema(BaseModel):
    name: str
    description: str
    npcs: List[str]
    adventures: List[str]

class AdventureSchema(BaseModel):
    name: str
    description: str
    npcs: List[str]
    story_arc: str

class RoleSchema(BaseModel):
    name: str
    description: str

class ObjectiveSchema(BaseModel):
    name: str
    description: str

class RelationshipSchema(BaseModel):
    npc1: str
    npc2: str
    relationship: str

class TimelineEventSchema(BaseModel):
    event: str
    time: str
    involved_npcs: List[str]
    consequences: List[str]

class PlayerActionSchema(BaseModel):
    action: str
    time: str
    involved_npcs: List[str]
    consequences: List[str]

class ModuleSchema(BaseModel):
    name: str
    description: str
    involved_npcs: List[str]
    consequences: List[str]
```