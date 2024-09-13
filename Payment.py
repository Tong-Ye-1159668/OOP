from datetime import datetime

class Payment:
  def __init__(self, customer, pAmount):
    self.__customer = customer
    self.__paymentAmount = pAmount
    self.__paymentDate = datetime.now()

  # Getter and setter for customer
  @property
  def customer(self):
    return self.__customer
  
  @customer.setter
  def customer(self, value):
    self.__customer = value

  # Getter and setter for paymentAmount
  @property
  def paymentAmount(self):
    if self.__paymentAmount < 0:
      raise ValueError("Payment amount cannot be negative")
    return self.__paymentAmount
  
  @paymentAmount.setter
  def paymentAmount(self, value):
    self.__paymentAmount = value

  # Getter and setter for paymentDate
  @property
  def paymentDate(self):
    return self.__paymentDate
  
  @paymentDate.setter
  def paymentDate(self, value):
    self.__paymentDate = value

  # Display the payment date, amount, and customer name.
  def __str__(self):
    '''Display the payment date, amount, and customer name.'''
    formattedDate = self.paymentDate.strftime("%d-%m-%Y %H:%M:%S")
    return (f'Payment: \n'
            f'Customer: {self.customer.customerName}\n'
            f'Amount: ${self.paymentAmount}\n'
            f'Date: {formattedDate}')