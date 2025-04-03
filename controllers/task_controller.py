from models.Task import Task, db 

def get_all_tasks():
  try:
    tasks = Task.query.all()
    return [{'id': task.id, 'task': task.title, 'description': task.description} for task in tasks]
  except Exception as e:
    db.session.rollback()
    return None, 'Database error'
  
def create_task(title, description):
  try:
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return {'task': new_task.title, 'description': new_task.description}, None  # Returnera två värden alltid!
  except Exception as e:
    db.session.rollback()
    return None, 'Database error'
