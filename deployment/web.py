import streamlit as st
import functions as f

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)

todos = f.get_todos()

st.title("My To-do App.")
st.subheader("This is a simple to-do app.")
st.write("This app is not going to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        
st.text_input(label = "Enter a to-do in the box below.",
              placeholder = "Add a new to-do",
              on_change = add_todo,
              key = "new_todo"
              )