from tkinter import *
from textblob import TextBlob

def clearAll():
    word1.delete(0,END)
    word2.delete(0,END)

def correction():
    input_word = word1.get()
    blob_obj = TextBlob(input_word)
    correct_word = str(blob_obj.correct())
    word2.insert(10,correct_word)

if __name__ == "__main__" :
    root = Tk()
    root.configure(background="light blue")

    root.geometry("250x250")

    root.title("Spelling Checker")

    header = Label(root,text="Welcome to Spell Corrector Application!",fg="black",font=("Arial",25,"bold"),bg="light blue",padx=20,pady=20)
    header.grid(row=0,column=1)

    label1 = Label(root,text="Input Word",fg="black",bg="light blue",font=("Arial",15,"bold"))
    label1.grid(row=1,column=0,padx=20,pady=20)

    label2 = Label(root,text="Corrected Word",fg="black",bg="light blue",font=("Arial",15,"bold"))
    label2.grid(row=2,column=0,padx=20,pady=20)

    word1 = Entry()
    word1.grid(row=1,column=1, padx=10, pady=10)

    word2 = Entry()
    word2.grid(row=2,column=1, padx=10, pady=10)

    button = Button(root,text="Check",fg="black",bg="green",font=("Arial",10,"bold"),command=correction)
    button.grid(row=3,column=0,padx=10,pady=10)

    clearButton = Button(root,text="Clear All",bg="grey",fg="black",font=("Arial",10,"bold"),command=clearAll)
    clearButton.grid(row=3,column=1,padx=10,pady=10)
    root.mainloop()