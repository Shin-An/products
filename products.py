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
# products[0][0] # 意即products中的第0個大清單中，第0個小清單

for p in products:
    print(p[0], '的價格是', p[1])

# csv為電腦常用儲存資料的檔案格式，可用excel開啟，用','分隔可將資料分成excel中的兩格
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')