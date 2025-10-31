from marshmallow import Schema, fields, post_load, validate
from app.models.cargo import Cargo

class CargoSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))
    id_facultad = fields.Integer(required=True)

    @post_load
    def make_cargo(self, data, **kwargs):
        return Cargo(**data)