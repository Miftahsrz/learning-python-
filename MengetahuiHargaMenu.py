print("==PILIH MENU==")
print("1.Mie ayam ")
print("2.Nasi goreng")
print("3.Pizza")
print("4.Kopi")

nasgor_harga = 20.000
mie_ayam = 15.000
pizza = 50.000
kopi = 10.000


while True:
    user_menu = input("MASUKAN MENU (pilih 1/2/3/4):")
    if user_menu == "1":
        print(f"Mie ayam harga: {mie_ayam}")
    elif user_menu == "2":
        print(f"Nasi goreng harga: {nasgor_harga}")
    elif user_menu == "3":
        print(f"pizza harga: {pizza}")
    elif user_menu == "4":
        print(f"kopi harga:{kopi}")
    else:
        print("PILIH 1/2/3/4")
