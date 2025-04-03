from flask import request, jsonify
from . import tasks_bp
from app.models import Task
from app.extensions import db
from app.schemas import TaskSchema
from app import app
from app.models import ContactMessage

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify(tasks_schema.dump(tasks))
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve tasks', 'error': str(e)}), 500

@tasks_bp.route('/', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        errors = task_schema.validate(data)
        if errors:
            return jsonify({'message': 'Invalid data', 'errors': errors}), 400

        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            due_date=data.get('due_date'),
            completed=data.get('completed', False)
        )

        db.session.add(new_task)
        db.session.commit()

        return jsonify({'message': 'Task created successfully', 'task': task_schema.dump(new_task)}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create task', 'error': str(e)}), 500

@tasks_bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        task = Task.query.get_or_404(id)
        data = request.get_json()
        errors = task_schema.validate(data, partial=True)

        if errors:
            return jsonify({'message': 'Invalid data', 'errors': errors}), 400

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.due_date = data.get('due_date', task.due_date)
        task.completed = data.get('completed', task.completed)

        db.session.commit()
        return jsonify({'message': 'Task updated successfully', 'task': task_schema.dump(task)})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update task', 'error': str(e)}), 500

@tasks_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Task.query.get(id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404

        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete task', 'error': str(e)}), 500
    
@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    try:
        message = ContactMessage(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )
        db.session.add(message)
        db.session.commit()
        return jsonify({'message': 'Meddelandet har sparats'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
