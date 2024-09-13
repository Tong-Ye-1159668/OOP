import tkinter as tk
from tkinter import ttk, messagebox
from Controller import Controller

# Colors and global styles
sidebar_colour = '#283662'
background_colour = 'white'
highlight_colour = '#6fffe9'  # A different color for the "Add New Order" button

class LOSApp:
    def __init__(self, root, controller):
        self.Controller = controller
        self.root = root
        self.root.title('Lincoln Office Supplies Order System Ver 1.0')

        # Set window size and layout
        self.root.geometry("1280x720")
        self.root.minsize(960, 540)
        self.root.maxsize(1920, 1080)

        # Load the images
        self.logo = tk.PhotoImage(file='images\\LOS_logo.png')
        self.icon = tk.PhotoImage(file='images\\LOS_icon.png')
        self.add_order_icon = tk.PhotoImage(file='images\\add_order.png')
        self.orders_icon = tk.PhotoImage(file='images\\customer_orders.png')
        self.payments_icon = tk.PhotoImage(file='images\\customer_payments.png')
        self.customers_icon = tk.PhotoImage(file='images\\all_customers.png')
        self.all_orders_icon = tk.PhotoImage(file='images\\all_orders.png')
        self.all_payments_icon = tk.PhotoImage(file='images\\all_payments.png')
        self.root.iconphoto(True, self.icon)

        # Sidebar
        sidebar = tk.Frame(root, bg=sidebar_colour)
        sidebar.place(relx=0, rely=0, relwidth=0.25, relheight=1)

        # LOS Logo and Brand
        brand_frame = tk.Frame(sidebar, bg=sidebar_colour)
        brand_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.LOS_logo = self.logo.subsample(2, 2)
        logo_label = tk.Label(brand_frame, image=self.LOS_logo, bg=sidebar_colour)
        logo_label.place(x=12, y=10)

        # Create submenu in the sidebar
        submenu_frame = tk.Frame(sidebar, bg=sidebar_colour)
        submenu_frame.place(relx=0, rely=0.15, relwidth=1, relheight=1)

        # Add New Order button
        add_order_button = tk.Button(submenu_frame, text=" Add New Order", bg=highlight_colour, font=("Arial", 17, "bold"),
                                     image=self.add_order_icon, compound=tk.LEFT, bd=0, cursor='hand2',
                                     fg="#1c2541", activebackground='#affc41', activeforeground="#1c2541", anchor="w")
        add_order_button.place(x=30, y=40, width=215, height=60)
        add_order_button.config(command=lambda: self.show_frame(self.frame1))

        # List Customer Orders button
        customer_orders_button = tk.Button(submenu_frame, text=" List Customer Orders", bg=sidebar_colour, font=("Arial", 14, "bold"),
                                           image=self.orders_icon, compound=tk.LEFT, bd=0, cursor='hand2',
                                           fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
        customer_orders_button.place(x=30, y=140, width=260, height=60)
        customer_orders_button.config(command=lambda: self.show_frame(self.frame2))

        # List Customer Payments button
        customer_payments_button = tk.Button(submenu_frame, text=" List Customer Payments", bg=sidebar_colour, font=("Arial", 14, "bold"),
                                             image=self.payments_icon, compound=tk.LEFT, bd=0, cursor='hand2',
                                             fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
        customer_payments_button.place(x=30, y=190, width=260, height=60)
        customer_payments_button.config(command=lambda: self.show_frame(self.frame3))

        # List All Customers button
        all_customers_button = tk.Button(submenu_frame, text=" List All Customers", bg=sidebar_colour, font=("Arial", 14, "bold"),
                                         image=self.customers_icon, compound=tk.LEFT, bd=0, cursor='hand2',
                                         fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
        all_customers_button.place(x=30, y=240, width=260, height=60)
        all_customers_button.config(command=lambda: self.show_frame(self.frame4))

        # List All Orders button
        all_orders_button = tk.Button(submenu_frame, text=" List All Orders", bg=sidebar_colour, font=("Arial", 14, "bold"),
                                      image=self.all_orders_icon, compound=tk.LEFT, bd=0, cursor='hand2',
                                      fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
        all_orders_button.place(x=30, y=290, width=260, height=60)
        all_orders_button.config(command=lambda: self.show_frame(self.frame5))

        # List All Payments button
        all_payments_button = tk.Button(submenu_frame, text=" List All Payments", bg=sidebar_colour, font=("Arial", 14, "bold"),
                                        image=self.all_payments_icon, compound=tk.LEFT, bd=0, cursor='hand2',
                                        fg="white", activebackground='#4361ee', activeforeground="white", anchor="w")
        all_payments_button.place(x=30, y=340, width=260, height=60)
        all_payments_button.config(command=lambda: self.show_frame(self.frame6))

        # Reset button
        reset_button = tk.Button(sidebar, text="Reset", bg='#ef233c', fg='white', font=("Arial", 14, "bold"),
                                 bd=0, activebackground='#fca311', activeforeground="white", command=self.reset_frame1)
        reset_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        # ---------------- MAIN CONTENT --------------------
        container = tk.Frame(root)
        container.place(relx=0.25, rely=0, relwidth=0.75, relheight=1)

        # Define frames for each page
        self.frame1 = tk.Frame(container, bg=background_colour)
        self.frame2 = tk.Frame(container, bg=background_colour)
        self.frame3 = tk.Frame(container, bg=background_colour)
        self.frame4 = tk.Frame(container, bg=background_colour)
        self.frame5 = tk.Frame(container, bg=background_colour)
        self.frame6 = tk.Frame(container, bg=background_colour)

        for frame in [self.frame1, self.frame2, self.frame3, self.frame4, self.frame5, self.frame6]:
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Initialize the first frame (Add New Order Page)
        self.setup_frame1()

        # Show the first frame by default
        self.show_frame(self.frame1)

    def setup_frame1(self):
        # Setup the layout for the "Add New Order" page
        customer_info_frame = tk.LabelFrame(self.frame1, text="Customer Information", bg=background_colour, padx=10, pady=10)
        customer_info_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

        customer_label = tk.Label(customer_info_frame, text="Select Customer:", bg=background_colour)
        customer_label.grid(row=0, column=0, sticky="w")

        self.customer_combobox = ttk.Combobox(customer_info_frame, values=[customer.customerName for customer in self.Controller.customers])
        self.customer_combobox.grid(row=0, column=1, padx=10)

        self.customer_info_text = tk.Text(customer_info_frame, height=2, width=40, bg="#e0ffff")
        self.customer_info_text.insert(tk.END, "Customer information will be displayed here.")
        self.customer_info_text.grid(row=0, column=2, padx=10)

        new_order_button = tk.Button(customer_info_frame, text="New Order", command=self.create_new_order)
        new_order_button.grid(row=0, column=3, padx=10)

        # Process Order Section
        process_order_frame = tk.LabelFrame(self.frame1, text="Process Order", bg=background_colour, padx=10, pady=10)
        process_order_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.2)

        product_label = tk.Label(process_order_frame, text="Select Product:", bg=background_colour)
        product_label.grid(row=0, column=0, sticky="w")

        self.product_combobox = ttk.Combobox(process_order_frame, values=[product.productName for product in self.Controller.products])
        self.product_combobox.grid(row=0, column=1, padx=10)

        quantity_label = tk.Label(process_order_frame, text="Quantity:", bg=background_colour)
        quantity_label.grid(row=0, column=2, sticky="w")

        self.quantity_entry = tk.Entry(process_order_frame)
        self.quantity_entry.grid(row=0, column=3, padx=10)

        add_product_button = tk.Button(process_order_frame, text="Add Product", command=self.add_product)
        add_product_button.grid(row=0, column=4, padx=10)

        # Order Details Section
        order_details_frame = tk.LabelFrame(self.frame1, text="Order Details", bg=background_colour, padx=10, pady=10)
        order_details_frame.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.25)

        self.order_details_text = tk.Text(order_details_frame, height=8, width=80, bg="#e0ffff")
        self.order_details_text.grid(row=0, column=0)

        submit_order_button = tk.Button(order_details_frame, text="Submit Order", command=self.submit_order)
        submit_order_button.grid(row=0, column=1, padx=10)

        # Payment Section
        process_payment_frame = tk.LabelFrame(self.frame1, text="Process Payment", bg=background_colour, padx=10, pady=10)
        process_payment_frame.place(relx=0.05, rely=0.85, relwidth=0.9, relheight=0.1)

        payment_label = tk.Label(process_payment_frame, text="Payment Amount", bg=background_colour)
        payment_label.grid(row=0, column=0, sticky="w")

        self.payment_entry = tk.Entry(process_payment_frame)
        self.payment_entry.grid(row=0, column=1, padx=10)

        pay_button = tk.Button(process_payment_frame, text="Pay", command=self.process_payment)
        pay_button.grid(row=0, column=2, padx=10)

    

    def show_frame(self, frame):
        frame.tkraise()

    def reset_frame1(self):
        self.show_frame(self.frame1)
        self.customer_combobox.set('')
        self.customer_info_text.delete(1.0, tk.END)
        self.product_combobox.set('')
        self.quantity_entry.delete(0, tk.END)
        self.order_details_text.delete(1.0, tk.END)
        self.payment_entry.delete(0, tk.END)

    def create_new_order(self):
        customer_name = self.customer_combobox.get()
        customer = self.Controller.find_customer_by_name(customer_name)
        if customer:
            self.order = self.Controller.create_order(customer.id)
            messagebox.showinfo("Order Created", f"New order created for {customer_name}.")
        else:
            messagebox.showerror("Error", "Customer not found.")

    def add_product(self):
        product_name = self.product_combobox.get()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be an integer.")
            return

        if self.order:
            product = self.Controller.find_product_by_name(product_name)
            if product:
                self.Controller.add_order_item(self.order, product.id, quantity)
                self.order_details_text.insert(tk.END, f"{product_name} - {quantity} units added to order.\n")
            else:
                messagebox.showerror("Error", "Product not found.")
        else:
            messagebox.showerror("Error", "Please create an order first.")

    def submit_order(self):
        if self.order:
            self.Controller.submit_order(self.order)
            messagebox.showinfo("Order Submitted", "Your order has been submitted successfully.")
            self.order_details_text.delete(1.0, tk.END)
        else:
            messagebox.showerror("Error", "No active order to submit.")

    def process_payment(self):
        customer_name = self.customer_combobox.get()
        try:
            amount = float(self.payment_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Payment amount must be a number.")
            return

        customer = self.Controller.find_customer_by_name(customer_name)
        if customer:
            self.Controller.make_payment(customer.id, amount)
            messagebox.showinfo("Payment Processed", f"Payment of ${amount:.2f} processed successfully.")
        else:
            messagebox.showerror("Error", "Customer not found.")
