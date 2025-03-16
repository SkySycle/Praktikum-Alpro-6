def hitung_ips():
    try:
        jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
        total_bobot = 0
        total_sks = jumlah_mk * 3 
        
        for i in range(jumlah_mk):
            nilai = input(f"Masukkan nilai (A/B/C/D) untuk mata kuliah {i+1}: ").upper()
            
            if nilai == 'A':
                bobot = 4
            elif nilai == 'B':
                bobot = 3
            elif nilai == 'C':
                bobot = 2
            elif nilai == 'D':
                bobot = 1
            else:
                print("Nilai tidak valid! Masukkan hanya A, B, C, atau D.")
                return
            
            total_bobot += bobot * 3
        
        ips = total_bobot / total_sks
        print(f"Indeks Prestasi Semester (IPS) Anda: {ips:.2f}")
    
    except ValueError:
        print("Input tidak valid! Masukkan angka untuk jumlah mata kuliah.")

hitung_ips()
