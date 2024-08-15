import tkinter as tk
from tkinter import messagebox

def add_task():
    task=task_entry.get()
    if task !="":
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","You must enter a task.")

def delete_task():
        try:
            selected_task_index=task_listbox.curselection()[0]
            task_listbox.delete(selected_task_index)
        except:
            messagebox.showwarning("Warning","You must select a task to delete.")

def clear_all_tasks():
    task_listbox.delete(0,tk.END)

root=tk.Tk()
root.title("To-Do List")

task_frame=tk.Frame(root)
task_frame.pack(pady=10)

task_label=tk.Label(task_frame,text="Task:")
task_label.pack(side=tk.LEFT, padx=5)

task_entry=tk.Entry(task_frame,width=35)
task_entry.pack(side=tk.LEFT,padx=5)

add_task_button=tk.Button(task_frame,text="Add Task", command=add_task) 
add_task_button.pack(side=tk.LEFT,padx=5)

listbox_frame=tk.Frame(root)
listbox_frame.pack(pady=10)

task_listbox=tk.Listbox(listbox_frame,height=15, width=50, bg="light yellow",fg="black",selectbackground="gray",selectforeground="white")
task_listbox.pack(side=tk.LEFT,fill=tk.BOTH)

scrollbar=tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

action_frame=tk.Frame(root)
action_frame.pack(pady=10)

delete_task_button=tk.Button(action_frame,text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT,padx=10)

clear_task_button=tk.Button(action_frame,text="Clear All Tasks", command=clear_all_tasks)
clear_task_button.pack(side=tk.LEFT,padx=10)

root.mainloop()