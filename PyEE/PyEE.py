from tkinter import *
from tkinter import ttk
import equivalent_RLC

root = Tk()
root.title("PyEE")
root.iconphoto(False, ee_logo)

value_list = []

checked = 0

def enter(*args):
    global value_list

    if value_list == "":
        value_list = []
        return

    if selected_option.get() == options[0]:
            
        value = specified_values.get()

        value_list.append(value)
        value_entry.delete(0, len(specified_values.get()))

    #capacitors
    elif selected_option.get() == options[1]:
            
        value = specified_values.get()

        value_list.append(value)
        value_entry.delete(0, len(specified_values.get()))

    #inductors
    elif selected_option.get() == options[2]:

        value = specified_values.get()

        value_list.append(value)
        value_entry.delete(0, len(specified_values.get()))

def calculate(*args):
    global value_list
    global checked

    print(checked)

    value_entry.delete(0, len(specified_values.get()))

    if int(checked) == 1:
        value = equivalent_RLC.n_parallel(value_list)
        equivalent_value.set(value)
        value_list = []
        return
    else:
        value = equivalent_RLC.two_parallel(value_list)
        equivalent_value.set(value)
        value_list = []
        return

def checkBox(*args):
    global checked
    checked = n_checkValue.get()
    return checked

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)

#user specified resistor resistance values
specified_values = StringVar()
value_entry = ttk.Entry(mainframe, width=7, textvariable=specified_values)
value_entry.grid(column=2, row=1, sticky=(W, E))

#checkbox for whether or not user is combining many components
n_checkValue = StringVar()
check = ttk.Checkbutton(mainframe, text='n-Combination', 
	    command=checkBox, variable=n_checkValue,
	    onvalue=1, offvalue=0)

check.grid(column=1, row=3, sticky=W)

equivalent_value = StringVar()

#results go here
results = ttk.Label(mainframe, textvariable=equivalent_value).grid(column=2, row=2, sticky=E)

ttk.Button(mainframe, text="Enter", command=enter).grid(column=4, row=1, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=2, sticky=W)

#dropdown menu
options = [
    "Parallel Resistors",
    "Series Capacitors",
    "Parallel Inductors"
    ]

selected_option = StringVar(root)
selected_option.set(options[0])

ttk.OptionMenu(mainframe, selected_option, *options).grid(column=2, row=3, sticky=(W,E))

#values label
ttk.Label(mainframe, text= "Enter Values").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="\u03A9, H, C").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="Equivalent Value(s)").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
value_entry.focus()
root.bind("<Return>", enter)
root.bind("<c>", calculate)

root.mainloop()