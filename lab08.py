#71200670 Renaldo Surya Saputra

'''Renal adalah seorang progammer pemula. Dia inginj mengembangkan bakatnya 
melalui berlatih membuat progamnya sendiri. Saat ini Ia memiliki keninginan untuk membuat 
program yang berhubungan mengenai topik pada python yaitu file. 
sehingga ia ingin membuat program file dengan topik hasil dari faktorial dan nanti ouputnya akan
ditampilkan pada dokumen text.

input : angka untuk faktorial

Proses :
penghitungan faktorial menggunakan perulangan pada python
membuka teks folder
menampikan hasil faktorial pada dokumen teks

Output : 
hasil dari faktorial yang telah diinputkan

'''
def faktorial(n) :
    file1 = open("teksoutput.txt", 'w')
    fakt = 1
    for i in range(1, n + 1) :
        fakt = fakt * i 
    file1.write(str(fakt))
    file1.close()
    return ("Berhasil ditampilkan")

n = int(input("Masukan angka : "))
print(faktorial(n))



