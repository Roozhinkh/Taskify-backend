from flask import Blueprint, request, jsonify
from controllers.task_controller import create_task, get_task_by_id, update_task, delete_task, search_tasks_by_deadline, search_tasks_by_title, get_all_tasks, completed_task

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/create', methods=['POST'])
def post_task():

  data = request.get_json()

  if not data or 'title' not in data or 'description' not in data:
    return jsonify({'error': 'Invalid input'}), 400
  
  new_task, error = create_task(data['title'], data['description'], data['deadline'])

  if error:
    return jsonify({'error': error}), 500
  
  return jsonify(new_task), 201

@task_routes.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task, error = get_task_by_id(task_id)
    if error:
        return jsonify({'error': error}), 404
    return jsonify({'task': task}), 200


@task_routes.route('/', methods=['GET'])
def get_tasks():
    tasks, error = get_all_tasks()
    if error:
        return jsonify({'error': error}), 500
    return jsonify({'tasks': tasks}), 200

@task_routes.route('/<int:task_id>', methods=['PUT'])
def put_task(task_id):
    data = request.get_json()
    task, error = update_task(task_id, data.get('title'), data.get('description'), data.get('deadline'))
    if error:
        return jsonify({'error': error}), 404
    return jsonify({'message': 'Task updated successfully', 'task': task}), 200

@task_routes.route('/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    message, error = delete_task(task_id)
    if error:
        return jsonify({'error': error}), 404
    return jsonify(message), 200

@task_routes.route('/search_by_deadline', methods=['GET'])
def search_by_deadline():
    deadline = request.args.get('deadline')  # Hämta deadline från URL-parametrar

    if not deadline:
        return jsonify({'error': 'Missing deadline parameter'}), 400

    tasks, error = search_tasks_by_deadline(deadline)
    if error:
        return jsonify({'error': error}), 500

    return jsonify({'tasks': tasks}), 200

@task_routes.route('/search', methods=['GET'])
def search_task_by_title():
  keyword = request.args.get('keyword')

  if not keyword:
    return jsonify({'error': 'Keyword is required'}), 400

  tasks, error = search_tasks_by_title(keyword)

  if error:
    return jsonify({'error': error}), 500

  return jsonify({'tasks': tasks}), 200


@task_routes.route('/<int:task_id>/complete', methods=['PATCH'])
def completed_task(task_id):
  task, error = completed_task(task_id)
  if error:
    return jsonify({'error': error}), 404
  return jsonify({'message': 'Task marked as completed', 'task': task}), 200
