tinggiBadan= float(input("Tinggi Badan (dalam meter): "))
beratBadan= float(input("Berat Badan (dalam Kg): "))
bmi=beratBadan/(tinggiBadan**2)
print("BMI anda adalah: {0} dan Anda: ".format(bmi, end=''))
if (bmi<18.5):
    print("Berat Badan Kurang")
elif (bmi>18.5 and bmi<23):
    print("Berat Badan Normal")
elif (bmi>23 and bmi<30):
    print("Berat Badan berlebih")
else:
    print("Obesitas")
    