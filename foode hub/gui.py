from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from twilio.rest import Client
from tkinter import messagebox
import random, webbrowser
from tkinter import PhotoImage


def kfc():
    cart = []

    def add_item_to_cart(item_name, item_price):
        cart.append((item_name, item_price))
        update_cart_display()

    def remove_item_from_cart(index):
        del cart[index]
        update_cart_display()

    def update_cart_display():
        total_price = 0
        cart_listbox.delete(0, tk.END)
        for i, (item_name, item_price) in enumerate(cart, start=1):
            total_price += item_price
            cart_listbox.insert(tk.END, f"{i}. {item_name} - ${item_price}")

        total_label.config(text=f"Total Price: ${total_price:.2f}")

    def generate_kfc_bill():
        kfc_bill = Toplevel()
        kfc_bill.geometry("400x400")
        kfc_bill.title("KFC Bill")

        title = tk.Label(kfc_bill, text="KFC Bill", font=("ariel", 20))
        title.pack()

        for item_name, item_price in cart:
            tk.Label(kfc_bill, text=f"{item_name} - ${item_price}", font=("ariel", 12)).pack()

        total_price = sum(item_price for _, item_price in cart)
        tk.Label(kfc_bill, text=f"Total Price: ${total_price:.2f}", font=("ariel", 16)).pack()
        kfc_pay = tk.Button(kfc_bill,text="payment", font=("ariel",10),command=pay)
        kfc_pay.place(x=200,y=300)

    # Create the main window
    root = tk.Tk()
    root.geometry("800x800")
    root.configure(bg="#EAFAF1")
    root.title("Food Ordering")

    # Create a Label to display the total price
    total_label = tk.Label(root, text="Total Price: $0.00", font=("ariel", 16))
    total_label.place(x= 600 , y= 50)

    # Create a Listbox to display the cart
    cart_listbox = tk.Listbox(root)
    cart_listbox.place(x= 600, y= 90)

    # Create "Open KFC" button
    title = tk.Label(root, text="KFC", font=("ariel", 20))
    title.pack(pady=40)
    menu_items = [
    ("Fried Wings", 99),
    ("4 pc hot&crispy", 380),
    ("Boneless Strips", 299),
    ("4 pc hot wings", 480),
    ("popcorn chicken", 380)
]

    for item_name, item_price in menu_items:
        tk.Button(root, text=f"{item_name} - ₹{item_price}", font=("ariel", 12), command=lambda name=item_name, price=item_price: add_item_to_cart(name, price)).pack()
    # Add a space (empty Label) between items
        tk.Label(root, text="", font=("ariel", 12)).pack()
        tk.Label(root, text="", font=("ariel", 12)).pack()

    # chechout
    kfc_checkout_button = tk.Button(root, text="Checkout", command=generate_kfc_bill)
    kfc_checkout_button.place(x= 600, y= 500)
 


    # Create a Remove Item button
    remove_button = tk.Button(root, text="Remove Item", command=lambda: remove_item_from_cart(cart_listbox.curselection()[0]))
    remove_button.place(x= 600,y= 300 )

    root.mainloop()

def hut():
    cart = []

    def add_item_to_cart(item_name, item_price):
        cart.append((item_name, item_price))
        update_cart_display()

    def remove_item_from_cart(index):
        del cart[index]
        update_cart_display()

    def update_cart_display():
        total_price = 0
        cart_listbox.delete(0, tk.END)
        for i, (item_name, item_price) in enumerate(cart, start=1):
            total_price += item_price
            cart_listbox.insert(tk.END, f"{i}. {item_name} - ${item_price}")

        total_label.config(text=f"Total Price: ${total_price:.2f}")

    def generate_hut_bill():
        hut_bill = Toplevel()
        hut_bill.geometry("400x400")
        hut_bill.title("hut Bill")

        title = tk.Label(hut_bill, text="hut Bill", font=("ariel", 20))
        title.pack()

        for item_name, item_price in cart:
            tk.Label(hut_bill, text=f"{item_name} - ${item_price}", font=("ariel", 12)).pack()

        total_price = sum(item_price for _, item_price in cart)
        tk.Label(hut_bill, text=f"Total Price: ${total_price:.2f}", font=("ariel", 16)).pack()

        hut_pay = tk.Button(hut_bill,text="payment", font=("ariel",10),command= pay)
        hut_pay.place(x=200,y=300)
    # Create the main window
    root = tk.Tk()
    root.geometry("800x800")
    root.configure(bg="#BDC3C7")
    root.title("Food Ordering")

    # Create a Label to display the total price
    total_label = tk.Label(root, text="Total Price: $0.00", font=("ariel", 16))
    total_label.place(x= 600 , y= 50)

    # Create a Listbox to display the cart
    cart_listbox = tk.Listbox(root)
    cart_listbox.place(x= 600, y= 90)

    # Create "Open hut" button
    title = tk.Label(root, text="hut", font=("ariel", 20))
    title.pack(pady=40)
    menu_items = [
    ("Fried Wings", 99),
    ("4 pc hot&crispy", 380),
    ("Boneless Strips", 299),
    ("4 pc hot wings", 480),
    ("popcorn chicken", 380)
]

    for item_name, item_price in menu_items:
        tk.Button(root, text=f"{item_name} - ₹{item_price}", font=("ariel", 12), command=lambda name=item_name, price=item_price: add_item_to_cart(name, price)).pack()
    # Add a space (empty Label) between items
        tk.Label(root, text="", font=("ariel", 12)).pack()
        tk.Label(root, text="", font=("ariel", 12)).pack()

    # chechout
    hut_checkout_button = tk.Button(root, text="Checkout", command=generate_hut_bill)
    hut_checkout_button.place(x= 600, y= 500)
 


    # Create a Remove Item button
    remove_button = tk.Button(root, text="Remove Item", command=lambda: remove_item_from_cart(cart_listbox.curselection()[0]))
    remove_button.place(x= 600,y= 300 )

    root.mainloop()

