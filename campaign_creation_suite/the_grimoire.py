```python
from shared_dependencies.exported_variables import prebuilt_modules
from shared_dependencies.data_schemas import ModuleSchema
from shared_dependencies.message_names import ModuleImported
from shared_dependencies.function_names import importModule

class TheGrimoire:
    def __init__(self):
        self.modules = prebuilt_modules

    def import_module(self, module_id):
        try:
            module = self.modules[module_id]
            if ModuleSchema.validate(module):
                importModule(module)
                print(ModuleImported.format(module_id))
            else:
                print("Invalid module schema.")
        except KeyError:
            print("Module not found.")

    def list_modules(self):
        for module_id, module in self.modules.items():
            print(f"ID: {module_id}, Name: {module['name']}, Description: {module['description']}")

the_grimoire = TheGrimoire()
```
