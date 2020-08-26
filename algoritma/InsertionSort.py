'''
insertion sort nasıl çalışır?
döngü her çalışıtğında bir sonraki elemanı sondan başa doğru karşılaştırarak yerlerini değiştirerek küçükten büyüğe sıralar.

'''

import random
mesafe = int(input("1' den başlayarak kaça kadar sayı üretsin: "))
sayi = int(input("Kaç tane sayı üretsin: "))
dizi = random.sample(range(mesafe),sayi)
i = 0
for j in range(1,len(dizi)):
    key= dizi[j]
    i=j-1
    while i>-1 and dizi[i]>key:
        dizi[i+1] = dizi[i]
        i-=1
    dizi[i+1]= key
print(dizi)