def dom():
    cart = []

    def add_item_to_cart(item_name, item_price):
        cart.append((item_name, item_price))
        update_cart_display()

    def remove_item_from_cart(index):
        del cart[index]
        update_cart_display()

    def update_cart_display():
        total_price = 0
        cart_listbox.delete(0, tk.END)
        for i, (item_name, item_price) in enumerate(cart, start=1):
            total_price += item_price
            cart_listbox.insert(tk.END, f"{i}. {item_name} - ${item_price}")

        total_label.config(text=f"Total Price: ${total_price:.2f}")

    def generate_dom_bill():
        dom_bill = Toplevel()
        dom_bill.geometry("400x400")
        dom_bill.title("dom Bill")

        title = tk.Label(dom_bill, text="dom Bill", font=("ariel", 20))
        title.pack()

        for item_name, item_price in cart:
            tk.Label(dom_bill, text=f"{item_name} - ${item_price}", font=("ariel", 12)).pack()

        total_price = sum(item_price for _, item_price in cart)
        tk.Label(dom_bill, text=f"Total Price: ${total_price:.2f}", font=("ariel", 16)).pack()
        dom_pay = tk.Button(dom_bill,text="payment", font=("ariel",10),command= pay)
        dom_pay.place(x=200,y=300)


    # Create the main window
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Food Ordering")

    # Create a Label to display the total price
    total_label = tk.Label(root, text="Total Price: $0.00", font=("ariel", 16))
    total_label.place(x= 600 , y= 50)

    # Create a Listbox to display the cart
    cart_listbox = tk.Listbox(root)
    cart_listbox.place(x= 600, y= 90)

    # Create "Open dom" button
    title = tk.Label(root, text="dom", font=("ariel", 20))
    title.pack(pady=40)
    menu_items = [
    ("Fried Wings", 99),
    ("4 pc hot&crispy", 380),
    ("Boneless Strips", 299),
    ("4 pc hot wings", 480),
    ("popcorn chicken", 380)
]

    for item_name, item_price in menu_items:
        tk.Button(root, text=f"{item_name} - ₹{item_price}", font=("ariel", 12), command=lambda name=item_name, price=item_price: add_item_to_cart(name, price)).pack()
    # Add a space (empty Label) between items
        tk.Label(root, text="", font=("ariel", 12)).pack()
        tk.Label(root, text="", font=("ariel", 12)).pack()

    # chechout
    dom_checkout_button = tk.Button(root, text="Checkout", command=generate_dom_bill)
    dom_checkout_button.place(x= 600, y= 500)



    # Create a Remove Item button
    remove_button = tk.Button(root, text="Remove Item", command=lambda: remove_item_from_cart(cart_listbox.curselection()[0]))
    remove_button.place(x= 600,y= 300 )

    root.mainloop()

