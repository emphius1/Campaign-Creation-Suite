```python
# Importing required schemas
from schemas.ModuleSchema import ModuleSchema

# Prebuilt modules
prebuilt_modules = []

# Function to add a prebuilt module
def add_prebuilt_module(module):
    if isinstance(module, ModuleSchema):
        prebuilt_modules.append(module)
        print("ModuleImported")
    else:
        print("Invalid module")

# Function to get a prebuilt module
def get_prebuilt_module(module_name):
    for module in prebuilt_modules:
        if module.name == module_name:
            return module
    return None
```