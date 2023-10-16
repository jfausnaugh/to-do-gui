# from functions import get_todos, write_todos
import functions  # creates a module and imports it into this file
import time  # module that is created by python developers, instead of one we made

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # this will remove any extra space at the end

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)  # since doesn't return anything, don't need to set to a variable

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] List comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo_item = input("Enter your new todo item: ")
            todos[number] = new_todo_item + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue  # causes to start the loop back over.

    elif user_action.startswith("complete"):
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
        break
    else:
        print("Command not valid.")
