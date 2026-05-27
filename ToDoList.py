#TO DO LIST GUI 


#importing libraries
import tkinter as tkin        
from tkinter import messagebox 


#function to handle entry click event
def on_entry_click(event):
    if entry_task.get() == "Enter task here...":
        entry_task.delete(0, tkin.END)
        entry_task.insert(0, '')
        entry_task.config(fg='blue')


#Function to handle the focus out event
def on_focus_out(event):
    if entry_task.get() == '':
        entry_task.insert(0, 'Enter task here...')
        entry_task.config(fg='blue')


# Function to add a task to the list
def add_task(event=None):
    task = entry_task.get().strip()
    if task and task != "Enter task here...":
        listbox_tasks.insert(tkin.END, task)
        entry_task.delete(0, tkin.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


# Function to delete the selected task from the list
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


# Function to delete all tasks from the list
def delete_all_tasks():
    confirm = messagebox.askyesno("Delete All Tasks", "Are you sure you want to delete all tasks?")
    if confirm:
        listbox_tasks.delete(0, tkin.END)


# Function to save tasks to a file
def save_task():
    with open("tasks.txt", "w") as f:
        for i in range(listbox_tasks.size()):
            task = listbox_tasks.get(i)
            bg_color = listbox_tasks.itemcget(i, "background")
            f.write(f"{task},{bg_color}\n")


# Function to update the selected task with new text
def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = entry_task.get()
        if task != "" and task != "Enter task here...":
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task)
            entry_task.delete(0, tkin.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")


# Function to mark the selected task as complete
def mark_complete():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg': 'pink'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")


# Function to exit the application
def exit_application():
    confirm = messagebox.askyesno("Exit Application", "Do you want to exit the application?")
    if confirm:
        window.destroy()


# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                task = data[0]
                bg_color = data[1] if len(data) > 1 else ''
                listbox_tasks.insert(tkin.END, task)
                if bg_color == 'green':
                    listbox_tasks.itemconfig(tkin.END, {'bg': bg_color})
    except FileNotFoundError:
        pass


# Creating the main window
window = tkin.Tk()
window.title("To-Do List")
window.configure(bg="cyan")
window.geometry('550x320')

# Creating an entry widget for task input
entry_task = tkin.Entry(window, width=35, bg="lightyellow", fg="blue",font=('Arial',12))
entry_task.pack(side=tkin.TOP, pady=10)
entry_task.insert(0, 'Enter task here...')
entry_task.bind('<FocusIn>', on_entry_click)
entry_task.bind('<FocusOut>', on_focus_out)
entry_task.bind("<Return>", add_task)

# Creating a listbox to display tasks
listbox_tasks = tkin.Listbox(window, height=5, width=100, bg="lightblue",font=('Arial',12))
listbox_tasks.pack(side=tkin.LEFT, expand=True,fill=tkin.BOTH,padx=5,pady=5)

# Create a scrollbar for the listbox
scrollbar_tasks = tkin.Scrollbar(listbox_tasks, orient=tkin.VERTICAL)
scrollbar_tasks.pack(side=tkin.RIGHT, fill=tkin.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create buttons for various actions
button_add_task = tkin.Button(window, text="Add Task", width=10, command=add_task,bg='violet',font=('Arial',12))
button_add_task.pack(pady=5)

button_delete_task = tkin.Button(window, text="Delete Task", width=10, command=delete_task,bg='red',font=('Arial',12))
button_delete_task.pack(pady=5)

button_delete_all_tasks = tkin.Button(window, text="Delete All Tasks", width=15, command=delete_all_tasks,bg='yellow',font=('Arial',12))
button_delete_all_tasks.pack(pady=5)

button_update_task = tkin.Button(window, text="Update Task", width=10, command=update_task,bg='blue',font=('Arial',12))
button_update_task.pack(pady=5)

button_mark_complete = tkin.Button(window, text="Mark Complete", width=12, command=mark_complete,bg='green',font=('Arial',12))
button_mark_complete.pack(pady=5)


button_save = tkin.Button(window, text="Save", width=10, command=save_task,bg='white',font=('Arial',12))
button_save.pack(side=tkin.LEFT, padx=5, pady=5)

button_exit = tkin.Button(window, text="Close",width=10, command=exit_application,bg='white',font=('Arial',12))
button_exit.pack(side=tkin.RIGHT, padx=5, pady=5)

# Load tasks from the file and start the main loop
load_tasks()
window.mainloop()
