"""
O(n^2) grows in complexity much more rapidly. 
That said, for small and medium input sizes, these algorithms can still be very useful.

A common reason an algorithm falls into O(n^2) is by using a nested loop, 
where the number of iterations of each loop is equal to the number of items in the input:

Karakteristik dari algoritma O(n^2) adalah jika ukuran input meningkat sebesar X kali lipat, maka waktu
eksekusi akan meningkat sebesar X^2 kali lipat.
Mari kita bedah data yang Anda berikan dengan melihat rasionya:
- Kondisi Awal: does_name_exist(10, 10) = 1 detik
- Kenaikan 1: Ukuran nama naik dari 10 ke 100 (10 kali lipat).
    - Waktu eksekusi: 1 detik x 10^2 = 1 detik x 100 = 100 detik.
- Kenaikan 2: Ukuran nama naik dari 10 ke 1.000 (100 kali lipat).
    - Waktu eksekusi: 1 detik x 100^2 = 1 detik x 10.000 = 10.000 detik.
- Kenaikan 3: Ukuran nama naik dari 10 ke 10.000 (1.000 kali lipat).
    - Waktu eksekusi: 1 detik x 1000^2 = 1 detik x 1.000.000 = 1.000.000 detik.
"""
def does_name_exist(
    first_names: list[str], last_names: list[str], full_name: str
) -> bool:
    # first_name, last_name = full_name.split(" ")

    for fname in first_names:
        for lname in last_names:
            completed_name = f"{fname} {lname}"
            if completed_name == full_name:
                return True

    return False
