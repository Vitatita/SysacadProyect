from marshmallow import fields, Schema, post_load, validate
from app.models.facultad import Facultad


class FacultadSchema(Schema):
    id = fields.Integer() 
    nombre = fields.String(required = True, validate = validate.Length(min=1, max=100))
    sigla = fields.String(required = True, validate = validate.Length(min=1, max=10))

    @post_load
    def make_facultad(self,data,**kwargs):
        return Facultad(**data)