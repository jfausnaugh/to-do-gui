import functions
import PySimpleGUI
import time
import os

# if a text file doesn't exist, it will be created
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# create GUI widgets
PySimpleGUI.theme("Purple")

clock = PySimpleGUI.Text('', key="Clock")
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add", size=10)
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=(45, 10))
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button(key="Complete",
                                     image_size=(50, 50),
                                     image_source="complete.png",
                                     mouseover_colors="LightBlue2",
                                     tooltip="Complete Todo")


exit_button = PySimpleGUI.Button("Exit")

# Create GUI layout
window = PySimpleGUI.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Helvetica',
                                  20))

while True:
    event, values = window.read(timeout=200)
    window["Clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            # pulls current to-do list
            todos = functions.get_todos()
            # Gets new to-do from user and adds to to-do list
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)

            # clears text box field
            input_box.update(value="")

            # updates to-do list in text file and on the screen
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                # Finds the value of the to-do item clicked
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                # pulls current to-do list and finds the index of current to-do
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                # replaces old to-do with the edited version
                todos[index] = new_todo

                # updates the to-do list in txt file and on screen
                functions.write_todos(todos)
                window['todos'].update(values=todos)

                # clears the textbox field
                input_box.update(value="")
            except IndexError:
                PySimpleGUI.popup("Please select an item first.",
                                  font=("Helvetica", 20))
        case "Complete":
            try:
                # gets the value of the to-do item clicked
                todo_to_complete = values['todos'][0]

                # pulls current to-do list and removes item from list
                todos = functions.get_todos()
                todos.remove(todo_to_complete)

                # updates to-do list in text file and on screen
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup("Please select an item first.",
                                  font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
