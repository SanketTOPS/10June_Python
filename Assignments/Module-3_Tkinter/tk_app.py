import tkinter
from tkinter import ttk,messagebox

window=tkinter.Tk()
window.title("MyApp")
window.geometry("400x500")
window.config(bg="lightblue")

#tkinter.Label(text="Firstname").pack()
#tkinter.Label(text="Lastname").pack()

"""tkinter.Label(text="Firstname:",bg='lightblue',fg='red',font='Cooper 15 bold').place(x=0,y=0)
tkinter.Label(text="Lastname:",bg='lightblue',fg='red',font='Cooper 15 bold').place(x=0,y=30)"""

tkinter.Label(text="Firstname:",bg='lightblue',fg='red',font='Cooper 15 bold').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",bg='lightblue',fg='red',font='Cooper 15 bold').grid(row=1,column=0,sticky='w')
tkinter.Entry().grid(row=0,column=1,sticky='w')
tkinter.Entry().grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0,text='Male',bg='lightblue',fg='red',font='Cooper 15 bold').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text='Female',bg='lightblue',fg='red',font='Cooper 15 bold').grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Gujarati",bg='lightblue',fg='red',font='Cooper 15 bold').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Hindi",bg='lightblue',fg='red',font='Cooper 15 bold').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="English",bg='lightblue',fg='red',font='Cooper 15 bold').grid(row=5,column=0,sticky='w')

city=['Rajkot','Ahmedabad','Surat','Baroda','Jamnagar']
ttk.Combobox(values=city).grid(row=6,column=0)

def btnclick():
    #print("Button Clicked!")
    #messagebox.showerror("Error!","Something went wrong...")
    #messagebox.showinfo("Success","Signup Successfully!")
    messagebox.showwarning("Warning","Your disk is full!")


tkinter.Button(text="Submit",font='Cooper 15 bold',command=btnclick).place(x=150,y=250)

window.mainloop()


