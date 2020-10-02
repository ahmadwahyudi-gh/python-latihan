n=int(input("Banyak Data: "))
data=[]
for x in range (n):
    print("Data ke- ", x+1)
    nilai=(int(input()))
    data.append(nilai)
print(data)
print("Angka terbesar adalah: ", max(data))
print("Angka terkecil adalah: ", min(data))