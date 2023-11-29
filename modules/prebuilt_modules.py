```python
from schemas.ModuleSchema import ModuleSchema

prebuilt_modules = []

def add_prebuilt_module(module):
    if isinstance(module, ModuleSchema):
        prebuilt_modules.append(module)
    else:
        raise TypeError("Expected instance of type 'ModuleSchema'")

def get_prebuilt_modules():
    return prebuilt_modules
```