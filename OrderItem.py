from Product import Product

class OrderItem:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity


    # Getter and setter for product
    @property
    def product(self):
        return self.__product
    
    @product.setter
    def product(self, value):
        self.__product = value

    # Getter and setter for quantity
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity cannot be negative or zero.")
        if value > 100:
            raise ValueError("Quantity cannot exceed 100. If you order more than 100, please contact customer service.")
        self.__quantity = value

    # Calculate the gross price, GST, and net price of the order item.
    def calcPrice(self):
        '''Calculate the gross price, GST, and net price of the order item.'''
        grossPrice = self.product.productPrice * self.quantity
        gst = grossPrice * 0.15
        netPrice = grossPrice + gst
        return netPrice
    
    # Display the product name and cost per item.
    def __str__(self):
        '''Display the product name and cost per item.'''
        return f'You have ordered {self.quantity} of {self.product.productName}, which totals ${self.calcPrice()}.'