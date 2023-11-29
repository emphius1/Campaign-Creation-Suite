class PlayerActionPerformed:
    def __init__(self, player_action):
        self.player_action = player_action

    def get_message(self):
        return f"Player action '{self.player_action}' has been performed."