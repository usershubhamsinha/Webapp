


def getTodo():
    with open('todos.txt', 'r') as data:
        todos = data.readlines()
        return todos

def pushTodo(arg):
    with open('todos.txt', 'w') as data:
        data.writelines(arg)

