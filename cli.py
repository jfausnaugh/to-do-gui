import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    # gets input from user
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # adds a new to-do item to the list that user enters
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        # shows the current to-do list to the user
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
    elif user_action.startswith("edit"):
        # edits an already existing to-do item
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo_item = input("Enter your new todo item: ")
            todos[number] = new_todo_item + '\n'

            functions.write_todos(todos)
        except ValueError:
            # will cause an exception if user doesn't enter an integer
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        # will remove to-do item from the list
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        # will exit the program
        break
    else:
        print("Command not valid.")
