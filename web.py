import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    # When user hits enter, it calls the function and executes it

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label_visibility="collapsed", label="Add new todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state