from task import Task
from taskmanager import TaskManager

t = Task(1,"TODO: Learn something",priority=3)
t2 = Task(2,"TODO: Check bugs on a program",priority=1)
t3 = Task(3,"TODO: Check for priority algorithm",priority=7)
task_manager = TaskManager()
task_manager.addTask(t)
task_manager.addTask(t2)
task_manager.addTask(t3)
print(task_manager)

"""Removing task"""
