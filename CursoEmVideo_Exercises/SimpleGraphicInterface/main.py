from tkinter import *

def printThis():
    a = 'TEXT'
    TextInWindow["text"] = a

window = Tk()#open window.

window.title('Main title.')
window.geometry("200x200")#window size.

guideText = Label(window, text='Do it to do that.')
guideText.grid(column=0, row=0, padx=10, pady=10)

button = Button(window, text='Click here', command=printThis)
button.grid(column=0, row=1, padx=10, pady=10)

TextInWindow = Label(window, text='')#print text in window.
TextInWindow.grid(column=0, row=2, padx=10, pady=10)

window.mainloop()#keep window open.