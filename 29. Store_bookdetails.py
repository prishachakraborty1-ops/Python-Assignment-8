# Book 1
title1 = "Python"
author1 = "John"
price1 = 450
publisher1 = "ABC"
edition1 = 2

# Book 2
title2 = "Java"
author2 = "James"
price2 = 350
publisher2 = "XYZ"
edition2 = 3

print("Type of title:", type(title1))
print("Type of author:", type(author1))
print("Type of price:", type(price1))
print("Type of publisher:", type(publisher1))

print("\nEdition of Book 1:", edition1)
print("Edition of Book 2:", edition2)

print("\nBook 1 Details:")
print(title1, author1, price1, publisher1, edition1)

print("\nBook 2 Details:")
print(title2, author2, price2, publisher2, edition2)

if price1 < price2:
    print("\nLowest Price Book:", title1)
else:
    print("\nLowest Price Book:", title2)