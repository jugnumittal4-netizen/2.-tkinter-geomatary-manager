from tkinter import *

root = Tk()
root.title('ATM')
root.geometry('350x320')

lbl = Label(root, text='Welcome to ATM', bg='black', fg='white', width=40)
lbl.pack(pady=5)

i = 3

def atm():
    Label(root, text='Welcome', bg='#3895D3', fg='white', width=25).pack(pady=2)
    Label(root, text='You have successfully logged in', bg='#3895D3', fg='white', width=30).pack(pady=2)
    Label(root, text='Please enter how much money you want to withdraw', bg='#3895D3', fg='white', wraplength=280).pack(pady=5)

    amt_box = Entry(root)
    amt_box.pack(pady=5)

    def withdraw():
        print("Here is your", amt_box.get(), "dollars")

    Button(root, text="Withdraw", command=withdraw).pack(pady=5)

def new():
    textbox = Entry(root, show='*')
    textbox.pack(pady=5)

    status_lbl = Label(root, text='', bg='#3895D3', fg='white', wraplength=280)
    status_lbl.pack(pady=5)

    def check_pin():
        global i
        if i <= 0:
            return

        if textbox.get() == "1234":
            status_lbl.config(text='Access granted')
            btn.config(state=DISABLED)
            atm()
        else:
            i -= 1
            if i == 0:
                status_lbl.config(text='Access denied. You have exceeded the maximum number of attempts')
                btn.config(state=DISABLED)
            else:
                status_lbl.config(text=f'Access denied. {i} attempts left')

    btn = Button(root, text="Submit", command=check_pin)
    btn.pack(pady=5)

def mai():
    Label(root, text='Enter your pin', bg='#3895D3', fg='white', width=20).pack(pady=5)
    new()

mai()
root.mainloop()
      
