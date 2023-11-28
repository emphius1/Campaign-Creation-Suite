```python
from marshmallow import Schema, fields

class ModuleSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    dependencies = fields.List(fields.Str(), required=True)
    version = fields.Str(required=True)
```