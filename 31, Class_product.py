class Product:

    def __init__(self, ProductID, Product_name, Quantity):
        self.ProductID = ProductID
        self.Product_name = Product_name
        self.Quantity = Quantity

    def show(self):
        print("Product ID:", self.ProductID)
        print("Product Name:", self.Product_name)
        print("Quantity:", self.Quantity)

P1 = Product(101, "Laptop", 10)
P2 = Product(102, "Mobile", 20)

print("Product 1 Details:")
P1.show()

print("\nProduct 2 Details:")
P2.show()