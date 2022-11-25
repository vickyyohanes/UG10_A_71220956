A = int(input(" Masukkan nilai soal 1 : "))
B = int(input(" Masukkan nilai soal 2 : "))
C = int(input(" Masukkan nilai soal 3 : "))
umur  = int(input(" Maukkan umur : "))
D = A * 50/100
E = B * 30/100
F = C * 20/100
total =D + E + F
print("Rata - rata nilai anda : ",round(total))

if umur <= 25 and total >=80:
        print("Selamat Anda Lulus !")
elif total >=90 and umur >= 25 :
        print("Selamat Anda  Lulus !")
else :
    print("Coba lagi tahun depan")
              


        
