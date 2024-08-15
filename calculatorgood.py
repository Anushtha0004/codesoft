import tkinter as tk

def click(event):
    text=event.widget.cget("text")
    if text == "=":
        try:
            result=eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
            screen.update()
    elif text =="C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get()+ text)

    screen.update()

root=tk.Tk()
root.geometry("200x300")
root.title("Calculator")

screen_var=tk.StringVar()
screen_var.set("")
screen=tk.Entry(root,textvar=screen_var, font = "lucida 25 bold")
screen.pack(fill=tk.BOTH,ipadx=5,pady=5,padx=5)

button_frame=tk.Frame(root)
button_frame.pack()
buttons=[
'7','8','9','+',
'4','5','6','-',
'1','2','3','*',
'C','0','=','/',
]

row=0
col=0
for button in buttons:
    btn=tk.Button(button_frame,text=button,font="lucida 15 bold")
    btn.grid(row=row,column=col,padx=5,pady=5,ipadx=5,ipady=5)
    btn.bind("<Button-1>",click)
    col+=1
    if col>3:
        col=0
        row+=1

root.mainloop()
 