"""
Day 2: *args & **kwargs - Shopping Cart.
Date: February 16, 2026
Describing: Learninng to flexible functions parameters.
            Built Shopping Cart.
"""

# Exerices 1 Shoping Cart.

def add_to_cart(*items):
    print("Adding to Cart.")
    for  i in items:
        print(i)
    
    total = len(items)
    print(f"Total items: {total}")


def calculate_bill(**items_with_price):
    print("Total Bill:")
    total = 0
    for key,value in items_with_price.items():
        print(f"{key}   ₹{value}")
        total = total + value
    print("="*40)
    print(f"Total   ₹{total}")
    discount = 10

def discount_(discount,**prices):
    total = 0
    for key, value in prices.items():
        total = total + value
    
    discount_price = total * discount /100
    final = total - discount_price
    return final

def checkout(discount,*items,**prices):
    print("="*40)
    add_to_cart(*items)
    print("="*40)
    calculate_bill(**prices)
    print("-"*40)
    print(f"Total after Discount of {discount}% : ₹{discount_(discount,**prices)}")


prices={
    "Apple": 90,
    "Banana": 50,
    "Orange": 70,
    "Mango": 80
}

items = ["Apple", "Banana","Orange","Mango"]

print("Items list: ")
for i  in items:
    print(i)

discount=10
checkout(discount,*items,**prices)


