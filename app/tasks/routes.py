from flask import requests, jsonify
from . import tasks_bp
from app.models import Task 
from app.extensions import db 

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify([{
            'id': t.id,
            'title': t.title,
            'description': t.description,
            'due_date': t.due_date,
            'completed': t.completed
        } for t in tasks])
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve tasks', 'error': str(e)}), 500

@tasks_bp.route('/', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        if 'title' not in data:
            return jsonify({'message': 'Title is required'}), 400
        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            due_date=data.get('due_date')
        )
        
        db.session.add(new_task)
        db.session.commit()
    
        return jsonify({'message': 'Task created successfully'}), 201

    except Exception as e:
        db.session.rollback()
        
        return jsonify({'message': 'Failed to create task', 'error': str(e)}), 500

@tasks_bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        task = Task.query.get_or_404(id)
        data = request.get_json()

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.due_date = data.get('due_date', task.due_date)
        task.completed = data.get('completed', task.completed)

        db.session.commit()
        return jsonify({'message' : 'Task updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update task', 'error': str(e)}), 500

@tasks_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:           
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message' : 'Task deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete task', 'error': str(e)}), 500