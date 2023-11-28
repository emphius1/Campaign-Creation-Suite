```python
from shared_dependencies.exported_variables import prebuilt_modules
from shared_dependencies.data_schemas import ModuleSchema
from messages.ModuleImported import ModuleImported

def importModule(module_name, module_data):
    try:
        # Validate the module data against the schema
        ModuleSchema.validate(module_data)

        # Add the module to the list of prebuilt modules
        prebuilt_modules[module_name] = module_data

        # Emit a message indicating that the module was imported
        ModuleImported.emit({
            'module_name': module_name,
            'module_data': module_data
        })

    except Exception as e:
        print(f"Failed to import module {module_name}: {str(e)}")
```