username, password, times ="ahmad","ahmadwahyudi", 3
while True:
    times-=1
    print("Username: ",username)
    txtPass=input("Masukkan Password: ")
    if txtPass==password:
        print("Login Berhasil")
        break
    elif times>0:
        print(f"Password Salah! Anda punya {times} kesempatan tersisa")
    else:
        print("Gagal maneh! Silahkan keluar!")
        break