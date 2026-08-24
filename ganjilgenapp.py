while True:
    angka = int(input("masukan bilangan baginda: "))

    if angka % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")

    keluar = input("Mau keluar baginda? (y/n): ")

    if keluar == "y":
        break
