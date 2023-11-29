```python
from selenium import webdriver
from selenium.webdriver.common.by import By

class ButterflyEffectEngine:
    def __init__(self, driver):
        self.driver = driver

    def log_event(self, event):
        butterfly_effect_engine = self.driver.find_element(By.ID, 'butterfly_effect_engine')
        butterfly_effect_engine.send_keys(event)

    def clear_log(self):
        butterfly_effect_engine = self.driver.find_element(By.ID, 'butterfly_effect_engine')
        butterfly_effect_engine.clear()
```