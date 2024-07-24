FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todo_arg, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
        
if __name__ == "__main__":
    print("C")