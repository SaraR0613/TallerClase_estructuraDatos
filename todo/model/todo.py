# TODO: Add code here

class Todo:

    def __init__(self, code_id, title, description):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: (list[str]) = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f" el código es:({self.code_id} y el titulo es: {self.title}"


class TodoBook:

    def __int__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        nuevo_id = int(len(self.todos)+1)
        todo_1= Todo(nuevo_id, title, description)
        self.todos [nuevo_id]= todo_1
        return nuevo_id
