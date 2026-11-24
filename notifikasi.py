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
