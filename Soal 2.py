def ganjil(bawah, atas):
    if bawah < atas:
        start, end, step = bawah, atas, 1
    else:
        start, end, step = bawah, atas, -1

    if start % 2 == 0:
        start += step
    
    hasil = []
    for i in range(start, end + step, step * 2):
        hasil.append(i)
    
    return hasil

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

print(", ".join(map(str, ganjil(bawah, atas))))