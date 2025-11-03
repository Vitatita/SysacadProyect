from flask import jsonify, Blueprint, request
from app.mapping.plan_schema import PlanSchema
from app.services.plan_service import PlanService

plan_bp = Blueprint('plan', __name__)
plan_schema = PlanSchema()

@plan_bp.route('/planes', methods=['POST'])
def create_plan():
    data = request.get_json()
    plan = PlanService.create_plan(**data)
    return jsonify(plan_schema.dump(plan)), 201

@plan_bp.route('/planes/<int:plan_id>', methods=['GET'])
def get_plan(plan_id):
    plan = PlanService.get_plan(plan_id)
    if plan:
        return jsonify(PlanMapping.to_dict(plan))
    return jsonify({'message': 'Plan not found'}), 404

@plan_bp.route('/planes/<int:plan_id>', methods=['PUT'])
def update_plan(plan_id):
    data = request.get_json()
    plan = PlanService.update_plan(plan_id, **data)
    if plan:
        return jsonify(PlanMapping.to_dict(plan))
    return jsonify({'message': 'Plan not found'}), 404

@plan_bp.route('/planes/<int:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    plan = PlanService.delete_plan(plan_id)
    if plan:
        return jsonify({'message': 'Plan deleted successfully'})
    return jsonify({'message': 'Plan not found'}), 404
