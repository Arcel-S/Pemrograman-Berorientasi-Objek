# Drum Air
class DrumAir:  #inisialisasi class Drum Air
    #inisialisasi atribut
    def __init__(self, kapasitas_maksimal):
        self.kapasitas_maksimal = kapasitas_maksimal
        self.volume_saat_ini = 0
        self.air_tumpah = 0

    #inisialisasi metode penambahan air
    def isi_air(self, volume):
        if 0 <= self.volume_saat_ini + volume <= self.kapasitas_maksimal:
            self.volume_saat_ini += volume
        elif self.volume_saat_ini + volume >= self.kapasitas_maksimal:
            self.air_tumpah += (self.volume_saat_ini + volume) - self.kapasitas_maksimal
            self.volume_saat_ini = self.kapasitas_maksimal
        else:
            pass

        print(f"Volume air yang ingin diisikan = {volume} liter, ", end="")
        print(f"Volume Air yang tumpah: {self.air_tumpah} liter")

    #inisialisasi metode pemakaian air
    def kurangi_air(self, volume):
        if self.volume_saat_ini >= volume:
            self.volume_saat_ini -= volume
            print(f"Air dipakai sebanyak {volume} liter.")
        else:
            print("Air tidak cukup atau telah habis.")

    #metode menampilkan informasi
    def tampilkan_info(self):
        print(f"Kapasitas Maksimal: {self.kapasitas_maksimal} liter")
        print(f"Volume Saat Ini: {self.volume_saat_ini} liter")
        print(f"Sisa Ruang: {self.kapasitas_maksimal - self.volume_saat_ini} liter\n")

#logika main untuk mengakses kelas DrumAir
if __name__ == "__main__":
    #inisialisasi objek drum air dengan kapasitas 200 liter
    drum1 = DrumAir(200)

    #menampilkan informasi drum (objek)
    drum1.tampilkan_info()

    #penambahan air
    drum1.isi_air(50)
    drum1.isi_air(30)
    drum1.isi_air(40)
    drum1.isi_air(85)

    print("\nVolume Air Setelah Diisi:")
    drum1.tampilkan_info()

    #pemakaian air
    drum1.kurangi_air(25)
    print("\nSetelah air digunakan:")
    drum1.tampilkan_info()
