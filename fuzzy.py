# Fuzzy Class

class Fuzzy:
    # input
    masaKerja = 0  # menggunakan satuan th / tahun
    produkTerjual = 0  # Menggunakan satuan unit barang

    # define bonus
    bonus = 0
    bonusBanyak = 0
    bonusSedikit = 0

    # define masa kerja
    masaKerjaLama = 0
    masaKerjaSedang = 0
    masaKerjaBaru = 0

    # define gaji
    terjualBanyak = 0
    terjualSedikit = 0

    # define default role
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0
    z6 = 0

    # define real role
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    R5 = 0
    R6 = 0

    # others
    total_RiZi = 0
    total_R = 0
    nilai_z = 0
    angka = 0

    def __init__(self, masaKerja, produkTerjual):
        self.masaKerja = masaKerja
        self.produkTerjual = produkTerjual
        self.hitungMasaKerja()
        self.hitungProdukTerjual()
        self.hitungRole()

    def hitungMasaKerja(self):
        # Jika karyawan lama
        if self.masaKerja <= 2:
            self.masaKerjaLama = 0
        elif 2 < self.masaKerja <= 5:
            self.masaKerjaLama = 0
        elif 5 < self.masaKerja <= 8:
            self.masaKerjaLama = (self.masaKerja - 5) / (8 - 5)
        else:
            self.masaKerjaLama = 1

        # Jika karyawan sedang
        if self.masaKerja <= 3:
            self.masaKerjaSedang = 0
        elif 3 < self.masaKerja <= 5:
            self.masaKerjaSedang = (self.masaKerja - 3) / (5 - 3)
        elif 5 < self.masaKerja < 7:
            self.masaKerjaSedang = (7 - self.masaKerja) / (7 - 5)
        else:
            self.masaKerjaSedang = 0

        # Jika karyawan baru
        if self.masaKerja <= 2:
            self.masaKerjaBaru = 1
        elif 2 < self.masaKerja < 5:
            self.masaKerjaBaru = (5 - self.masaKerja) / (5 - 2)
        else:
            self.masaKerjaBaru = 0

    def hitungProdukTerjual(self):
        # Jika produk terjual banyak
        if self.produkTerjual <= 6:
            self.terjualBanyak = 0
        elif 6 < self.produkTerjual <= 10:
            self.terjualBanyak = (self.produkTerjual - 6) / (10 - 6)
        else:
            self.terjualBanyak = 1

        # Jika produk terjual sedikit
        if self.produkTerjual <= 4:
            self.terjualSedikit = 1
        elif 4 < self.produkTerjual <= 7:
            self.terjualSedikit = (7 - self.produkTerjual) / (7 - 4)
        else:
            self.terjualSedikit = 0

    def hitungRole(self):
        self.R1 = min(self.masaKerjaBaru, self.terjualSedikit)
        self.z1 = 600000 - (300000 * self.R1)

        self.R2 = min(self.masaKerjaBaru, self.terjualBanyak)
        self.z2 = 600000 - (300000 * self.R2)

        self.R3 = min(self.masaKerjaSedang, self.terjualSedikit)
        self.z3 = 600000 - (300000 * self.R3)

        self.R4 = min(self.masaKerjaSedang, self.terjualBanyak)
        self.z4 = 300000 + (self.R4 * 300000)

        self.R5 = min(self.masaKerjaLama, self.terjualSedikit)
        self.z5 = 300000 + (self.R5 * 300000)

        self.R6 = min(self.masaKerjaLama, self.terjualBanyak)
        self.z6 = 300000 + (self.R6 * 300000)

        # Menghitung nilai bonus
        # Menjumlahkan (Ri) dan (Zi)
        self.total_RiZi = (self.R1 * self.z1) + (self.R2 * self.z2) + (self.R3 * self.z3) + \
                          (self.R4 * self.z4) + (self.R5 * self.z5) + (self.R6 * self.z6)

        # Menjumlahkan seluruh (Ri)
        self.total_R = self.R1 + self.R2 + self.R3 + self.R4 + self.R5 + self.R6
        # Mendapatkan nilai_z / total bonus
        self.nilai_z = self.total_RiZi / self.total_R

        self.hitungBonus()

    def hitungBonus(self):
        self.bonus = self.nilai_z

        if self.bonus <= 300000:
            self.bonusBanyak = 0
        elif 300000 < self.bonus <= 6000000:
            self.bonusBanyak = (self.bonus - 300000) / (600000 - 300000)
        else:
            self.bonusBanyak = 1

        if self.bonus <= 300000:
            self.bonusSedikit = 1
        elif 300000 < self.bonus <= 600000:
            self.bonusSedikit = (600000 - self.bonus) / (600000 - 300000)
        else:
            self.bonusSedikit = 0

        return format(self.bonus, '.2f')

    def displayMasaKerja(self):
        if self.masaKerjaBaru != 0:
            msg = "Baru ({})".format("%.2f" % self.masaKerjaBaru)
            return msg
        elif self.masaKerjaSedang != 0:
            msg = "Sedang ({})".format("%.2f" % self.masaKerjaSedang)
            return msg
        elif self.masaKerjaLama != 0:
            msg = "Lama ({})".format("%.2f" % self.masaKerjaLama)
            return msg

    def displayProdukTerjual(self):
        if self.terjualSedikit != 0:
            msg = "Sedikit ({})".format("%.2f" % self.terjualSedikit)
            return msg
        elif self.terjualBanyak != 0:
            msg = "Banyak ({})".format("%.2f" % self.terjualBanyak)
            return msg

    def displayBonus(self):
        if self.bonusSedikit != 0:
            msg = "Sedikit ({})".format("%.2f" % self.bonusSedikit)
            return msg
        elif self.bonusBanyak != 0:
            msg = "Banyak ({})".format("%.2f" % self.bonusBanyak)
            return msg