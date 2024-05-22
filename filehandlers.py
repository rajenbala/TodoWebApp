def gethelp():
    print(help(get_todos))

def get_todos(filepath="todos.txt"):
    """ Open the File and convert the content as list
     with each line as an individual object of the list"""
    with (open(filepath, 'r')) as fileRead:
        return fileRead.readlines()

def write_todos(todos_args,filepath="todos.txt"):
    """Write the To-do items list in the new file"""
    with (open(filepath, 'w')) as fileWrite:
        fileWrite.writelines(todos_args)