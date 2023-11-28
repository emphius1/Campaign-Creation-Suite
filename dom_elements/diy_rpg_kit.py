```python
from selenium import webdriver
from selenium.webdriver.common.by import By

class DIYRPGKit:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self):
        return self.driver.find_element(By.ID, 'diy_rpg_kit')
```