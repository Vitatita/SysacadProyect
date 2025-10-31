from marshmallow import fields, Schema, post_load, validate
from app.models.grado import Grado

class GradoSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))
    id_facultad = fields.Integer(required=True)

    @post_load
    def make_grado(self, data, **kwargs):
        return Grado(**data)
