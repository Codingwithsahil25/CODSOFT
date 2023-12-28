import PySimpleGUI as sg
import time
import functions
sg.theme('DarkTeal2')
clock = sg.Text('',key='clock')
label1 = sg.Text("TODO APP")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("ADD",key="Add")
edit_button = sg.Button("EDIT")
complete_button = sg.Button("COMPLETE")
exit_button = sg.Button("EXIT")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45,10))
layout = [[clock],
          [label1],
          [input_box,add_button],
          [list_box,edit_button,complete_button],
          [exit_button]]
win = sg.Window("Welcome to my TO-DO App", layout=layout)
while True:
    event, values = win.read(timeout=200)
    win['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:#if event == "Add":
        case "Add":
            todos = functions.get_todos()               #load existing list
            new_todo = values['todo'] + "\n"            #take input from inputbox
            todos.append(new_todo)                      #append new to do in list
            functions.write_todos(todos)                #write updated todos back to file
            win['todos'].update(values=todos)           #update the display


        case "EDIT":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                win['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select an item First", font= ('Helvetica', 20))

        case "COMPLETE":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                win['todos'].update(values=todos)
                win['todo'].update(value='')
            except IndexError:
                sg.popup("Please Select an item First", font= ('Helvetica', 20))

        case "todos":
            win['todo'].update(value=values['todos'][0])
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    label = sg.Text("Type in a To-Do")