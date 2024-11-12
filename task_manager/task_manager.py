import json

class Task:
  
  def __init__(self, id, title, completed=False):
    self.id = id
    self.title = title
    self.completed = completed

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"{self.id}. {status}: {self.title}"

def load_tasks():
 
  try:
    with open("tasks.json", "r") as f:
      tasks = json.load(f)
      return [Task(**task) for task in tasks]
  except FileNotFoundError:
    return []

def save_tasks(tasks):
 
  with open("tasks.json", "w") as f:
    json.dump([task.__dict__ for task in tasks], f, indent=4)

def add_task():
 
  title = input("Enter task title: ")
  tasks.append(Task(len(tasks) + 1, title))
  print("Task added successfully!")

def view_tasks():
  
  if not tasks:
    print("There are no tasks to display.")
    return
  for task in tasks:
    print(task)

def delete_task():
 
  task_id = int(input("Enter task ID to delete: "))
  for i, task in enumerate(tasks):
    if task.id == task_id:
      del tasks[i]
      print(f"Task {task_id} deleted successfully!")
      return
  print(f"Task with ID {task_id} not found.")

def mark_complete():
  
  task_id = int(input("Enter task ID to mark complete: "))
  for task in tasks:
    if task.id == task_id:
      task.completed = True
      print(f"Task {task_id} marked as complete!")
      return
  print(f"Task with ID {task_id} not found.")

def main_menu():
  
  print("\nTask Manager")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Delete Task")
  print("4. Mark Task Complete")
  print("5. Exit")

def main():
  global tasks
  tasks = load_tasks()

  while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      delete_task()
    elif choice == '4':
      mark_complete()
    elif choice == '5':
      save_tasks(tasks)
      print("Exiting Task Manager.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()