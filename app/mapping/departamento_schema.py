from marshmallow import fields, Schema, post_load, validate
from app.models.departamento import Departamento

class DepartamentoSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))
    id_facultad = fields.Integer(required=True)

    @post_load
    def make_departamento(self, data, **kwargs):
        return Departamento(**data)