#  creating a graphical user interface for the to do lists

import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add")
window = PySimpleGUI.Window('My To-Do App',
                            layout=[[label], [input_box, add_button]],
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
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
