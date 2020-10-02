n = 5
data=[]
total=0
ave=0
for x in range (n):
    print("Angka ke- ", x+1)
    nilai = int(input(" "))
    data.append(nilai)
print(data)
for i in range(len(data)):
    total=total+data[i]
    ave=ave+data[i]/n
print(total)
print(ave)
