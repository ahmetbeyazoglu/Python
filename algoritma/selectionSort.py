
a = int(input("Kaç tane sayı gireceksiniz?: "))
dizi = []
for i in range(a):
    dizi.append(int(input()))
for i in range(len(dizi)):
    min = i
    for j in range(i + 1, len(dizi)):
        if dizi[min] > dizi[j]:
            min = j
    dizi[i], dizi[min] = dizi[min], dizi[i]

print("Sorted sequence:")
for i in range(len(dizi)):
    print(dizi[i])
