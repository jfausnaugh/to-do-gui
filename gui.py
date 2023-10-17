#  creating a graphical user interface for the to do lists

import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
add_button = PySimpleGUI.Button("Add")
window = PySimpleGUI.Window('My To-Do App', layout=[[label], [input_box, add_button]])  # this is the title of the window application
#  each square bracket around the items above represent a new row. If all in one bracket, that's one row
window.read()
window.close()
