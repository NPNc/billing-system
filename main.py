from tkinter import *

root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('resource/icon.ico')

headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold'), bg='gray20', fg='gold')
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text='Customer Details', font=('Times new roman', 15, 'bold'))
customer_details_frame.pack()

nameLabel = Label(customer_details_frame, text='Name')
nameLabel.grid(row=0, column=0, padx=10, pady=5)

nameEntry = Entry(customer_details_frame, font=('arial', 15), width=18)
nameEntry.grid(row=0, column=1, padx=10, pady=5)

phoneLabel = Label(customer_details_frame, text='Phone')
phoneLabel.grid(row=0, column=2, padx=10, pady=5)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), width=18)
phoneEntry.grid(row=0, column=3, padx=10, pady=5)

root.mainloop()
