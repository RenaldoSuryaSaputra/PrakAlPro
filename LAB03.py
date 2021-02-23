#71200670_Renaldo Surya Saputra

'''Deka adalah seorang progammer yang baru saja diterima di perusahaan listrik yang baru berdiri. 
sebagai tugas awal, Deka diminta perusahaan untuk membuat program pemberitahu gaji untuk setiap karyawan.
dengan ketentuan jika karyawan sudah berkeluarga, maka gaji pokok akan ditambah 500.000.
Program yan harus dibuat berdasarkan status pekerja di perusahaan (manajer mendapat gaji pokok sebesar 8juta,
 dan karyawan sebesar 5 juta ).
'''
'''
input : nama ; status diperusahaan ; status sudah berkeluarga atau belum


proses : 
1. mengetahui apakah status manajer sudah berkeluarga atau belum 
2. menampilkan jumlah gaji manajer
3. mengetahui apakah ststus karyawan sudah berkeluarga atau bekum
4. menampilkan jumlah gaji karyawan

output :
1. jumlah gaji manajer berkeluarga
2. jumlah gaji manajer yang belum berkeluarga
3. jimlah gaji karyawan sudah berkeluarga
4. jumlah gaji karyawan belum berkeluarga
5. tidak ada statusnya diperusahaan


'''

nama = input("masukan nama anda :")
statusP = input("status anda di perusahaan :")
statusK = input("apakah sudah berkeluarga (ya/tidak) :")

if statusP == "manajer" :
    if statusK == "ya" :
        print("Gaji anda saat ini sebesar Rp 8.500.000")
    else :
        print("gaji anda saat ini sebesar Rp 8.000.000")
elif statusP == "karyawan" :
    if statusK == "ya" :
        print("gaji anda saat ini sebesar Rp 5.500.000")
    else :
        print("gaji anda saat ini sebesar Rp 5.000.000")
else :
    print("status yang anda masukan tidak tersedia")

