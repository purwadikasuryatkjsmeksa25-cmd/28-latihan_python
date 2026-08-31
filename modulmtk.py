def ganjil_genap(angka):
    if angka % 2 == 0:
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"

def bilangan_prima(angka):
    if angka < 2:
        return False

    pembagi = 0

    for i in range(1, angka + 1):
        if angka % i == 0:
            pembagi += 1

    if pembagi == 2:
        return True
    else:
        return False
    return 2 * (panjang + lebar)
