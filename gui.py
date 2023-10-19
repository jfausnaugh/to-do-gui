#  creating a graphical user interface for the to do lists

import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[label],
                                    [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Helvetica', 20))  # this is the title of the window application
#  each square bracket around the items above represent a new row. If all in one bracket, that's one row
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]  # by putting [0] it grabs just the string instead of List
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)  # will give index of the item you pick
            todos[index] = new_todo  # will replace other item

            functions.write_todos(todos)  # then will rewrite list to text file
            window['todos'].update(values=todos)  # list of values will be updated with new list
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')  # value if only 1 value. Values if multiple
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
