def test_product_details():
    expected_output = (
        "Product Name: Mobile\n"
        "Product ID: 10001\n"
        "Quantity: 100\n"
        "Price: 15000"
    )

    assert product_details("Mobile", "10001", 100, 15000) == expected_output
