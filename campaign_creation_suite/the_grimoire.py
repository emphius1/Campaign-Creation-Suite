```python
import json
from campaign_creation_suite.utils import ModuleSchema

prebuilt_modules = []

def load_modules():
    global prebuilt_modules
    try:
        with open('campaign_creation_suite/assets/prebuilt_modules.json', 'r') as file:
            data = json.load(file)
            for module in data:
                validated_module = ModuleSchema(**module)
                prebuilt_modules.append(validated_module)
    except FileNotFoundError:
        print("Prebuilt modules file not found. Please ensure the file exists.")

def import_module(module_name):
    global prebuilt_modules
    for module in prebuilt_modules:
        if module.name == module_name:
            return module
    print(f"Module {module_name} not found in the grimoire.")
    return None

load_modules()
```