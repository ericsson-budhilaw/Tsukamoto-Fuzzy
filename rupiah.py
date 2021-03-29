import locale


class Rupiah:
    desimal = 2

    def __init__(self, angka):
        self.angka = angka

    def konversi(self):
        str_value = str(self.angka)
        separate_decimal = str_value.split(".")
        after_decimal = separate_decimal[0]
        before_decimal = separate_decimal[1]

        reverse = after_decimal[::-1]
        temp_reverse_value = ""

        for index, val in enumerate(reverse):
            if (index + 1) % 3 == 0 and index + 1 != len(reverse):
                temp_reverse_value = temp_reverse_value + val + "."
            else:
                temp_reverse_value = temp_reverse_value + val

        temp_result = temp_reverse_value[::-1]

        return "Rp " + temp_result + "," + before_decimal
