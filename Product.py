class Product:
  def __init__(self, id, pName, pPrice):
    self.__id = id
    self.__productName = pName
    self.__productPrice = pPrice

  @property
  def id(self):
    return self.__id

# Getter and setter for productName
  @property
  def name(self):
    return self.__productName
  
  @name.setter
  def name(self, value):
    self.__productName = value

# Getter and setter for productPrice
  @property
  def price(self):
    return self.__productPrice
  
  @price.setter
  def price(self, value):
    if value <= 0:
      raise ValueError("Price cannot be negative or zero")
    self.__productPrice = value

  def __str__(self):
    return f'{self.productName}: ${self.productPrice}'