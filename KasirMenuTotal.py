print("==HARGA MENU==")
print("1.Nasi goreng:15.000\n2.pizza:\t50.000\n3.Mie ayam:\t16.000")
nasi_goreng = 15000
pizza = 50000
mie_ayam = 16000

menu = input("Pilih menu (1/2/3):")
if menu == "1":
    jumlah = int(input(" Nasi goreng,mau berapa?:"))
    total = nasi_goreng * jumlah
    print(f"YANG HARUS KAMU BAYAR: {total}")

elif menu == "2":
    jumlah = int(input("Pizza, Mau berapa?"))
    total = jumlah * pizza
    print(f"YANG HARUS KAMU BAYAR: {total}")

elif menu == "3":
    jumlah = int(input(f"Mie ayam, mau berapa?:"))
    total = jumlah * mie_ayam
    print(f"YANG HARUS KAMU BAYAR: {total}")

else:
    print("not found")
