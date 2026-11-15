import pandas as pd

products = pd.Series(
    [20, 40, 60, 80, 30, 100, 50, 70, 25, 90],
    index=["Rice", "Milk", "Oil", "Sugar", "Salt",
           "Tea", "Bread", "Flour", "Soap", "Coffee"]
)

print("Products with Prices:")
print(products)

avg = products.mean()
print("\nAverage Price:", avg)

print("\nProducts with price more than average:")
print(products[products > avg])

print("\nProducts with price more than 50:")
print(products[products > 50])