class Task:
    def __init__(self,name: str, description: str):
        self.name = name
        self.description = description
    
    def display_info(self):
        print(f"Task is: {self.name}, description is: {self.description}")


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list(Task) = []
    
    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))
    
    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]
    
    def display_project_info(self):
        print(f"Project is: {self.name}")
        for task in self.tasks:
            task.display_info()

# Створення проекту
my_project = Project('Web-development')

# Додавання задач
my_project.add_task('Interface design', 'Create a main page model')
my_project.add_task('API develonment', 'implement endpoints for users')

# Відображення інформації про проєкт
my_project.display_project_info()

# Видалення задачи
my_project.remove_task('API develonment')

# Перевіврка видалення задачи
my_project.display_project_info()
