```python
from shared_dependencies.exported_variables import prebuilt_modules
from shared_dependencies.data_schemas import ModuleSchema
from messages.ModuleImported import ModuleImported

def importModule(module_name):
    try:
        module = prebuilt_modules[module_name]
        validated_module = ModuleSchema().load(module)
        prebuilt_modules[module_name] = validated_module
        ModuleImported.emit(module_name)
    except KeyError:
        print(f"Module {module_name} not found in prebuilt modules.")
    except ValidationError as e:
        print(f"Module {module_name} failed validation: {e}")
```