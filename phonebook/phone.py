from tkinter import *

CONTACTS_FILE = "contacts.txt"

root = Tk()
root.geometry('500x500')
root.config(bg='Orange')
root.title('Phone-Book')
root.resizable(0, 0)

contactlist = []

Name = StringVar()
Number = StringVar()
SearchText = StringVar()

frame = Frame(root)
frame.pack(side=LEFT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=10)
scroll.config(command=select.yview)
scroll.pack(side=LEFT, fill=Y)
select.pack(side=RIGHT, fill=BOTH, expand=1)


def Selected():
    return int(select.curselection()[0] if select.curselection() else 0)


def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()
    save_contacts()


def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()
    save_contacts()


def DELETE():
    del contactlist[Selected()]
    Select_set()
    save_contacts()


def VIEW():
    try:
        NAME, PHONE = contactlist[Selected()]
        Name.set(NAME)
        Number.set(PHONE)
    except IndexError:
        pass


def EXIT():
    save_contacts()
    root.destroy()


def RESET():
    Name.set('')
    Number.set('')


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                contactlist.append([name, number])
            Select_set()
    except FileNotFoundError:
        pass


def save_contacts():
    with open(CONTACTS_FILE, 'w') as file:
        for name, number in contactlist:
            file.write(f"{name},{number}\n")


load_contacts()


def search_contact():
    search_term = SearchText.get()
    select.delete(0, END)
    for name, _ in contactlist:
        if search_term.lower() in name.lower():
            select.insert(END, name)


def clear_search():
    SearchText.set('')
    Select_set()


Label(root, text='NAME', font='arial 12 bold', bg='Yellow').place(x=30, y=20)
Entry(root, textvariable=Name).place(x=130, y=20)
Label(root, text='PHONE NO.', font='arial 12 bold', bg='Yellow').place(x=30, y=70)
Entry(root, textvariable=Number).place(x=130, y=70)

Button(root, text=" ADD", font='arial 14 bold', bg='SlateGray4', command=AddContact).place(x=200, y=175)
Button(root, text="EDIT", font='arial 14 bold', bg='SlateGray4', command=EDIT).place(x=200, y=250)
Button(root, text="DELETE", font='arial 14 bold', bg='SlateGray4', command=DELETE).place(x=300, y=250)
Button(root, text="VIEW", font='arial 14 bold', bg='SlateGray4', command=VIEW).place(x=300, y=175)
Button(root, text="EXIT", font='arial 14 bold', bg='tomato', command=EXIT).place(x=300, y=350)
Button(root, text="RESET", font='arial 14 bold', bg='SlateGray4', command=RESET).place(x=50, y=350)

Label(root, text='Search by Name:', font='arial 12 bold', bg='Yellow').place(x=30, y=120)
Entry(root, textvariable=SearchText).place(x=180, y=120)
Button(root, text="Search", font='arial 12 bold', bg='SlateGray4', command=search_contact).place(x=310, y=115)
Button(root, text="Clear", font='arial 12 bold', bg='SlateGray4', command=clear_search).place(x=390, y=115)

root.mainloop()
