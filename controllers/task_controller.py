from models.Task import Task, db 
from datetime import datetime

def get_all_tasks():
  try:
    tasks = Task.query.all()
    return [{'id': task.id, 'task': task.title, 'description': task.description, 'deadline': task.deadline} for task in tasks]
  except Exception as e:
    db.session.rollback()
    return None, 'Database error'
  
def create_task(title, description):
  try:
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return {'task': new_task.title, 'description': new_task.description}, None 
  except Exception as e:
    db.session.rollback()
    return None, 'Database error'
  
def get_task_by_id(task_id):
  task = Task.query.get(task_id)
  if task:
    return {'id': task.id, 'title': task.title, 'description': task.description, 'deadline': task.deadline}, None
  return None, "Task not found"

def update_task(task_id, title=None, description=None, deadline=None):
  task = Task.query.get(task_id)
  if not task:
    return None, 'Task not found'

  if title: 
    task.title = title
  if description: 
    task.description = description
  if deadline:
    task.deadline = deadline

  db.session.commit()
  return {'id': task.id, 'title': task.title, 'description': task.description, 'deadline': task.deadline}, None

def delete_task (task_id):
  task = Task.query.get(task_id)
  if not task:
    return None, 'Task not found'

  db.session.delete(task)
  db.session.commit()
  return {'message': 'Task deleted successfully'}, None


def search_tasks_by_deadline(deadline):
    try:
        deadline_date = datetime.strptime(deadline, '%Y-%m-%d')  # Använd rätt format för datumen
        
        tasks = Task.query.filter(Task.deadline == deadline_date).all()

        return [{'id': task.id, 'title': task.title, 'description': task.description, 'deadline': task.deadline} for task in tasks], None
    except Exception as e:
        db.session.rollback()
        return None, f"Database error: {str(e)}"
    
def search_tasks_by_title(keyword):
  try:
    tasks = Task.query.filter(Task.title.ilike(f'%{keyword}%')).all()
    return [
      {'id': task.id, 'title': task.title, 'description': task.description, 'deadline': task.deadline}
      for task in tasks
    ], None
  except Exception as e:
    db.session.rollback()
    return None, 'Database error'
  
def completed_task(task_id):
  task = Task.query.get(task_id)
  if not task:
    return None, 'Task not found'

  task.is_completed = True
  db.session.commit()
  return {'id': task.id, 'title': task.title, 'completed': task.is_completed}, None

