from functions import get_todos, write_todos
# or import functions

# import time module
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip char from it
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    # type add, give space and type your
    # todos activity, in the final program
    if user_action.startswith('add'):
        # using list slicing to extract part of a user input
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):

            item = item.strip('\n')
            row = f"{index + 1} - {item.capitalize()}"
            print(row)
    # type edit, give space and type the 4 you want to edit in the program
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)

            print('successful!')
        except ValueError:
            print('Type edit, give a space follow by the serial number ')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"todo, {todo_to_remove} was removed from the list!"
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('You must select a command!')

print('Bye!!!')