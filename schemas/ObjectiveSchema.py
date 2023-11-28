```python
from marshmallow import Schema, fields

class ObjectiveSchema(Schema):
    objective_id = fields.Str(required=True)
    objective_name = fields.Str(required=True)
    objective_description = fields.Str(required=True)
    objective_status = fields.Str(required=True)
    objective_priority = fields.Int(required=True)
    objective_deadline = fields.DateTime(required=False)
```