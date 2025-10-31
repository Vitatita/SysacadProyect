from marshmallow import fields, Schema, post_load, validate
from app.models.materia import Materia

class MateriaSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))
    id_facultad = fields.Integer(required=True)
    codigo = fields.String(required=True, validate=validate.Length(max=20))
    creditos = fields.Integer(required=True, validate=validate.Range(min=1))

    @post_load
    def make_materia(self, data, **kwargs):
        return Materia(**data)