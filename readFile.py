from Customer import Customer
from Product import Product

customerFileName = open("customer.txt", "r")
productFileName = open("product.txt", "r")

def getCustomerList():
    '''Read the customer.txt file and return a list of Customer objects.'''
    cList = []
    with open("customer.txt", "r") as customerFile:
        for line in customerFile:
            data = line.strip()
            customer = Customer(data)
            cList.append(customer)
    return cList

def getProductList():
    '''Read the product.txt file and return a list of Product objects.'''
    pList = []
    with open("product.txt", "r") as productFile:
        for line in productFile:
            data = line.strip().split(", ")
            pName = data[0]
            pPrice = float(data[1])
            product = Product(pName, pPrice)
            pList.append(product)
    return pList