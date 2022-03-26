import tkinter
#Kwargs / Keyword Arguments are used in entire Project as Tkinter works on kwargs Inputs
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=500)
label = tkinter.Label(text = "I am a Label",font=("Calibri",24,"bold"))
label.place(x=0,y=0)
#variable_name.pack() is used to display the Label (Text on Screen)
label.pack()
#label.pack(side="right")
#Modify / Replace Old Text
label.config(text="Hello")
def button_clicked():
    print("I got Clicked")
    label.config(text="Yayy!!! I got Clicked")
    

#command keyword is used to call a function defined
button = tkinter.Button(text="Pls Click me", font=("Calibri", 18, "italic"), command=button_clicked)
button.pack()


input = tkinter.Entry(width=20)
input.pack()
def button2():
    print(button2.get())
    label.config(text=input.get())
button2 = tkinter.Button(text="I am a Button",font=("Calibri", 18, "italic"),command=button2)
button2.pack()

#Multi-Line Text
text = tkinter.Text(width=50,height=100)
text.focus()
#focus puts cursor in textbox
text.insert(tkinter.END, "Example : Write some text to begin with")
#Insert : Adds some text to begin with
print(text.get("1.0",tkinter.END))
text.pack()
def button3():
    print(input.get())
    label.config(text=input.get())
button3 = tkinter.Button(text="I am a Button",font=("Calibri", 18, "italic"),command=button3)
button3.pack()
#1.0 : Hold of Text starting from 1st Line & Character 0
window.mainloop()
