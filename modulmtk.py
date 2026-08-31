def ganjil_genap(angka):
    if angka % 2 == 0:
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"


def bilangan_prima(angka):
    if angka < 2:
        return False

    for i in range(2, angka):
        if angka % i == 0:
            return False

    return True


def luas_persegi(sisi):
    return sisi * sisi


def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar


def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari


def keliling_persegi(sisi):
    return 4 * sisi


def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)