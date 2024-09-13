from Customer import Customer
from Product import Product
from Order import Order
from OrderItem import OrderItem
from Payment import Payment
import readFile

class Controller:
    def __init__(self):
        self.customers = []
        self.products = []
        self.orders = []
        self.payments = []

    def load_data(self):
        # Reading customers and products from files
        self.customers = readFile.getCustomerList()
        self.products = readFile.getProductList()

    def display_customers(self):
        # Display all customers
        for customer in self.customers:
            print(customer)

    def display_products(self):
        # Display all products
        for product in self.products:
            print(product)

    def create_order(self, customer_name):
        # Create a new order for a selected customer
        customer = self.find_customer_by_name(customer_name)
        if customer:
            new_order = Order(customer)
            self.orders.append(new_order)
            return new_order
        else:
            print("Customer not found.")
            return None

    def add_order_item(self,order, product, quantity):
        if product:
            order_item = OrderItem(product, quantity)
            order.addOrderItem(order_item)
            print(f"Added {quantity} x {product.productName} to order.")
        else:
            print("Product not found.")

    def submit_order(self, order):
        # Submit the order and update customer's balance
        order.calcTotal()
        customer = order.customer
        customer.update_balance(order.total)
        print(f"Order submitted. Total: {order.total}. Updated customer balance: {customer.balance}")

    def make_payment(self, customer_name, amount):
        # Make a payment and update the balance
        customer = self.find_customer_by_name(customer_name)
        if customer:
            payment = Payment(customer, amount)
            self.payments.append(payment)
            customer.update_balance(-amount)
            print(f"Payment of {amount} made. Updated balance: {customer.balance}")
        else:
            print("Customer not found.")

    def display_customer_orders(self, customer_id):
        # Display all orders for a selected customer
        customer_orders = [order for order in self.orders if order.customer.customerID == customer_id]
        for order in customer_orders:
            print(order)

    def display_customer_payments(self, customer_id):
        # Display all payments for a selected customer
        customer_payments = [payment for payment in self.payments if payment.customer.customerID == customer_id]
        for payment in customer_payments:
            print(payment)

    def display_all_orders(self):
        # Display all orders for the company
        for order in self.orders:
            print(order)

    def display_all_payments(self):
        # Display all payments for the company
        for payment in self.payments:
            print(payment)

    def find_customer_by_name(self, customer_name):
        # Helper function to find a customer by Name
        for customer in self.customers:
            if customer.customerName == customer_name:
                return customer
        return None

    def find_product_by_name(self, product_name):
        # Helper function to find a product by ID
        for product in self.products:
            if product.productName == product_name:
                return product
        return None
