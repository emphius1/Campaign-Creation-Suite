class ModuleImported:
    def __init__(self, module_name, timestamp):
        self.module_name = module_name
        self.timestamp = timestamp

    def __str__(self):
        return f'Module {self.module_name} was successfully imported at {self.timestamp}'