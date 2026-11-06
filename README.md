# Habits Queen

![Logo](logo.svg)

Aplikasi catatan pribadi untuk perempuan muslimah: mencatat kapan haid, nifas, dan istihadhah, lalu menunjukkan kewajiban dan larangan pada masa itu.

## Fitur

- **Login PIN**: nama panggilan dan PIN 4 angka. Aplikasi terkunci lagi bila ditinggal lebih dari 2 menit, dan bisa dikunci manual lewat tombol Kunci. PIN disimpan sebagai hash; ini kunci privasi di perangkat, bukan enkripsi.
- **Tampilan terang dan gelap**: pilih Terang, Gelap, atau Otomatis (ikut perangkat) lewat tombol di pojok kanan atas. Pilihan tersimpan.
- **Amalan**: checklist amalan harian (dzikir pagi/petang, istighfar, shalawat, murattal, ilmu, doa, kebaikan) dengan rangkaian hari beruntun dan grafik 7 hari; tasbih digital untuk 8 dzikir dengan target 33/100/1000; bacaan sayyidul istighfar dan doa; penjelasan membaca Al-Qur'an saat haid; tautan murattal ke quran.com.
- **Tips harian**: tips seputar haid dan ibadah untuk remaja.
- **Hari ini**: status saat ini (haid, nifas, istihadhah, atau suci), hitungan hari, tanggal hijriah, daftar larangan dan kewajiban, langkah setelah suci, serta niat mandi wajib.
- **Kalender**: tanggal berwarna per jenis darah, tanggal hijriah, dan perkiraan haid berikutnya.
- **Riwayat**: tambah, ubah, dan hapus catatan, lengkap dengan hukumnya.
- **Panduan**: batas waktu dan ringkasan fikih haid, nifas, istihadhah, dan mandi wajib.
- **Hutang puasa Ramadan**: dihitung otomatis dari hari haid/nifas di bulan Ramadan.

## Aturan yang dipakai (mazhab Syafi'i)

| Batas | Waktu |
|---|---|
| Minimal haid | 24 jam |
| Maksimal haid | 15 hari |
| Minimal suci di antara dua haid | 15 hari |
| Umumnya nifas | 40 hari |
| Maksimal nifas | 60 hari |

Aplikasi ini alat bantu mencatat, bukan fatwa. Untuk kasus yang rumit, tanyakan kepada ustadzah.

## Menjalankan

Dari folder ini, jalankan server lokal lalu buka http://localhost:8090:

```bash
python -m http.server 8090 --bind 127.0.0.1
```

Catatan disimpan di `localStorage` peramban perangkat itu.

Kode utama ada di `habbits-queen.html`. Setelah mengubahnya, jalankan `python build.py` untuk membuat ulang `index.html`.
