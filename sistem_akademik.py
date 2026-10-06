"""
Tugas Mandiri 1a - Sistem Akademik (Data Mahasiswa)
Menunjukkan penggunaan struktur data: List, Stack, Queue, dan Dictionary (Hash Table)
"""
from collections import deque


class Mahasiswa:
    def __init__(self, nim, nama, prodi):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi

    def __repr__(self):
        return f"[{self.nim}] {self.nama} - {self.prodi}"


# ------------------------------------------------------------------
# a. Penyimpanan data secara berurutan -> ARRAY (list Python)
# ------------------------------------------------------------------
daftar_mahasiswa = []  # <-- STRUKTUR DATA: Array/List

def tambah_mahasiswa(mhs):
    daftar_mahasiswa.append(mhs)          # O(1)
    riwayat_undo.append(("tambah", mhs))  # simpan aksi ke stack

def tampilkan_semua():
    for i, m in enumerate(daftar_mahasiswa):  # akses berurutan via indeks
        print(f"  {i}. {m}")


# ------------------------------------------------------------------
# b. Fitur Undo -> STACK (LIFO)
# ------------------------------------------------------------------
riwayat_undo = []  # <-- STRUKTUR DATA: Stack (push = append, pop = pop)

def undo():
    if not riwayat_undo:                  # cek stack kosong
        print("  Tidak ada aksi untuk di-undo.")
        return
    aksi, mhs = riwayat_undo.pop()        # pop elemen teratas, O(1)
    if aksi == "tambah":
        daftar_mahasiswa.remove(mhs)
        indeks_nim.pop(mhs.nim, None)
        print(f"  Undo: penambahan {mhs.nama} dibatalkan.")


# ------------------------------------------------------------------
# c. Sistem antrean pengolahan data -> QUEUE (FIFO)
# ------------------------------------------------------------------
antrean_proses = deque()  # <-- STRUKTUR DATA: Queue (deque)

def masuk_antrean(mhs):
    antrean_proses.append(mhs)            # enqueue, O(1)

def proses_antrean():
    while antrean_proses:
        mhs = antrean_proses.popleft()    # dequeue, O(1)
        print(f"  Memproses data: {mhs}")


# ------------------------------------------------------------------
# d. Pencarian data berdasarkan key -> DICTIONARY (Hash Table)
# ------------------------------------------------------------------
indeks_nim = {}  # <-- STRUKTUR DATA: Hash Table, key = NIM

def cari_by_nim(nim):
    return indeks_nim.get(nim)            # rata-rata O(1)


def daftarkan(mhs):
    """Menambah data ke list, stack undo, dan indeks pencarian."""
    tambah_mahasiswa(mhs)
    indeks_nim[mhs.nim] = mhs


# ------------------------------------------------------------------
# Program utama
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=== a. Penyimpanan berurutan (Array/List) ===")
    daftarkan(Mahasiswa("1201", "Aulia", "Teknik Informatika"))
    daftarkan(Mahasiswa("1202", "Budi", "Teknik Informatika"))
    daftarkan(Mahasiswa("1203", "Citra", "Teknik Informatika"))
    tampilkan_semua()

    print("\n=== b. Fitur Undo (Stack / LIFO) ===")
    undo()  # membatalkan penambahan Citra
    tampilkan_semua()

    print("\n=== c. Antrean pengolahan data (Queue / FIFO) ===")
    for m in daftar_mahasiswa:
        masuk_antrean(m)
    proses_antrean()

    print("\n=== d. Pencarian berdasarkan key (Dictionary) ===")
    hasil = cari_by_nim("1201")
    print("  Cari NIM 1201:", hasil if hasil else "tidak ditemukan")
    hasil = cari_by_nim("9999")
    print("  Cari NIM 9999:", hasil if hasil else "tidak ditemukan")