import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import *

# -------------------------- DEFINING GLOBAL VARIABLES -------------------------

sidebar_colour = '#283662'
background_colour = 'white'
highlight_colour = '#6fffe9'  # A different color for the "Add New Order" button

# ------------------------------- ROOT WINDOW ----------------------------------

# Create the main window
root = tk.Tk()
root.geometry("1280x720")
root.minsize(960, 540)
root.maxsize(1920, 1080)
root.title('Lincoln Office Supplies Order System Ver 1.0')

# Load the images
logo = tk.PhotoImage(file='images\\LOS_logo.png')
icon = tk.PhotoImage(file='images\\LOS_icon.png')
add_order_icon = tk.PhotoImage(file='images\\add_order.png')
orders_icon = tk.PhotoImage(file='images\\customer_orders.png')
payments_icon = tk.PhotoImage(file='images\\customer_payments.png')
customers_icon = tk.PhotoImage(file='images\\all_customers.png')
all_orders_icon = tk.PhotoImage(file='images\\all_orders.png')
all_payments_icon = tk.PhotoImage(file='images\\all_payments.png')
root.iconphoto(True, icon)

# ---------------- SIDEBAR -----------------------

# Create the sidebar frame
sidebar = tk.Frame(root, bg=sidebar_colour)
sidebar.place(relx=0, rely=0, relwidth=0.25, relheight=1)

# UNIVERSITY LOGO AND NAME
brand_frame = tk.Frame(sidebar, bg=sidebar_colour)
brand_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
LOS_logo = logo.subsample(x=2, y=2)
logo_label = tk.Label(brand_frame, image=LOS_logo, bg=sidebar_colour)
logo_label.place(x=12, y=0)

# SUBMENUS IN SIDE BAR

# Function to show specific frame
def show_frame(frame):
    frame.tkraise()

# Function to reset the container
def reset_frame1():
    for widget in frame1.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        elif isinstance(widget, tk.Text):
            widget.delete('1.0', tk.END)
        elif isinstance(widget, ttk.Combobox):
            widget.set('')  # Clear the combobox selection
        elif isinstance(widget, tk.Checkbutton):
            widget.deselect()
        elif isinstance(widget, tk.Radiobutton):
            widget.deselect()


# ------------------- SIDEBAR ----------------------------

# Create submenu in the sidebar
submenu_frame = tk.Frame(sidebar, bg=sidebar_colour)
submenu_frame.place(relx=0, rely=0.15, relwidth=1, relheight=1)

# Manually create buttons with different icons

# Add New Order button
add_order_button = tk.Button(submenu_frame, text=" Add New Order", bg=highlight_colour, font=("Arial", 17, "bold"), 
                             image=add_order_icon, compound=tk.LEFT, bd=0, cursor='hand2', 
                             fg="#1c2541", activebackground='#affc41', activeforeground="#1c2541", anchor="w")
add_order_button.place(x=30, y=40, width=215, height=60)  # Adjust x, width for alignment
add_order_button.config(command=lambda: show_frame(frame1))

