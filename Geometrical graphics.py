from tkinter import *

root=Tk()
root.geometry("622x433")

def getvalue():
    print("Thank you for attending our demo class.")

Label(root, text="Welcome to our organisation..", font="comicsansms 12 bold", pady=25).grid(row=0, column=3)

name=Label(root, text="Name")
mobilenumber=Label(root, text="Mobile Number")
gender=Label(root, text="Gender")
mailid=Label(root, text="Mail id")
state=Label(root, text="State")

name.grid(row=1, column=2)
mobilenumber.grid(row=2, column=2)
gender.grid(row=3, column=2)
mailid.grid(row=4, column=2)
state.grid(row=5, column=2)

namevalue=StringVar()
mobilenumbervalue=StringVar()
gendervalue=StringVar()
mailidvalue=StringVar()
statevalue=StringVar()
demovalue=IntVar()

nameentry=Entry(root, textvariable=namevalue)
mobilenumberentry=Entry(root, textvariable=mobilenumbervalue)
genderentry=Entry(root, textvariable=gendervalue)
mailidentry=Entry(root, textvariable=mailidvalue)
stateentry=Entry(root, textvariable=statevalue)

nameentry.grid(row=1, column= 3)
mobilenumberentry.grid(row=2, column= 3)
genderentry.grid(row=3, column= 3)
mailidentry.grid(row=4, column= 3)
stateentry.grid(row=5, column= 3)

Checkbutton(text="Do you want to attend Demo?", variable=demovalue).grid(row=6, column=3)

Button(text="Submit", command= getvalue).grid(row=7, column=3)


root.mainloop()