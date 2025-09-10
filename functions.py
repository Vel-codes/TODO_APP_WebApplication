FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads the text file and returns a
    list of to-do items.
    """

    with open(filepath, 'r') as file:
        return file.readlines()
    
    
def update_todos(list_of_todos, filepath=FILEPATH):
    """ Writes to-do's to the file """
    with open(filepath, 'w') as file:
        file.writelines(list_of_todos)

