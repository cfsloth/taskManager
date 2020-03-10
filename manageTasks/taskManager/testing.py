from task import Task
from taskmanager import TaskManager

t = Task(1,"TODO: Learn something")
task_manager = TaskManager()
task_manager.addTask(t)
print(task_manager)
