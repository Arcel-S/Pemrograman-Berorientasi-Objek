#inisialisasi class media
class Media:
    #inisialisasi attribut
    def __init__(self, judul, penulis, tahun):
        self.__judul = judul  #enkapsulasi menjadi atribut private
        self.__penulis = penulis
        self.__tahun = tahun
        self.__dipinjam = False
    
    #getter judul untuk mendapatkan judul (enkapsulasi - akses data secara terbatas)
    def get_judul(self):
        return self.__judul
    
    #getter untuk mendapatkan status peminjaman (enkapsulasi)
    def get_status_pinjam(self):
        if self.__dipinjam:
            return "Dipinjam"
        return "Tersedia"
    
    #method untuk mendapatkan peminjaman (enkapsulasi - kontrol perubahan state)
    def pinjam(self):   
        if not self.__dipinjam:
            self.__dipinjam = True
            return True
        return False
    
    #method untuk mendapatkan pengembalian (enkapsulasi)
    def kembalikan(self):
        if self.__dipinjam:
            self.__dipinjam = False
            return True
        return False
    
    #method abstrak yang akan diimplementasi atau digunakan oleh subclass (abstraksi)
    def tampilkan_info(self):
        pass
    
    #operator overloading untuk menambahkan dua objek Media (misalnya koleksi buku)
    def __add__(self, other):
        if isinstance(other, Media):
            return "Koleksi : " + self.get_judul() + " dan " + other.get_judul()
        return "Operasi tidak didukung"

#kelas Buku yang mewarisi kelas Media (Pewarisan)
class Buku(Media):
    #insialisasi atribut
    def __init__(self, judul, penulis, tahun, halaman):
        Media.__init__(self, judul, penulis, tahun)  #memanggil konstruktor kelas induk
        self.__halaman = halaman
    
    #implementasi method tampilkan_info (polimorfisme - metode berbeda di kelas turunan)
    def tampilkan_info(self):
        return "Buku            : " + self.get_judul() + " (" + self.get_status_pinjam() + ")\n" + "Jumlah Halaman  : " + str(self.__halaman)

#kelas EBook mewarisi dari Media (Pewarisan)
class EBook(Media):
    def __init__(self, judul, penulis, tahun, format_file):
        Media.__init__(self, judul, penulis, tahun)
        self.__format = format_file
    
    #implementasi method tampilkan_info (polimorfisme - metode berbeda di kelas turunan)
    def tampilkan_info(self):
        return "E-book  : " + self.get_judul() + " (" + self.get_status_pinjam() + ")\n" + "Format  : " + self.__format

#kelas untuk mengelola peminjaman
class PeminjamanManager:
    #inisialisasi atribut
    def __init__(self):
        self.__riwayat_peminjaman = []  #enkapsulasi - daftar peminjaman tidak bisa diubah langsung
    
    #metode untuk mencatat peminjaman
    def catat_peminjaman(self, media, peminjam):
        if media.pinjam():
            self.__riwayat_peminjaman.append({
                "media": media.get_judul(),
                "peminjam": peminjam
            })
            return True
        return False
    
    #metode untuk menampilkan riwayat peminjaman
    def tampilkan_riwayat(self):
        for pinjam in self.__riwayat_peminjaman:
            print("Media    : " + pinjam["media"])
            print("Peminjam : " + pinjam["peminjam"])
            print("")

#fungsi dengan Duck Typing: Bisa menerima objek apapun yang memiliki metode tampilkan_info
def cetak_info(media):
    print(media.tampilkan_info())

#program utama
buku1 = Buku("Python Programming", "John Doe", 2023, 300)  #objek Buku
ebook1 = EBook("Data Science Basics", "Jane Smith", 2023, "PDF")  #objek EBook

#membuat manager peminjaman
manager = PeminjamanManager()

#menampilkan informasi media (Polimorfisme - metode yang sama, hasil berbeda)
print("======== Perpustakaan ========")
cetak_info(buku1)  #mencoba duck Typing
print("")
cetak_info(ebook1)  #mencoba duck Typing

#mencoba peminjaman
print("\n=== Mencoba Peminjaman ===")
if manager.catat_peminjaman(buku1, "Ali"):
    print("Buku berhasil dipinjam!")

if manager.catat_peminjaman(ebook1, "Budi"):
    print("EBook berhasil dipinjam!")

#menampilkan riwayat peminjaman
print("\n=== Riwayat Peminjaman ===")
manager.tampilkan_riwayat()

#mengakses operator overloading
print(buku1 + ebook1)
