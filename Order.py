from OrderItem import OrderItem
from datetime import datetime

class Order:
  nextID = 10000

  def __init__(self, customer):
    self.__customer = customer

    self.__orderID = Order.nextID
    Order.nextID += 1

    self.__date = datetime.now()
    self.__orderItems = []

  # Getter and setter for customer
  @property
  def customer(self):
    return self.__customer
  
  @customer.setter
  def customer(self, value):
    self.__customer = value

  # Getter and setter for orderID
  @property
  def id(self):
    return self.__orderID
  
  @id.setter
  def id(self, value):
    self.__orderID = value

  # Getter and setter for date
  @property
  def date(self):
    return self.__date
  
  @date.setter
  def date(self, value):
    self.__date = value

  # Getter for orderItems
  @property
  def items(self):
    return self.__orderItems
  
  #Add an order item to the order.
  def add(self, orderItem):
    '''Add an order item to the order.'''
    self.__orderItems.append(orderItem)
  
  #Calculate the total price of the order.
  @property
  def total(self):
        total = 0
        for item in self.__orderItems:
            total += item.price
        return total
  
  #Display the order ID, Customer, date, and order items.
  def __str__(self):
    '''Display the order ID, date, and order items.'''
    formattedDate = self.date.strftime("%d-%m-%Y %H:%M:%S")
    items = ''
    for item in self.__orderItems:
        items += f'{item}\n'
    return (f'Order ID: {self.id}\n'
            f'Customer: {self.customer.name}\n'
            f'Date: {formattedDate}\n'
            f'Order Items:\n{items}\n'
            f'Total Price: ${self.total}')