# creating a custom function helps to reduce the amount of code we repeat

def get_todos(
        filepath="todos.txt"):  # function has an argument in it, so when we call it we mention the file to call
    # docstring of a function, describes function
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:  # r is the default of the context manager
        todos_local = file_local.readlines()
    return todos_local


# file = open('files/todos.txt', 'r')
# todos = file.readlines()
# file.close()
# using a context-manager you don't need to close a file
# better way of writing the code than the above commented out code
def write_todos(todos_arg, filepath="todos.txt"):  # nondefault perameters come before default ones
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    # isn't returning anything because we are just having it do an action, nothing to return.


# conditional block will only run when running the program directly.
# when running the file through import then the block won't run

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
