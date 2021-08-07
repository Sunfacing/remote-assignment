"""
Assignment 3: Function, Array and Dictionary (Python)
Complete the function below by Python which can calculate the average price of all the 
products.
"""



def avg(dict):
    item_lst = dict.values()
    total = 0
    for item in item_lst:
        for product in item:
            total += product['price']
        return round(total / len(item), 3)


print(
 avg({
 "products": [
 {
 "name": "Product 1",
 "price": 100
 },
 {
 "name": "Product 2",
 "price": 700
 },
 {
 "name": "Product 3",
 "price": 300
 }
 ]
 })
) 
# print the average price of all products (round to 3 decimal)