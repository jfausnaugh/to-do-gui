#  creating a graphical user interface for the to do lists

import functions
import PySimpleGUI
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

PySimpleGUI.theme("Purple")

clock = PySimpleGUI.Text('', key="Clock")
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add", size=10)
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=(45, 10))
edit_button = PySimpleGUI.Button("Edit")
# complete_button = PySimpleGUI.Button(key="Complete", size=2, image_source="complete.png",
                                        # mouseover_colors="LightBlue2",tooltip="Complete Todo")
# Can use an image for a button instead of just text

complete_button = PySimpleGUI.Button("Complete")

exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Helvetica', 20))  # this is the title of the window application
#  each square bracket around the items above represent a new row. If all in one bracket, that's one row
while True:
    event, values = window.read(timeout=200)
    window["Clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # by putting [0] it grabs just the string instead of List
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)  # will give index of the item you pick
                todos[index] = new_todo  # will replace other item

                functions.write_todos(todos)  # then will rewrite list to text file
                window['todos'].update(values=todos)  # list of values will be updated with new list
            except IndexError:
                PySimpleGUI.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')  # value if only 1 value. Values if multiple
            except IndexError:
                PySimpleGUI.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