# List Customer Orders button
customer_orders_button = tk.Button(submenu_frame, text=" List Customer Orders", bg=sidebar_colour, font=("Arial", 14, "bold"), 
                                   image=orders_icon, compound=tk.LEFT, bd=0, cursor='hand2', 
                                   fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
customer_orders_button.place(x=30, y=140, width=260, height=60)  # Adjust x, width for alignment
customer_orders_button.config(command=lambda: show_frame(frame2))

# List Customer Payments button
customer_payments_button = tk.Button(submenu_frame, text=" List Customer Payments", bg=sidebar_colour, font=("Arial", 14, "bold"), 
                                     image=payments_icon, compound=tk.LEFT, bd=0, cursor='hand2', 
                                     fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
customer_payments_button.place(x=30, y=190, width=260, height=60)  # Adjust x, width for alignment
customer_payments_button.config(command=lambda: show_frame(frame3))

# List All Customers button
all_customers_button = tk.Button(submenu_frame, text=" List All Customers", bg=sidebar_colour, font=("Arial", 14, "bold"), 
                                 image=customers_icon, compound=tk.LEFT, bd=0, cursor='hand2', 
                                 fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
all_customers_button.place(x=30, y=240, width=260, height=60)  # Adjust x, width for alignment
all_customers_button.config(command=lambda: show_frame(frame4))

# List All Orders button
all_orders_button = tk.Button(submenu_frame, text=" List All Orders", bg=sidebar_colour, font=("Arial", 14, "bold"), 
                              image=all_orders_icon, compound=tk.LEFT, bd=0, cursor='hand2', 
                              fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
all_orders_button.place(x=30, y=290, width=260, height=60)  # Adjust x, width for alignment
all_orders_button.config(command=lambda: show_frame(frame5))

# List All Payments button
all_payments_button = tk.Button(submenu_frame, text=" List All Payments", bg=sidebar_colour, font=("Arial", 14, "bold"), 
                                image=all_payments_icon, compound=tk.LEFT, bd=0, cursor='hand2', 
                                fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
all_payments_button.place(x=30, y=340, width=260, height=60)  # Adjust x, width for alignment
all_payments_button.config(command=lambda: show_frame(frame6))

# Reset button
reset_button = tk.Button(sidebar, text="Reset", bg='#ef233c', fg='white', font=("Arial", 14, "bold"),
                         bd=0, activebackground='#fca311', activeforeground="white", command=reset_frame1)
reset_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

# --------------------  MULTI PAGE SETTINGS ----------------------------

container = tk.Frame(root)
container.place(relx=0.25, rely=0, relwidth=0.75, relheight=1)

# Define frames for each page
frame1 = tk.Frame(container, bg=background_colour)
frame2 = tk.Frame(container, bg=background_colour)
frame3 = tk.Frame(container, bg=background_colour)
frame4 = tk.Frame(container, bg=background_colour)
frame5 = tk.Frame(container, bg=background_colour)
frame6 = tk.Frame(container, bg=background_colour)

# Place frames in the container
for frame in [frame1, frame2, frame3, frame4, frame5, frame6]:
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# ------------------- Frame1 Layout ----------------------------

# --------------- Customer Information Section ---------------

customer_info_frame = tk.LabelFrame(frame1, text="Customer Information", bg=background_colour, padx=10, pady=10)
customer_info_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

customer_label = tk.Label(customer_info_frame, text="Select Customer:", bg=background_colour)
customer_label.grid(row=0, column=0, sticky="w")

customer_combobox = ttk.Combobox(customer_info_frame, values=["Karina Matthews", "Another Customer"])
customer_combobox.grid(row=0, column=1, padx=10)

customer_info_text = tk.Text(customer_info_frame, height=2, width=40, bg="#e0ffff")
customer_info_text.insert(tk.END, "Customer ID: 106\nCustomer Name: Karina Matthews\nBalance: $241.58")
customer_info_text.grid(row=0, column=2, padx=10)

new_order_button = tk.Button(customer_info_frame, text="New Order")
new_order_button.grid(row=0, column=3, padx=10)

# --------------- Process Order Section ---------------

process_order_frame = tk.LabelFrame(frame1, text="Process Order", bg=background_colour, padx=10, pady=10)
process_order_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.2)

product_label = tk.Label(process_order_frame, text="Select Product:", bg=background_colour)
product_label.grid(row=0, column=0, sticky="w")

product_combobox = ttk.Combobox(process_order_frame, values=["Post-it Notes", "Blue Ballpoint Pens", "Everyday Scissors", "Black Whiteboard Markers"])
product_combobox.grid(row=0, column=1, padx=10)

quantity_label = tk.Label(process_order_frame, text="Quantity:", bg=background_colour)
quantity_label.grid(row=0, column=2, sticky="w")

quantity_entry = tk.Entry(process_order_frame)
quantity_entry.grid(row=0, column=3, padx=10)

add_product_button = tk.Button(process_order_frame, text="Add Product")
add_product_button.grid(row=0, column=4, padx=10)

# --------------- Order Details Section ---------------

order_details_frame = tk.LabelFrame(frame1, text="Order Details", bg=background_colour, padx=10, pady=10)
order_details_frame.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.25)

order_details_text = tk.Text(order_details_frame, height=8, width=80, bg="#e0ffff")
order_details_text.insert(tk.END, "Post-it Notes--5--$79.45 Subtotal: $79.45\nBlue Ballpoint Pens Box of 50--1--$32.65 Subtotal: $112.10\nEveryday Scissors 200mm--5--$109.25 Subtotal: $221.35\nBlack Whiteboard Markers Pack of 6--1--$20.23 Subtotal: $241.58")
order_details_text.grid(row=0, column=0)

submit_order_button = tk.Button(order_details_frame, text="Submit Order")
submit_order_button.grid(row=0, column=1, padx=10)

# --------------- Process Payment Section ---------------

process_payment_frame = tk.LabelFrame(frame1, text="Process Payment", bg=background_colour, padx=10, pady=10)
process_payment_frame.place(relx=0.05, rely=0.85, relwidth=0.9, relheight=0.1)

payment_label = tk.Label(process_payment_frame, text="Payment Amount", bg=background_colour)
payment_label.grid(row=0, column=0, sticky="w")

payment_entry = tk.Entry(process_payment_frame)
payment_entry.grid(row=0, column=1, padx=10)

pay_button = tk.Button(process_payment_frame, text="Pay")
pay_button.grid(row=0, column=2, padx=10)


# Add labels to each frame
label1 = tk.Label(frame1, text='Add New Order', font=("Arial", 15), bg=background_colour)
label1.pack()

label2 = tk.Label(frame2, text='Customer Orders', font=("Arial", 15), bg=background_colour)
label2.pack()

label3 = tk.Label(frame3, text='Customer Payments', font=("Arial", 15), bg=background_colour)
label3.pack()

label4 = tk.Label(frame4, text='Customers List', font=("Arial", 15), bg=background_colour)
label4.pack()

label5 = tk.Label(frame5, text='Orders List', font=("Arial", 15), bg=background_colour)
label5.pack()

label6 = tk.Label(frame6, text='Payments List', font=("Arial", 15), bg=background_colour)
label6.pack()

# Show the initial frame
show_frame(frame1)

# Start the main loop
root.mainloop()
