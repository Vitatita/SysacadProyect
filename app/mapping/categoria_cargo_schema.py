from marshmallow import fields, Schema, post_load, validate
from app.models.categoria_cargo import CategoriaCargo

class CategoriaCargoSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))
    id_facultad = fields.Integer(required=True)

    @post_load
    def make_categoria_cargo(self, data, **kwargs):
        return CategoriaCargo(**data)