from flask import Blueprint, request, jsonify
from controllers.task_controller import create_task

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/create', methods=['POST'])
def post_task():

  data = request.get_json()

  if not data or 'title' not in data or 'description' not in data:
    return jsonify({'error': 'Invalid input'}), 400
  
  new_task, error = create_task(data['title'], data['description'])

  if error:
    return jsonify({'error': error}), 500
  
  return jsonify(new_task), 201