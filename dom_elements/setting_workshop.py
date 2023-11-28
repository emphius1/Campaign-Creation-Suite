```python
from selenium import webdriver
from selenium.webdriver.common.by import By

class SettingWorkshop:
    def __init__(self, driver):
        self.driver = driver

    def get_campaign_settings(self):
        return self.driver.find_element(By.ID, 'campaign_settings')

    def get_npc_list(self):
        return self.driver.find_element(By.ID, 'npc_list')

    def get_story_arcs(self):
        return self.driver.find_element(By.ID, 'story_arcs')

    def get_adventures(self):
        return self.driver.find_element(By.ID, 'adventures')

    def get_npc_roles(self):
        return self.driver.find_element(By.ID, 'npc_roles')

    def get_npc_objectives(self):
        return self.driver.find_element(By.ID, 'npc_objectives')

    def get_npc_relationships(self):
        return self.driver.find_element(By.ID, 'npc_relationships')

    def get_timeline_events(self):
        return self.driver.find_element(By.ID, 'timeline_events')

    def get_player_actions(self):
        return self.driver.find_element(By.ID, 'player_actions')

    def get_prebuilt_modules(self):
        return self.driver.find_element(By.ID, 'prebuilt_modules')
```