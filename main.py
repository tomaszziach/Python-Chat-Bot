
from tkinter import *

root = Tk()


def send():
    send = "you:"+a.get()
    text.insert(END, "\n"+send)
    if a.get() == 'hi':
        text.insert(END, "\n" + "Bot: Hello")
    elif a.get() == 'hello':
        text.insert(END, "\n" + "Bot: Hi")
    elif a.get() == 'how are you?':
        text.insert(END, "\n" + "Bot: I am fine. How are you?")
    elif a.get() == 'I am fine':
        text.insert(END, "\n" + "Nice to hear that")
    else:
        text.insert(END, "Bot: I'm sorry you must use the right statement.")


text = Text(root, bg='white')
text.grid(row=0, column=0, columnspan=2)
a = Entry(root, width=80)
send = Button(root, text='Send', bg='white', width=20, command=send).grid(row=1, column=1)
a.grid(row=1, column=0)
root.title('Simple Chat bot')
root.mainloop()
