```python
class AdventureCreated:
    def __init__(self, adventure):
        self.adventure = adventure

    def __str__(self):
        return f"Adventure '{self.adventure['name']}' has been successfully created."
```