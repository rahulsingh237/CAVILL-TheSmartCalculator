from tkinter import *
from smartcalculator import calci

root = Tk()
# Icon
root.wm_iconbitmap('cal.ico')
# Width  x  Height
root.geometry("644x800")

# Fix window size
root.minsize(479,350)
root.maxsize(479,350)

# Title
root.title("CAVILL - TheSmartCalculator")



# Display 
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold") 
screen.pack(fill=X)
             

# Function
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "Calculate":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"   

        scvalue.set(value)
        print(type(text))
        screen.update()    
   
    elif text == "DEL": #scvalue=text
         try:
            fullstring = scvalue.get()
            newstring=fullstring[:-1]
            # we are replacing the last string item[-1] with blank or ""
            # String slicing method
            
            scvalue.set(newstring)

            # print(newstring)
            screen.update()
         except Exception as e:
            print(e)
             
    elif text == "voice":
        text = str(calci())
        scvalue.set(scvalue.get() + text)
        screen.update()
    elif text == "All Clear":
        scvalue.set("")
        screen.update()
    elif text == "OFF":
        sys.exit()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



#voice
"""self.loadimage = root.PhotoImage(file="voice.png")
self.roundedbutton = root.Button(self, image=self.loadimage)
self.roundedbutton["bg"] = "white"
self.roundedbutton["border"] = "0"
self.roundedbutton.pack(side="top")"""

# Frame
mFrame = Frame(root)
mFrame.pack(side=TOP, fill=X)


vframe=Frame(mFrame,relief=GROOVE)
vframe.pack(side=TOP)
b=Button(vframe,text="voice",width=20,height=3)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)
b=Button(vframe,text="All Clear",width=20,height=3)
b.grid(row=0,column=1)
b.bind("<Button-1>",click)
b=Button(vframe,text="OFF",width=20,height=3)
b.grid(row=0,column=2,padx=15)
b.bind("<Button-1>",click)

topFrame = Frame(root)
topFrame.pack(side=TOP, fill=X)


numframe=Frame(topFrame,relief=RAISED)
numframe.pack(side=LEFT,fill=X,padx=30)
b = Button(numframe,text="7",width=10,height=3)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)

b=Button(numframe,text="8",width=10,height=3)
b.grid(row=0,column=1)
b.bind("<Button-1>",click)

b=Button(numframe,text="9",width=10,height=3)
b.grid(row=0,column=2)
b.bind("<Button-1>",click)

b=Button(numframe,text="4",width=10,height=3)
b.grid(row=1,column=0)
b.bind("<Button-1>",click)

b=Button(numframe,text="5",width=10,height=3)
b.grid(row=1,column=1)
b.bind("<Button-1>",click)

b=Button(numframe,text="6",width=10,height=3)
b.grid(row=1,column=2)
b.bind("<Button-1>",click)

b=Button(numframe,text="1",width=10,height=3)
b.grid(row=2,column=0)
b.bind("<Button-1>",click)

b=Button(numframe,text="2",width=10,height=3)
b.grid(row=2,column=1)
b.bind("<Button-1>",click)

b=Button(numframe,text="3",width=10,height=3)
b.grid(row=2,column=2)
b.bind("<Button-1>",click)

b=Button(numframe,text="00",width=10,height=3)
b.grid(row=3,column=0)
b.bind("<Button-1>",click)

b=Button(numframe,text="0",width=10,height=3)
b.grid(row=3,column=1)
b.bind("<Button-1>",click)

b=Button(numframe,text=".",width=10,height=3)
b.grid(row=3,column=2)
b.bind("<Button-1>",click)


opframe=Frame(topFrame,relief=GROOVE)
opframe.pack(side=TOP,fill=X,padx=10)
b=Button(opframe,text="DEL",width=10,height=3)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)
b=Button(opframe,text="%",width=10,height=3)
b.grid(row=0,column=1)
b.bind("<Button-1>",click)
b=Button(opframe,text="+",width=10,height=3)
b.grid(row=1,column=0)
b.bind("<Button-1>",click)
b=Button(opframe,text="-",width=10,height=3)
b.grid(row=1,column=1)
b.bind("<Button-1>",click)
b=Button(opframe,text="*",width=10,height=3)
b.grid(row=2,column=0)
b.bind("<Button-1>",click)
b=Button(opframe,text="/",width=10,height=3)
b.grid(row=2,column=1)
b.bind("<Button-1>",click)



cframe=Frame(topFrame,relief=GROOVE)
cframe.pack(side=LEFT,padx=15)
b=Button(cframe,text="Calculate",width=20,height=3)
b.pack()
b.bind("<Button-1>",click)

root.mainloop()