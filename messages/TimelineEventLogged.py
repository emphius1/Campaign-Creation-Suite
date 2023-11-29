class TimelineEventLogged:
    def __init__(self, timeline_event):
        self.name = 'TimelineEventLogged'
        self.timeline_event = timeline_event

    def to_dict(self):
        return {
            'name': self.name,
            'timeline_event': self.timeline_event
        }