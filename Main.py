# Comma-Separated Values
import csv

# Data awal sebagai daftar dari daftar
data = [['Name', 'NIM', 'Semester'],
        ['Andi', '11119', '1'],
        ['Bima', '11112', '1'],
        ['Rahma', '11131', '3'],
        ['Zeno', '11198', '9'],
        ['Rahma', '11131', '3'],
        ['Andi', '11119', '1']]

# ini baris code buat ngilangin dupe
unique_data = set(tuple(row) for row in data)

# gandengan dari baris code di atas
unique_data = [list(row) for row in unique_data]

# buat nulis data unik ke dalam sebuah file
with open('data_mahasiswa.txt', 'w', newline='') as f:
    # Buat objek penulis CSV
    writer = csv.writer(f)

    # Tulis data unik ke dalam file
    writer.writerows(unique_data)
