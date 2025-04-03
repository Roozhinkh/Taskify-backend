from marshmallow import Schema, fields
from .models import User, Task

# User Schema
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)

# Task Schema
class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    due_date = fields.Str()
    completed = fields.Bool(default=False)
