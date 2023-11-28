```python
from campaign_creation_suite.assets.timeline import TimelineEventSchema
from campaign_creation_suite.utils import send_message

class DMJournal:
    def __init__(self):
        self.timeline_events = []
        self.player_actions = []

    def log_timeline_event(self, event_data):
        event = TimelineEventSchema().load(event_data)
        self.timeline_events.append(event)
        send_message('TimelineEventLogged', event)
        return event

    def log_player_action(self, action_data):
        action = PlayerActionSchema().load(action_data)
        self.player_actions.append(action)
        send_message('PlayerActionPerformed', action)
        return action

    def get_timeline(self):
        return [event.dump() for event in self.timeline_events]

    def get_player_actions(self):
        return [action.dump() for action in self.player_actions]

    def share_updates(self):
        updates = {
            'timeline': self.get_timeline(),
            'player_actions': self.get_player_actions()
        }
        send_message('UpdatesShared', updates)
        return updates
```