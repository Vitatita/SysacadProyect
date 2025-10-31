from marshmallow import fields, Schema, post_load, validate
from app.models.plan import Plan

class PlanSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))
    id_facultad = fields.Integer(required=True)
    id_orientacion = fields.Integer(required=True)
    id_categoria_cargo = fields.Integer(required=True)
    id_departamento = fields.Integer(required=True)

    @post_load
    def make_plan(self, data, **kwargs):
        return Plan(**data)