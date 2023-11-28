```python
class DMJournal:
    def __init__(self):
        self.element_id = "dm_journal"

    def get_element(self):
        return document.getElementById(self.element_id)

dm_journal = DMJournal()
```