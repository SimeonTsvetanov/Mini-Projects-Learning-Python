import tkinter
import pickle


# Functions:

# This function saves the code to the family.pickle file
def save():
    family_file = open("family.pickle", "wb")
    pickle.dump(family, family_file)
    family_file.close()


# This function will check if there is already data file and if there is none it will create it.
def check():
    global family
    try:
        family_file = open("family.pickle", "rb")
        family = pickle.load(family_file)
    except IOError or EOFError:
        family = []


check()  # call the check function to run the check for the family file.


def add_task():  # Add a new task
    task = new_task_input.get()  # Pull the task from the input field
    if task != "":
        family.append(task)  # Adding the new task to the family file
        save()  # save the family file
        update_task_list()  # Update the task list, so ti will be clean.
        lbl_interactive["text"] = "Task Added."  # Adding a message
        new_task_input.delete(0, "end")  # Clear the interactive label
    else:
        lbl_interactive["text"] = "You need to enter the task, first."  # Adding a message


def del_all_tasks():  # Delete all the tasks.
    family.clear()  # This will clear the whole file.
    save()  # Save the file cleaned.
    update_task_list()  # Update the task list, so ti will be clean.
    lbl_interactive["text"] = "All Deleted"  # print a message


def show_all():  # Show All tasks.
    clear_tasks_list()  # Clear the list from all the prev. items.
    for task in family:  # Update the Task List if update is needed (like adding new task)
        list_tasks.insert("end", task)
    if len(family) == 0:
        lbl_interactive["text"] = "No Tasks yet. Enter the first one."  # print a message


def delete_current():  # Delete just the current task
    task = list_tasks.get("active")  # pull the selected task
    if task in family:  # Check if task exist
        family.remove(task)  # Remove it from the family file.
        save()  # Save the family file
        update_task_list()  # Update the task list (without the deleted item)
        lbl_interactive["text"] = "Task Deleted."  # print a message
    else:
        lbl_interactive["text"] = "Select a task from the list."  # print a message


def update_task_list():
    clear_tasks_list()  # Clear the list from all the prev. items.
    for task in family:  # Update the Task List if update is needed (like adding new task)
        list_tasks.insert("end", task)


def clear_tasks_list():  # Clear the task list. Otherwise it overpopulates.
    list_tasks.delete(0, "end")


# GUI

# Create the Window
window = tkinter.Tk()

# Change the Window Background color
window.configure(bg="gray")

# Change the title
window.title("To Do List")

# Change the window size:
window.geometry("285x230")

# This is the TO-DO visual label
lbl_interactive = tkinter.Label(window, text='<< TO-DO >>', bg="light gray", width=11)
lbl_interactive.grid(row=0, column=0)

# This is the interactive visual label
lbl_interactive = tkinter.Label(window, text='Welcome to the TO-DO list Manager', bg="light gray", width=28)
lbl_interactive.grid(row=0, column=1)

# Text field for the new entry
new_task_input = tkinter.Entry(window, width=27,)
new_task_input.grid(row=2, column=1)

# Button Add New Task
btn_add_task = tkinter.Button(window, text="Add Task", bg="black", fg="white", width="11", command=add_task)
btn_add_task.grid(row=2, column=0)

# Button Shall All Tasks
btn_add_task = tkinter.Button(window, text="Show All", bg="black", fg="white", width="11", command=show_all)
btn_add_task.grid(row=3, column=0)

# Button Delete Current Task
btn_delete_current = tkinter.Button(window, text="Delete Selected", bg="black", fg="white", width="11",
                                    command=delete_current)
btn_delete_current.grid(row=4, column=0)

# Button Delete All Tasks
btn_del_all = tkinter.Button(window, text="Delete All", bg="black", fg="white", width="11", command=del_all_tasks)
btn_del_all.grid(row=5, column=0)

# Button Quit the Program
btn_exit = tkinter.Button(window, text="Exit", bg="red", fg="white", width="11", command=exit)
btn_exit.grid(row=8, column=0)

# Show all the tasks as a List Box.
list_tasks = tkinter.Listbox(window, width=27)
list_tasks.grid(row=3, column=1, rowspan=6,)

# Footer - Used a button to make the Footer. Yep i'am a cheater!
btn_footer = tkinter.Button(window, text="", bg="light gray", fg="white", width="39",)
btn_footer.grid(row=9, column=0, columnspan=2)


window.mainloop()  # Start The main Window.

