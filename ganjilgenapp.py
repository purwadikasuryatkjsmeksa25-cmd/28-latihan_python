def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"


# Function Bilangan Prima
def cek_prima(angka):
    if angka < 2:
        return False

    for i in range(2, angka):
        if angka % i == 0:
            return False

    return True


# Menu
while True:
    print("\n=== MENU ===")
    print("1. Cek Ganjil/Genap")
    print("2. Cek Bilangan Prima")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        angka = int(input("Masukkan angka: "))
        print(cek_ganjil_genap(angka))

    elif pilihan == "2":
        angka = int(input("Masukkan angka: "))

        if cek_prima(angka):
            print("Bilangan Prima")
        else:
            print("Bukan Bilangan Prima")

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak tersedia")
