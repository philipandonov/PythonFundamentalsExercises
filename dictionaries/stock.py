data = input().split()
search_product = input().split()
product_data = {data[i]: int(data[i+1]) for i in range(0, len(data), 2)}
for product in search_product:
    if product not in product_data:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {product_data[product]} of {product} left")