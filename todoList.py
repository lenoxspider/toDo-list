#/usr/bin/env python3

succ = 'Task added.'
prompt = 'Enter a task for our to-do list. Press <enter> when done: '
title = 'Your To-Do List:'
task_list = []

def printer():
    for number in range(0, len(task_list)):
        print(task_list[number])

while True:
    task_input = input(prompt)
    n += 1

    if task_input == "":
        print(title)
        print('-' * len(title))
        printer()
        break
    else:
        task_list.append(task_input)
        print(succ)
        
