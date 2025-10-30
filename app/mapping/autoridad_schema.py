from marshmallow import fields, Schema, post_load, validate
from app.models.autoridad import Autoridad

class AutoridadSchema(Schema):
    nombre= fields.String(required=True, validate=validate.Length(max=100))
    cargo = fields.String(required=True, validate=validate.Length(max=100))
    telefono = fields.String(required=True, validate=validate.Length(max=20))
    email = fields.String(required=True, validate=validate.Length(max=100))
    id_facultad = fields.Integer(required=True)
  
    @post_load
    def make_autoridad(self, data, **kwargs):
        return Autoridad(**data)