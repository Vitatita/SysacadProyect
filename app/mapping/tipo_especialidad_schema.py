from marshmallow import fields, Schema, post_load, validate
from app.models.tipo_especialidad import TipoEspecialidad

class TipoEspecialidadSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))
    id_facultad = fields.Integer(required=True)

    @post_load
    def make_tipo_especialidad(self, data, **kwargs):
        return TipoEspecialidad(**data)