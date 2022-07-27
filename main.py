def menu():
    print("1. Jakarta - Bandung")
    print("2. Jakarta - Semarang")
    print("3. Jakarta - Solo")
    print("4. Jakarta - Yogyakarta")
    print("5. Jakarta - Surabaya")
# program waktu tempuh
print("Program waktu tempuh")
menu()
jakarta_bandung = 151
jakarta_semarang = 442 
jakarta_solo = 538
jakarta_jogja = 562
jakarta_surabaya = 783
# tampilan
jam_berangkat = int(input("\nmasukkan jam berangkat (0 - 24) : "))
menit_berangkat = int(input("masukkan menit berangkat (0 - 60) : "))
kecepatan_kereta = int(input("masukkan kecepatan kereta (km/jam): "))
kota_tujuan = int(input("kota tujuan (1 - 5) : "))
besok = 0
besok1 = 0

t_kereta = jam_berangkat + (menit_berangkat/60) # dibuat jam
if kota_tujuan == 1:
    j_kereta = jakarta_bandung
    tujuan = "Jakarta - Bandung"
    waktu_tempuh_jam = (j_kereta//kecepatan_kereta)
    waktu_tempuh_menit = (j_kereta%kecepatan_kereta)
    waktu_tiba_jam = jam_berangkat + waktu_tempuh_jam
    waktu_tiba_menit = menit_berangkat + waktu_tempuh_menit
    while waktu_tempuh_menit > 60:
        waktu_tempuh_jam += (waktu_tempuh_menit//60)
        waktu_tempuh_menit %= 60
    while waktu_tempuh_jam > 24:
        besok1 = waktu_tempuh_jam // 24
        waktu_tempuh_jam %= 24
    while waktu_tiba_menit > 60:
        waktu_tiba_jam += (waktu_tiba_menit//60)
        waktu_tiba_menit %= 60
    while waktu_tiba_jam > 24:
        besok = waktu_tiba_jam // 24
        waktu_tiba_jam %= 24

elif kota_tujuan == 2:
    j_kereta = jakarta_semarang
    tujuan = "Jakarta - Semarang"
    waktu_tempuh_jam = (j_kereta//kecepatan_kereta)
    waktu_tempuh_menit = (j_kereta%kecepatan_kereta)
    waktu_tiba_jam = jam_berangkat + waktu_tempuh_jam
    waktu_tiba_menit = menit_berangkat + waktu_tempuh_menit
    while waktu_tempuh_menit > 60:
        waktu_tempuh_jam += (waktu_tempuh_menit//60)
        waktu_tempuh_menit %= 60
    while waktu_tempuh_jam > 24:
        besok1 = waktu_tempuh_jam // 24
        waktu_tempuh_jam %= 24
    while waktu_tiba_menit > 60:
        waktu_tiba_jam += (waktu_tiba_menit//60)
        waktu_tiba_menit %= 60
    while waktu_tiba_jam > 24:
        besok = waktu_tiba_jam // 24
        waktu_tiba_jam %= 24
            
elif kota_tujuan == 3:
    j_kereta = jakarta_solo
    tujuan = "Jakarta - Solo"
    waktu_tempuh_jam = (j_kereta//kecepatan_kereta)
    waktu_tempuh_menit = (j_kereta%kecepatan_kereta)
    waktu_tiba_jam = jam_berangkat + waktu_tempuh_jam
    waktu_tiba_menit = menit_berangkat + waktu_tempuh_menit
    while waktu_tempuh_menit > 60:
        waktu_tempuh_jam += (waktu_tempuh_menit//60)
        waktu_tempuh_menit %= 60
    while waktu_tempuh_jam > 24:
        besok1 = waktu_tempuh_jam // 24
        waktu_tempuh_jam %= 24
    while waktu_tiba_menit > 60:
        waktu_tiba_jam += (waktu_tiba_menit//60)
        waktu_tiba_menit %= 60
    while waktu_tiba_jam > 24:
        besok = waktu_tiba_jam // 24
        waktu_tiba_jam %= 24

elif kota_tujuan == 4:
    j_kereta = jakarta_jogja
    tujuan = "Jakarta - Yogyakarta"
    waktu_tempuh_jam = (j_kereta//kecepatan_kereta)
    waktu_tempuh_menit = (j_kereta%kecepatan_kereta)
    waktu_tiba_jam = jam_berangkat + waktu_tempuh_jam
    waktu_tiba_menit = menit_berangkat + waktu_tempuh_menit
    while waktu_tempuh_menit > 60:
        waktu_tempuh_jam += (waktu_tempuh_menit//60)
        waktu_tempuh_menit %= 60
    while waktu_tempuh_jam > 24:
        besok1 = waktu_tempuh_jam // 24
        waktu_tempuh_jam %= 24
    while waktu_tiba_menit > 60:
        waktu_tiba_jam += (waktu_tiba_menit//60)
        waktu_tiba_menit %= 60
    while waktu_tiba_jam > 24:
        besok = waktu_tiba_jam // 24
        waktu_tiba_jam %= 24

elif kota_tujuan == 5:
    j_kereta = jakarta_surabaya
    tujuan = "Jakarta - Surabaya"
    waktu_tempuh_jam = (j_kereta//kecepatan_kereta)
    waktu_tempuh_menit = (j_kereta%kecepatan_kereta)
    waktu_tiba_jam = jam_berangkat + waktu_tempuh_jam
    waktu_tiba_menit = menit_berangkat + waktu_tempuh_menit
    while waktu_tempuh_menit > 60:
        waktu_tempuh_jam += (waktu_tempuh_menit//60)
        waktu_tempuh_menit %= 60
    while waktu_tempuh_jam > 24:
        besok1 = waktu_tempuh_jam // 24
        waktu_tempuh_jam %= 24
    while waktu_tiba_menit > 60:
        waktu_tiba_jam += (waktu_tiba_menit//60)
        waktu_tiba_menit %= 60
    while waktu_tiba_jam > 24:
        besok = waktu_tiba_jam // 24
        waktu_tiba_jam %= 24
else:
    print("Data yang dimasukkan salah mohon diinput lagi")
        
# kereta tujuan =
# jarak tempuh =
# waktu keberangkatan = 
# waktu tempuh = 
# waktu kedatangan =
print(f"\nKereta tujuan = {tujuan}")
print(f"Jarak tempuh = {j_kereta} Km")
print(f"Waktu keberangkatan = {jam_berangkat} : {menit_berangkat}")
print(f"Waktu tempuh = {besok1} hari : {waktu_tempuh_jam} jam : {waktu_tempuh_menit} menit")
print(f"Waktu kedatangan = besok {besok} hari jam {waktu_tiba_jam} menit {waktu_tiba_menit}")