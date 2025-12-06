import pytest

def product_details(name, id, qty, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {id}\n"
        f"Quantity: {qty}\n"
        f"Price: {price}"
    )
    return result


if __name__ == "__main__":
    name = "Mobile"
    id = "10001"
    qty = 100
    price = 15000

    print(product_details(name, id, qty, price))
