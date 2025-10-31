from marshmallow import fields, Schema, post_load, validate
from app.models.especialidad import Especialidad

class EspecialidadSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1))
    descripcion = fields.Str(required=False, allow_none=True)

    @post_load
    def make_especialidad(self, data, **kwargs):
        return Especialidad(**data)
    