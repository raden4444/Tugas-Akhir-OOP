from datetime import datetime

class ManajerRuagan:
      def __init__(self):
        self.daftar_ruangan = []
        self.daftar_jadwal = []
        self.daftar_peminjaman = []
        self.daftar_penggunaan = []

    def tambah_ruangan(self, ruangan):
        self.daftar_ruangan.append(ruangan)

    def tambah_jadwal(self, jadwal):
        # Periksa bentrok dengan jadwal yang sudah tersimpan
        for jadwal_lama in self.daftar_jadwal:
            if jadwal.bentrok_dengan(jadwal_lama):
                print("Jadwal bentrok dengan jadwal yang sudah ada.")
                return False

        self.daftar_jadwal.append(jadwal)
        print("Jadwal berhasil ditambahkan.")
        return True

    def cari_ruangan_kosong(self):
        ruangan_kosong = []

        for ruangan in self.daftar_ruangan:
            if ruangan.cek_status() == "Kosong":
                ruangan_kosong.append(ruangan)

        return ruangan_kosong

    def ajukan_peminjaman(self, pemohon, data):
        peminjaman = data
        self.daftar_peminjaman.append(peminjaman)

        print("Pengajuan peminjaman berhasil dicatat.")
        return peminjaman

    def check_in(self, pengguna, jadwal):
        # Pastikan ruangan terdaftar
        if jadwal.ruangan not in self.daftar_ruangan:
            print("Ruangan tidak terdaftar.")
            return False

        # Periksa hak check-in pengguna
        if not pengguna.punya_hak_check_in(jadwal):
            print("Pengguna tidak memiliki hak check-in.")
            return False

        # Pastikan ruangan belum digunakan
        if jadwal.ruangan.cek_status() != "Kosong":
            print("Ruangan sedang digunakan.")
            return False

        # Ubah status ruangan setelah check-in berhasil
        jadwal.ruangan.tandai_dipakai()

        print(f"Check-in berhasil untuk ruangan {jadwal.ruangan.nama}.")
        return True

    def check_out(self, penggunaan):
        # Pastikan penggunaan masih aktif
        if not penggunaan.masih_aktif():
            print("Penggunaan ruangan sudah berakhir.")
            return False

        penggunaan.check_out()
        penggunaan.ruangan.tandai_kosong()

        print("Check-out berhasil. Ruangan kembali kosong.")
        return True

    def kirim_notifikasi_jadwal(self):
        for jadwal in self.daftar_jadwal:
            print(
                f"Pengingat jadwal: {jadwal.get_deskripsi()}"
            )
        
    def cari_ruangan_kosong(waktu):
        ruangan_kosong = []
        for ruang in self.daftar_ruangan:
            ruangan_kosong.append(ruangan)
    return ruangan_kosong
    
    def ajukan_peminjaman(pemohon, data):
        
        pass
    def check_in(pengguna, jadwal):
        pass
    def check_out(penggunaan):
        pass
    def kirim_notifikasi_jadwal:


class Ruangan:
    def cek_status(self):
        pass
    def tandai_dipakai():
        pass
    def tandai_kosong():


class Ruangan:
    def __init__(self, id_ruangan, nama):
        self.id_ruangan = id_ruangan
        self.nama = nama
        self.status = "Kosong"

    def cek_status(self):
        return self.status

    def tandai_dipakai(self):
        if self.status == "Kosong":
            self.status = "Dipakai"
            return True

        return False

    def tandai_kosong(self):
        if self.status == "Dipakai":
            self.status = "Kosong"
            return True

        return False

    def get_deskripsi(self):
        return (
            f"Ruangan {self.nama} "
            f"(ID: {self.id_ruangan}) - Status: {self.status}"
        )


class Jadwal:
    def __init__(
        self,
        id_jadwal,
        tanggal,
        jam_mulai,
        jam_selesai,
        ruangan
    ):
        self.id_jadwal = id_jadwal
        self.tanggal = tanggal
        self.jam_mulai = jam_mulai
        self.jam_selesai = jam_selesai
        self.ruangan = ruangan

    def bentrok_dengan(self, jadwal_lain):
        # Periksa apakah tanggal dan ruangannya sama
        if self.tanggal != jadwal_lain.tanggal:
            return False

        if self.ruangan.id_ruangan != jadwal_lain.ruangan.id_ruangan:
            return False

        # Periksa apakah waktu kedua jadwal bertumpang tindih
        return (
            self.jam_mulai < jadwal_lain.jam_selesai
            and self.jam_selesai > jadwal_lain.jam_mulai
        )

    def get_deskripsi(self):
        return (
            f"Jadwal ID: {self.id_jadwal}\n"
            f"Tanggal: {self.tanggal}\n"
            f"Waktu: {self.jam_mulai} - {self.jam_selesai}\n"
            f"Ruangan: {self.ruangan.nama}"
        )


class Peminjaman(jadwal)
    def __init__(
        self,
        id_jadwal,
        waktu_mulai,
        waktu_selesai,
        ruangan,
        keperluan,
        pemohon
    ):
        super().__init__(id_jadwal, waktu_mulai, waktu_selesai, ruangan)
        self.keperluan = keperluan
        self.status = StatusPeminjaman.MENUNGGU
        self.pemohon = pemohon

    def ajukan(self):
        self.status = StatusPeminjaman.MENUNGGU
        return True

    def batalkan(self):
        if self.status == StatusPeminjaman.MENUNGGU:
            self.status = StatusPeminjaman.DIBATALKAN
            return True

        return False

    def get_deskripsi(self):
        return (
            f"{super().get_deskripsi()}\n"
            f"Keperluan: {self.keperluan}\n"
            f"Pemohon: {self.pemohon.nama}\n"
            f"Status: {self.status.value}"
        )

   
class PenggunaanRuangan:
    def check_out():
        pass
    def masih_aktif():
        pass

class Notifikasi:
      def __init__(self, penerima, pesan, waktu_kirim=None):
            if penerima is None:
                  raise ValueError("Penerima notifikasi tidak boleh kosong.")
            if not isistance(pesan, str) or not pesan.strip():
                  rasie ValueError("Pesan notifikasi tidak boleh kosong.")
            self._penerima = penerima
            self._pesan = pesan.strip()
            self._sudah_dibaca = False
            
      @property
      def penerima(self):
            return self._penerima

      @property
      def pesan(self):
            return self._pesan

      @property
      def waktu_kirim(self):
            return self._waktu_kirim

      @property
      def sudah_dibaca(self):
            return self._sudah_dibaca
            
      def tandai_dibaca()
            pass

      def __str__(self):
            tanda = "dibaca" if self._sudah_dibaca else "BARU"
            return f"[{tanda}] {self.waktu_kirim:%d-%m-%Y %H: %M}

class Pengguna:
    get_peran()
    def punya_hak_check_in(jadwal):
        pass

class Dosen:
    get_peran()
    def punya_hak_check_in(jadwal):
        pass

class Mahasiswa:
    get_peran()
    def punya_hak_check_in(jadwal):
        pass

class Admin:
    get_peran()

    def setujui(peminjaman):
        pass
    def tolak(peminjaman, alasan):
        pass
    def buat_rekap_penggunaan():
        pass
    
        

        

