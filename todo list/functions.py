import streamlit as st

FILE_PATH = "todos.txt"

def get_todos(filepath=FILE_PATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILE_PATH):
    """Write the to-do items lists in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is to increase your productivity")

todos = get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    write_todos(todos)
    st.session_state['new_todo'] = ''

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="Add a new todo", placeholder="Add a new todo", on_change=add_todo, key="new_todo")
