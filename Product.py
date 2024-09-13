class Product:
  def __init__(self, pName, pPrice):
    self.__productName = pName
    self.__productPrice = pPrice

# Getter and setter for productName
  @property
  def productName(self):
    return self.__productName
  
  @productName.setter
  def productName(self, value):
    self.__productName = value

# Getter and setter for productPrice
  @property
  def productPrice(self):
    return self.__productPrice
  
  @productPrice.setter
  def productPrice(self, value):
    if value <= 0:
      raise ValueError("Price cannot be negative or zero")
    self.__productPrice = value

  def __str__(self):
    return f'{self.productName}: ${self.productPrice}'