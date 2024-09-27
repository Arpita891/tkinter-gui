from tkinter import * 
import calendar

def yearly_calendar():
    window = Tk()
    window.configure(background="light yellow")
    window.title("Yearly Calendar")
    window.geometry("1000x1000")
    get_year = int(year_entry.get())
    window_content = calendar.calendar(get_year)
    year_cal = Label(window,text=window_content,font=("Arial",15,"bold"))
    year_cal.grid(row=1,column=1,padx=20)
    window.mainloop()
    

if __name__ == "__main__" :
    root = Tk()
    root.configure(background="light yellow")
    root.title("GUI Calendar")
    root.geometry("500x500")

    name = Label(root,text="Calendar" , bg="light yellow",font=("Arial",30,"bold"),padx=20,pady=20,fg="black")
    name.grid(row=0,column=1)

    year = Label(root,text="Enter Year", bg="light yellow",font=("Arial",15,"bold"),fg="black",padx=10,pady=10)
    year.grid(row=1,column=1)

    year_entry = Entry(root,font=("Arial",12,"bold"))
    year_entry.grid(row=1,column=2,padx=10,pady=10)

    cal_button = Button(root,text="Calendar",font=("Arial",12,"bold"),fg="black",bg="light blue", command=yearly_calendar)
    cal_button.grid(row=2,column=1)

    root.mainloop()