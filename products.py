# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line: # 跳過商品及價格，continue為跳到下一迴，跟break一樣只能寫在迴圈裡
            continue # 跳過7-8行迴圈內容不執行
        name, price = line.strip().split(',') # split為切割，()內為切割的標準，切割完的結果是清單
        products.append([name, price])
print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')