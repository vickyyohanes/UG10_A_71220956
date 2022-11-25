print("=================================Selamat datang di Toko Andi Tersenyum, selamat belanja!================")
A = int(input("Total Belanja : Rp. "))
B = A - (A * 2/100)
C = A - (A * 5/100)
D = A - (A * 10/100)

if A >= 1000000 :
      print("Biaya yang harus dibayar setelah diskon adalah : ",D)
elif A >= 500000 :
      print("Biaya yang harus dibayar setelah diskon adalah : ", C)
elif A >= 100000 :
      print("Biaya yang harus dibayar setelah diskon adalah : ", B)
else    :
      print("Tidak ada diskon! Maka yang anda bayarkan adalah : ", A)
