'''def test_sum_category_as_tuple(lst: list)-> list:
    final_lst = []
    sum_price = 0
    sum_price_last = 0
    for i in range(len(lst) - 1): 
        if lst[i]['category'] == lst[i+1]['category']:
            sum_price += lst[i]['price_rub']
        else:
            sum_price += lst[i]['price_rub']
            final_lst.append((lst[i]['category'], sum_price))
            sum_price = 0
    for j in lst:
        if j['category'] == 'drinks':
            sum_price_last += j['price_rub']
    final_lst.append((lst[-1]['category'], sum_price_last))
    final_dct = dict(final_lst)
    return sorted(final_dct.items(), key=lambda item: item[1])
   '''
def test_sum_category_as_tuple(lst: list) -> list:
    category_sums = {}
    for item in lst:
        category = item['category']
        price = item['price_rub']
        category_sums[category] = category_sums.get(category, 0) + price
    
    return sorted(category_sums.items(), key=lambda item: item[1])
 


sales_data = [
    {"category": "dairy_products", "product": "milk", "price_rub": 100, "count": 1},
    {"category": "dairy_products", "product": "cream", "price_rub": 290, "count": 1},
    {"category": "dairy_products", "product": "yogurt", "price_rub": 50, "count": 1},
    {"category": "bakery", "product": "white_bread", "price_rub": 60, "count": 1},
    {"category": "bakery", "product": "black_bread", "price_rub": 55, "count": 1},
    {"category": "drinks", "product": "water", "price_rub": 90, "count": 1},
    {"category": "drinks", "product": "apple", "price_rub": 300, "count": 1},
]

assert test_sum_category_as_tuple(sales_data) == [('bakery', 115), ('drinks', 390), ('dairy_products', 440)]
print("All tests passed")