def king():
    cart = []

    def add_item_to_cart(item_name, item_price):
        cart.append((item_name, item_price))
        update_cart_display()

    def remove_item_from_cart(index):
        del cart[index]
        update_cart_display()

    def update_cart_display():
        total_price = 0
        cart_listbox.delete(0, tk.END)
        for i, (item_name, item_price) in enumerate(cart, start=1):
            total_price += item_price
            cart_listbox.insert(tk.END, f"{i}. {item_name} - ${item_price}")

        total_label.config(text=f"Total Price: ${total_price:.2f}")

    def generate_king_bill():
        king_bill = Toplevel()
        king_bill.geometry("400x400")
        king_bill.title("king Bill")

        title = tk.Label(king_bill, text="king Bill", font=("ariel", 20))
        title.pack()

        for item_name, item_price in cart:
            tk.Label(king_bill, text=f"{item_name} - ${item_price}", font=("ariel", 12)).pack()

        total_price = sum(item_price for _, item_price in cart)
        tk.Label(king_bill, text=f"Total Price: ${total_price:.2f}", font=("ariel", 16)).pack()

        king_pay = tk.Button(king_bill,text="payment", font=("ariel",10),command= pay)
        king_pay.place(x=200,y=300)

    # Create the main window
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Food Ordering")

    # Create a Label to display the total price
    total_label = tk.Label(root, text="Total Price: $0.00", font=("ariel", 16))
    total_label.place(x= 600 , y= 50)

    # Create a Listbox to display the cart
    cart_listbox = tk.Listbox(root)
    cart_listbox.place(x= 600, y= 90)

    # Create "Open king" button
    title = tk.Label(root, text="king", font=("ariel", 20))
    title.pack(pady=40)
    menu_items = [
    ("Fried Wings", 99),
    ("4 pc hot&crispy", 380),
    ("Boneless Strips", 299),
    ("4 pc hot wings", 480),
    ("popcorn chicken", 380)
]

    for item_name, item_price in menu_items:
        tk.Button(root, text=f"{item_name} - ₹{item_price}", font=("ariel", 12), command=lambda name=item_name, price=item_price: add_item_to_cart(name, price)).pack()
    # Add a space (empty Label) between items
        tk.Label(root, text="", font=("ariel", 12)).pack()
        tk.Label(root, text="", font=("ariel", 12)).pack()

    # chechout
    king_checkout_button = tk.Button(root, text="Checkout", command=generate_king_bill)
    king_checkout_button.place(x= 600, y= 500)
 


    # Create a Remove Item button
    remove_button = tk.Button(root, text="Remove Item", command=lambda: remove_item_from_cart(cart_listbox.curselection()[0]))
    remove_button.place(x= 600,y= 300 )

    root.mainloop()
def pay():
    def back():
        card = tk.Button(payment, text="CREDIT/DEBIT CARD", command=payment_window)
        card.place(x=187, y=150)
        upi = tk.Button(payment, text="UPI PAYMENT")
        upi.place(x=187, y=220)
    def payment_window():
        def generate_otp():
            return str(random.randint(1000, 9999))
        def send_otp_via_twilio(phone_number, otp):
            try:
                twilio_client.messages.create(
                    to=phone_number,
                    from_=TWILIO_PHONE_NUMBER,
                    body=f"Your OTP for the payment is: {otp}"
                )
            except Exception as e:
                messagebox.showerror("OTP Sending Error", f"Failed to send OTP: {str(e)}")
        def validate_otp(otp_entry, generated_otp):
            user_input = otp_entry.get()
            if user_input == generated_otp:
                messagebox.showinfo("Payment Successful", "Payment was successful!")
            else:
                messagebox.showerror("Payment Failed", "OTP is incorrect. Payment failed.")
        def submit_payment():
            card_number = card_number_entry.get()
            expiration_date = expiration_date_entry.get()
            cvv = cvv_entry.get()
            phone_number = phone_number_entry.get()
            if not card_number.strip() or not expiration_date.strip() or not cvv.strip() or not phone_number.strip():
                messagebox.showerror('Warning', 'Please fill all fields')
                return
            generated_otp = generate_otp()
            send_otp_via_twilio(phone_number, generated_otp)
            otp_window = tk.Toplevel(payment)
            otp_window.title("OTP Verification")
            otp_window.geometry("300x150")
            otp_label = tk.Label(otp_window, text="Enter OTP:")
            otp_label.pack(pady=10)
            otp_entry = tk.Entry(otp_window)
            otp_entry.pack(pady=5)
            validate_button = tk.Button(otp_window, text="Validate OTP", command=lambda: validate_otp(otp_entry, generated_otp))
            validate_button.pack(pady=10)
        # Define your Twilio credentials
        TWILIO_ACCOUNT_SID = "ACf9c1d1c731caf7aa99ecaed41db209fd"
        TWILIO_AUTH_TOKEN = "5daec4c7a031f73575b99249ad1e9283"
        TWILIO_PHONE_NUMBER = "+12513175308"
        twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        root = tk.Tk()
        root.title("Payment Details")
        root.geometry("500x500")
        card_number_label = tk.Label(root, text="Card Number:")
        card_number_label.place(x=50, y=50)
        card_number_entry = tk.Entry(root)
        card_number_entry.place(x=150, y=50)
        expiration_date_label = tk.Label(root, text="Expiration Date:")
        expiration_date_label.place(x=50, y=100)
        expiration_date_entry = tk.Entry(root)
        expiration_date_entry.place(x=150, y=100)
        cvv_label = tk.Label(root, text="CVV:")
        cvv_label.place(x=50, y=150)
        cvv_entry = tk.Entry(root)
        cvv_entry.place(x=150, y=150)
        phone_number_label = tk.Label(root, text="Phone Number:")
        phone_number_label.place(x=50, y=200)
        phone_number_entry = tk.Entry(root)
        phone_number_entry.place(x=150, y=200)
        submit_button = tk.Button(root, text="Submit Payment", command=submit_payment)
        submit_button.place(x=300, y=300)
        root.mainloop()

    payment = tk.Tk()
    payment.title("foodie hub")
    payment.geometry("500x500")
    payment.configure(bg="white")
    head = tk.Label(payment, text="Payment")
    head.place(x=200, y=40)
    back()
    payment.mainloop()
