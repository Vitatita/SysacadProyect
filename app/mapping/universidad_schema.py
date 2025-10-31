from marshmallow import Schema, fields
from app.models.universidad import Universidad


class UniversidadSchema(Schema):
    id = fields.Int(load_only=True)
    hashid = fields.Str(attribute="hashid", dump_only=True)  
    nombre = fields.Str()
    direccion = fields.Str()
    ciudad = fields.Str()
    provincia = fields.Str()
    pais = fields.Str()
    telefono = fields.Str()
    email = fields.Str()