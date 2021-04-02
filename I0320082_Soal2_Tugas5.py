# Membuat program grading nilai
# Memasukkan nama dan nilai
Nama_mahasiswa = input("Masukkan nama mahasiswa :")
Nilai = int(input("Masukkan nilai berupa angka :"))
info = 'Halo, ' + str(Nama_mahasiswa) + '! ' + 'Nilai anda setelah dikonversi adalah '

# Mengkonversikan nilai
if Nilai <= 100 and Nilai >= 85:
    print(info + 'A')
elif Nilai <= 84 and Nilai >= 80:
    print(info + 'A-')
elif Nilai <= 79 and Nilai >= 75:
    print(info + 'B+')
elif Nilai <= 74 and Nilai >= 70:
    print(info + 'B')
elif Nilai <= 65 and Nilai >= 69:
    print(info + 'C+')
elif Nilai <= 64 and Nilai >= 60:
    print(info + 'C')
elif Nilai < 60:
    print(info + 'E')
else :
    print(info + 'nilai tidak valid untuk dikonversi')
print()

