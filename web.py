import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.update_todos(todos)


todos = functions.get_todos()

st.title("Todo App")
st.subheader("Made with Python")
st.text("Increase you productivity with this way too simple on an app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.update_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label='', placeholder="Enter a to-do...", key='new_todo',
              on_change=add_todo)

st.session_state