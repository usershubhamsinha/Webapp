import streamlit as st
import todomodule as tm

todos = tm.getTodo()
index = 0
def addTodo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    tm.pushTodo(todos)
    st.session_state['new_todo'] = ''


st.title('My Todo App')
st.subheader('its just a todo app')
st.write("this is an experimental app")

if len(todos) > 10:
    todos.pop(0)
    tm.pushTodo(todos)

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'{i} - {todo}')
    if checkbox:
        todos.pop(i)
        tm.pushTodo(todos)
        del st.session_state[f'{i} - {todo}']
        st.experimental_rerun()

def clear():
    todo = ''
    tm.pushTodo(todo)

st.text_input(label='', placeholder='Add new todo...',
              on_change=addTodo, key='new_todo')
st.button(label='Clear All', key='clear', on_click=clear)

