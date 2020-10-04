from tkinter import *
from phone_number_locater import number_check


# visual variables
root = Tk()
root.title('Number locator')
root.geometry('400x200+0+0')

#heading of thw window
heading = Label(root, text = "Phone Number Locator", font = ('arial', 20, 'bold'), fg = 'steelblue')
heading.pack()

# entry prompt
entry_label = Label(root, text = "Enter your number: ", font = ('italics', 10, 'bold'), fg = 'black')
entry_label.place(x = 10, y = 100)

# entry info
number = StringVar()
entry = Entry(root, textvariable = number, width = 25, bg = 'lightgrey')
entry.place(x = 150, y = 100)

# locator command
def locator():
    location = number_check(str(number.get()))
    print('Location : ' + str(location[0]))
    print('Supplier : ' + str(location[1]))

# locate button info
locate = Button(root, text = 'locate', width = 20, height = 2, bg = 'light blue', command = locator)
locate.place(x = 150,y =  150)

# mainloop()
root.mainloop()
