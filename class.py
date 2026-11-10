from datetime import datetime


class Ruangan:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.status = "Kosong"

    def mulai_penggunaan(self):
        self.status = "Dipakai"
        print(f"{self.nama} sekarang sedang dipakai.")

    def akhiri_penggunaan(self):
        self.status = "Kosong"
        print(f"{self.nama} sekarang kosong.")

    def cek_status(self):
        return self.status


class Jadwal:
    def __init__(self, ruangan, mata_kuliah, mulai, selesai):
        self.ruangan = ruangan
        self.mata_kuliah = mata_kuliah
        self.mulai = mulai
        self.selesai = selesai

    def cek_jadwal(self, waktu):
        return self.mulai <= waktu < self.selesai


kelas_a = Ruangan("A101", "Ruang A101")

jadwal = Jadwal(
    kelas_a,
    "Pemrograman Berorientasi Objek",
    datetime(2026, 10, 27, 8, 0),
    datetime(2026, 10, 27, 10, 0)
)
