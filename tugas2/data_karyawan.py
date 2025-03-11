nama=str(input("masukkan nama : "))
nik=int(input("masukkan nik : "))
status=str(input("masukkan status pegawai (tetap/honor) : "))
gol=str(input("masukkan golongan (A/B/C) : "))

if status=="tetap":
    gaji=1000000
    if gol=="A":
        bonus=200000
    elif gol=="B":
        bonus=400000
    elif gol=="C":
        bonus=550000
    total=gaji+bonus
    print("Nama : ", nama)
    print("NIK : ", nik)
    print("Status : ", status)
    print("Golongan : ", gol)
    print("Gaji : ", gaji)
    print("Bonus : ", bonus)
    print("Gaji total : ", total)
elif status=="honor":
    gaji=750000
    if gol=="A":
        bonus=150000
    elif gol=="B":
        bonus=275000
    elif gol=="C":
        bonus=480000
    total=gaji+bonus
    print("Nama : ", nama)
    print("NIK : ", nik)
    print("Status : ", status)
    print("Golongan : ", gol)
    print("Gaji : ", gaji)
    print("Bonus : ", bonus)
    print("Gaji total : ", total)

