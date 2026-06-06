"""
Notasi O(nm) digunakan ketika performa suatu algoritma bergantung pada dua variabel input yang berbeda.
Jika pada Notasi O(n^2) kita mengasumsikan sebuah matriks berbentuk persegi,
maka pada Notasi O(nm) kita mengasumsikan sebuah matriks berbentuk persegi panjang,
di mana n adalah jumlah baris dan m adalah jumlah kolom.

# Contoh Kode O(nm)
for i in range(n):        # Berjalan sebanyak n kali
    for j in range(m):    # Berjalan sebanyak m kali
        # Eksekusi kode/operasi di sini
"""
def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:
    count_found_string = 0
    
    for i in all_handles:
        for j in i:
            if brand_name in j:
                count_found_string += 1

    return count_found_string / len(all_handles)
