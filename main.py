from rupiah import Rupiah
from fuzzy import Fuzzy

masaKerja = int(input("Masukkan lama masa kerja (tahun): "))
produkTerjual = int(input("Masukkan banyak barang terjual (unit): "))
fuzz = Fuzzy(masaKerja, produkTerjual)
bonus = Rupiah(fuzz.hitungBonus())
nilai_z = Rupiah(fuzz.nilai_z)
print("> Masa Kerja:", "{} Tahun".format(masaKerja), "| {}".format(fuzz.displayMasaKerja()))
print("> Produk Terjual:", "{} Unit".format(produkTerjual), "| {}".format(fuzz.displayProdukTerjual()))
print("> Bonus Penjualan:", fuzz.displayBonus())
print("----------------------------------")
print(">> Total Bonus: {}".format(bonus.konversi()), "<<")
print("----------------------------------")