def next():
    next = tk.Toplevel()
    next.title("Foodie Hub")
    next.geometry("1000x1000")
    re = tk.Label(next, text="Restaurant", font="arial")
    re.place(x=450, y=100)

   # bc = PhotoImage(file="D:\\python workspace\\mini project\\medicen delivery mini project\\opps.py\\imge\\resize pic\\rr3.png")
    #b3 = Label(tab1, image=bc)
   # b3.place(x=0, y=0)

    r = tk.PhotoImage(file="D:\python workspace\\mini project\\medicen delivery mini project\\opps.py\\imge\\resize pic\\png's\\kfc.png")
    r1 = tk.Button(next, image=r, command= kfc)
    r1.place(x=100, y= 200)

    h = tk.PhotoImage(file="D:\\python workspace\\mini project\\medicen delivery mini project\\opps.py\\imge\\resize pic\\png's\\hut.png")
    h1 = tk.Button(next, image=h,command=hut)
    h1.place(x=600, y=200)

    d = tk.PhotoImage(file= "D:\\python workspace\\mini project\\medicen delivery mini project\opps.py\\imge\\resize pic\\png's\\dom.png")
    d1 = tk.Button(next, image=d, command = dom)
    d1.place(x=100, y=550)

    b = tk.PhotoImage(file="D:\\python workspace\\mini project\\medicen delivery mini project\\opps.py\\imge\\resize pic\\png's\\king.png")
    b1 = tk.Button(next, image=b, command = king)
    b1.place(x=600, y=550)


    next.mainloop()


tab = Tk()
tab.title("Foodie Hub")
tab.geometry("1000x1000")


a = PhotoImage(file="D:\\python workspace\\mini project\\medicen delivery mini project\\opps.py\\imge\\resize pic\\png's\\bg.png")
b = Label(tab, image=a)
b.place(x=0, y=0)

l = Label(tab, text="LOCATION", font="arial")
l.place(x=50, y=170)
e = Label(tab, text="Salem",font="arial ")
e.place(x=180, y=170)

l1 = Label(tab, text="Offer day's", font="arial")
l1.place(x=330, y=170)
com = Combobox(tab)
com["values"] = ("sunday", "wednesday", "friday")
com.place(x=460, y=170)

l3 = Label(tab, text="Ph.No", font="arial")
l3.place(x=690, y=170)
e1 = Label(tab, text="+91 8220327051",font="arial")
e1.place(x=770, y=170)

l2 = Label(tab, text="Foodie Hub", font="Sans-serif")
l2.place(x=450, y=80)


ad1 = PhotoImage(file="D:\\python workspace\\mini project\\medicen delivery mini project\\opps.py\imge\\resize pic\\png's\\k1.png")
ad2 = Label(tab, image=ad1)
ad2.place(x=100, y= 300)

ad2 = PhotoImage(file="D:\\python workspace\\mini project\\medicen delivery mini project\\opps.py\\imge\\resize pic\\png's\\hut.png")
ad3 = Label(tab, image=ad2)
ad3.place(x=600, y=300)

ad3 = PhotoImage(file= "D:\\python workspace\\mini project\\medicen delivery mini project\opps.py\\imge\\resize pic\\png's\\dom.png")
ad4 = Label(tab, image=ad3)
ad4.place(x=100, y=550)

ad4 = PhotoImage(file="D:\\python workspace\\mini project\\medicen delivery mini project\\opps.py\\imge\\resize pic\\png's\\king.png")
ad5 = Label(tab, image=ad4)
ad5.place(x=600, y=550)

n1 = Button(tab, text="NEXT", command=next)
n1.place(x=890, y= 750)









tab.mainloop()
