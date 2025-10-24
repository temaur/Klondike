def test_get_distinct_categories(lst: list) -> set:
    final_set = {x["category"] for x in lst}
    return final_set


sales_data = [
    {"category": "dairy_products", "product": "milk", "price_rub": 100, "count": 1},
    {"category": "dairy_products", "product": "cream", "price_rub": 290, "count": 1},
    {"category": "dairy_products", "product": "yogurt", "price_rub": 50, "count": 1},
    {"category": "bakery", "product": "white_bread", "price_rub": 60, "count": 1},
    {"category": "bakery", "product": "black_bread", "price_rub": 55, "count": 1},
    {"category": "drinks", "product": "water", "price_rub": 90, "count": 1},
    {"category": "drinks", "product": "apple", "price_rub": 300, "count": 1},
]

assert test_get_distinct_categories(sales_data) == {
    "drinks",
    "dairy_products",
    "bakery",
}
print("All tests passed")
