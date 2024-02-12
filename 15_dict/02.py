products_qu = input().split(" ")
order = input().split()

product_dict = {}
for el in range(0, len(products_qu), 2):
    name_p = products_qu[el]
    quantity_p = products_qu[el + 1]
    if name_p not in product_dict.keys():
        product_dict[name_p] = int(quantity_p)

for ord in order:
    if ord in product_dict.keys():
        print(f"We have {product_dict[ord]} of {ord} left")
    else:
        print(f"Sorry, we don't have {ord}")