
class MenuMakanan:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    # Property untuk mengambil nama
    @property
    def nama(self):
        return self._nama

    # Property dan setter untuk harga
    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai > 0:
            self._harga = nilai
        else:
            raise ValueError("Harga harus lebih dari 0!")

    # Class method
    @classmethod
    def menu_default(cls):
        return [
            cls("Nasi Goreng", 15000),
            cls("Mie Ayam", 12000),
            cls("Ayam Geprek", 18000),
            cls("Bakso", 13000),
            cls("Es Teh", 5000)
        ]

    # Static method
    @staticmethod
    def format_rupiah(angka):
        return "Rp" + format(angka, ",").replace(",", ".")


class Pemesanan:
    def __init__(self, nama_pelanggan):
        self._nama_pelanggan = nama_pelanggan
        self._pesanan = []

    # Method untuk menambahkan pesanan
    def tambah_pesanan(self, menu, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return

        self._pesanan.append((menu, jumlah))
        print(menu.nama, "berhasil ditambahkan!")

    # Menghitung total harga
    def hitung_total(self):
        total = 0
        for menu, jumlah in self._pesanan:
            total += menu.harga * jumlah
        return total

    # Menampilkan struk
    def tampilkan_struk(self):
        print("\n========== STRUK PEMESANAN ==========")
        print("Nama Pelanggan:", self._nama_pelanggan)
        print("-------------------------------------")

        for menu, jumlah in self._pesanan:
            subtotal = menu.harga * jumlah
            print(menu.nama)
            print("Jumlah:", jumlah)
            print("Subtotal:", MenuMakanan.format_rupiah(subtotal))

        print("-------------------------------------")
        print("Total Bayar:",
              MenuMakanan.format_rupiah(self.hitung_total()))
        print("=====================================")


# PROGRAM UTAMA

daftar_menu = MenuMakanan.menu_default()

nama = input("Masukkan nama pelanggan: ")
pesanan = Pemesanan(nama)

while True:
    print("\n===== SISTEM PEMESANAN MAKANAN =====")
    print("1. Lihat Menu")
    print("2. Pesan Makanan")
    print("3. Lihat Total Pesanan")
    print("4. Cetak Struk")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\n========== DAFTAR MENU ==========")
        for i, menu in enumerate(daftar_menu, start=1):
            print(i, menu.nama, "-",
                  MenuMakanan.format_rupiah(menu.harga))

    elif pilihan == "2":
        print("\nPilih makanan:")
        for i, menu in enumerate(daftar_menu, start=1):
            print(i, menu.nama, "-",
                  MenuMakanan.format_rupiah(menu.harga))

        try:
            nomor = int(input("Masukkan nomor makanan: "))
            jumlah = int(input("Masukkan jumlah pesanan: "))

            if 1 <= nomor <= len(daftar_menu):
                pesanan.tambah_pesanan(
                    daftar_menu[nomor - 1], jumlah
                )
            else:
                print("Nomor makanan tidak tersedia!")

        except ValueError:
            print("Masukkan angka yang benar!")

    elif pilihan == "3":
        print("\nTotal Pesanan:",
              MenuMakanan.format_rupiah(pesanan.hitung_total()))

    elif pilihan == "4":
        pesanan.tampilkan_struk()

    elif pilihan == "5":
        print("Terima kasih sudah memesan!")
        break

    else:
        print("Pilihan tidak tersedia!")
