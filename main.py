from tkinter import *

root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('resource/icon.ico')

headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold'), bg='gray20', fg='gold')
headingLabel.pack(fill=X)

# Customer Info Frame
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

billNumberLabel = Label(customer_details_frame, text='Bill Number')
billNumberLabel.grid(row=0, column=4, padx=10, pady=5)

billNumberEntry = Entry(customer_details_frame, font=('arial', 15), width=18)
billNumberEntry.grid(row=0, column=5, padx=10, pady=5)

searchButton = Button(customer_details_frame, text='Search', font=('arial', 12, 'bold'))
searchButton.grid(row=0, column=6, padx=8, pady=5)

# Products Frame
productsFrame = Frame(root)
productsFrame.pack()

fields = {
    'Cosmetics': ['Bath Soap', 'Face Cream', 'Face Wash', 'Hair Spray', 'Hair Gel', 'Body Lotion'],
    'Grocery': ['Rice', 'Oil', 'Face Wash', 'Dall', 'Wheat', 'Sugar'],
    'Cold Drinks': ['Maaza', 'Pepsi', 'Sprite', 'Dew', 'Frooti', 'Coca cola']
}

index = 0

for title, field_list in fields.items():
    frame = LabelFrame(productsFrame, text=title, font=('Times new roman', 15, 'bold'))
    frame.grid(row=0, column=index)

    for field in field_list:
        label = Label(frame, text=field, font=('time new roman', 12), width=10)
        label.grid(row=index, column=0, padx=10, pady=5)
        entry = Entry(frame, font=('time new roman', 12), width=15)
        entry.grid(row=index, column=1, padx=5, pady=5)
        index += 1

billFrame = Frame(productsFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=index)
billFrameLabel = Label(billFrame, text='Bill Display', font=('time new roman', 15, 'bold'))
billFrameLabel.pack(fill=X)
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billFrame, height=12, width=45, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billMenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'))
billMenuFrame.pack()

cosmeticPriceLabel = Label(billMenuFrame, text='Cosmetic Price', font=('times new roman', 12, 'bold'))
cosmeticPriceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
cosmeticPriceEntry = Entry(billMenuFrame, font=('time new roman', 12), width=15)
cosmeticPriceEntry.grid(row=0, column=1, padx=5, pady=5)

groceryPriceLabel = Label(billMenuFrame, text='Grocery Price', font=('times new roman', 12, 'bold'))
groceryPriceLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
groceryPriceEntry = Entry(billMenuFrame, font=('time new roman', 12), width=15)
groceryPriceEntry.grid(row=1, column=1, padx=5, pady=5)

coldDrinksPriceLabel = Label(billMenuFrame, text='Cold Drinks Price', font=('times new roman', 12, 'bold'))
coldDrinksPriceLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
coldDrinksPriceEntry = Entry(billMenuFrame, font=('time new roman', 12), width=15)
coldDrinksPriceEntry.grid(row=2, column=1, padx=5, pady=5)

cosmeticTaxLabel = Label(billMenuFrame, text='Cosmetic Tax', font=('times new roman', 12, 'bold'))
cosmeticTaxLabel.grid(row=0, column=2, pady=9, padx=10, sticky='w')
cosmeticTaxEntry = Entry(billMenuFrame, font=('time new roman', 12), width=15)
cosmeticTaxEntry.grid(row=0, column=3, padx=5, pady=5)

groceryTaxLabel = Label(billMenuFrame, text='Grocery Tax', font=('times new roman', 12, 'bold'))
groceryTaxLabel.grid(row=1, column=2, pady=9, padx=10, sticky='w')
groceryTaxEntry = Entry(billMenuFrame, font=('time new roman', 12), width=15)
groceryTaxEntry.grid(row=1, column=3, padx=5, pady=5)

coldDrinksTaxLabel = Label(billMenuFrame, text='Cold Drinks Tax', font=('times new roman', 12, 'bold'))
coldDrinksTaxLabel.grid(row=2, column=2, pady=9, padx=10, sticky='w')
coldDrinksTaxEntry = Entry(billMenuFrame, font=('time new roman', 12), width=15)
coldDrinksTaxEntry.grid(row=2, column=3, padx=5, pady=5)

buttonFrame = Frame(billMenuFrame, bd=8)
buttonFrame.grid(row=0, column=4)
totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'))
totalButton.grid(row=0, column=0,pady=10)
root.mainloop()
