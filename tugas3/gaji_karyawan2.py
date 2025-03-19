
statuslist = {"honor":750000, "tetap":1000000}
bonuslist = {
    "a":{"honor":150000, "tetap":200000}, 
    "b":{"honor":275000, "tetap":400000}, 
    "c":{"honor":480000, "tetap":550000}
}

nama=str(input("masukkan nama : "))
nik=int(input("masukkan nik : "))
while True:
    status = input("Masukkan Status (tetap/honor): ").strip().lower()
    if status in statuslist:
        gaji = statuslist[status]
        break
    print("Invalid! Harap masukkan 'tetap' atau 'honor'.")
while True:
    gol = input("Masukkan Golongan (A/B/C): ").strip().lower()
    if gol in bonuslist:
        bonus = bonuslist[gol][status]
        break
    print("Invalid! Harap masukkan 'A', 'B', atau 'C'.")
total = int(gaji + bonus)

print("Nama:", nama.capitalize())
print("NIK:", nik)
print("Status : ", status.capitalize())
print("Golongan : ", gol.upper())
print("Gaji:", gaji)
print("Bonus:", bonus)
print("Gaji Total:", total)