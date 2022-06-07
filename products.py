# 二維度清單
products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格: ')
    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]
    # products.append(p)
    products.append([name, price])
print(products)

products[0][0] # 意即products中的第0個大清單中，第0個小清單