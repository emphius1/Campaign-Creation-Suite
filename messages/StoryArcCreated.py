class StoryArcCreated:
    def __init__(self, story_arc):
        self.story_arc = story_arc

    def get_message(self):
        return f"Story Arc '{self.story_arc['name']}' has been successfully created."