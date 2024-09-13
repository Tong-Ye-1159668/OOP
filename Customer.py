from Payment import Payment
from Order import Order

class Customer:
  nextID = 1000

  def __init__(self, cName):
    self.__customerName = cName

    self.__customerID = Customer.nextID
    Customer.nextID += 1
    
    self.__customerBalance = 0.00
    self.__orders = []
    self.__payments = []

  # Getter and setter for customerName
  @property
  def name(self):
    return self.__customerName
  
  @name.setter
  def name(self, value):
    self.__customerName = value

  # Getter and setter for customerID
  @property
  def id(self):
    return self.__customerID
  
  @id.setter
  def id(self, value):
    self.__customerID = value

  # Getter and setter for balance
  @property
  def balance(self):
    return self.__customerBalance
  
  @balance.setter
  def balance(self, value):
    if value < 0:
      raise ValueError("Balance cannot be negative")
    self.__customerBalance = value

  @property
  def orders(self):
    return self.__orders
  
  @property
  def payments(self):
    return self.__payments
  
  # Add order and update balance
  def addOrder(self, order):
    '''Adds a new order.'''
    self.__orders.append(order)
    # self.customerBalance += order.calcTotal()

  # Add payment and update balance
  def addPayment(self, payment):
    '''Adds a new payment.'''
    self.__payments.append(payment)
    # self.customerBalance -= payment.paymentAmount

  # Display the customer ID, name, and balance.
  def __str__(self):
    '''Display the customer ID, name, and balance.'''
    return (f'Customer ID: {self.customerID}\n'
           f'Customer Name: {self.customerName}\n'
           f'Balance: ${self.customerBalance}')
