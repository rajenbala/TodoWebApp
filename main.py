import streamlit as st
import filehandlers as fh

todos = fh.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    fh.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my TodoApp")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fh.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a Todo", on_change=add_todo, key='new_todo')

#st.session_state