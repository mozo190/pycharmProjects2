import streamlit as st

import functions

todos = functions.read_todos_txt_file()

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""  # Initialize the session state variable


st.title('Web ToDo App')
st.subheader('A simple ToDo app to keep track of your tasks')
st.write('Welcome to the Web ToDo App!')

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # If the checkbox is checked
        todos.remove(todo)
        functions.write_into_todos_txt_file(todos)
        st.write(f'Task "{todo}" is completed!')


st.text_input(label='Add a new task', on_change=functions.add_todo, key='new_todo')
