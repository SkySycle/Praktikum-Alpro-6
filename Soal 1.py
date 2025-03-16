def perkalian(a, b):
    hasil = 0
    for _ in range(a):
        hasil += b
    return hasil

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = perkalian(angka1, angka2)
print(f"{angka1} x {angka2} = {' + '.join([str(angka2)] * angka1)} = {hasil}")