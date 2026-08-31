import modulmtk
import olahraga


while True:

    print("\n==============================")
    print("          MENU UTAMA")
    print("==============================")
    print("1. Cek Ganjil / Genap")
    print("2. Cek Bilangan Prima")
    print("3. Sepak Bola")
    print("4. Cardio")
    print("5. Keluar")
    print("==============================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        angka = int(input("Masukkan bilangan: "))

        hasil = modulmtk.ganjil_genap(angka)

        print("Hasil:", hasil)

    elif pilihan == "2":

        angka = int(input("Masukkan bilangan: "))

        if modulmtk.bilangan_prima(angka):
            print("Hasil: Bilangan Prima")
        else:
            print("Hasil: Bukan Bilangan Prima")

    elif pilihan == "3":

        olahraga.sepak_bola()

    elif pilihan == "4":

        olahraga.cardio()

    elif pilihan == "5":

        print("Program selesai.")
        break

    else:

        print("Pilihan tidak tersedia.")

    ulang = input("\nMau mengulang? (y/n): ")

    if ulang.lower() == "n":

        print("Program selesai.")
        break