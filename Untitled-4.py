from datetime import datetime
import pytz
import time

def display_time():
    # Menentukan timezone UTC+7
    timezone = pytz.timezone("Asia/Jakarta")
    
    # Mendapatkan waktu saat ini dengan timezone UTC+7
    now = datetime.now(timezone)
    
    # Menampilkan waktu saat ini
    print("===================================")
    print("Nama: Reza nugraha santoso")
    print("Nim: 064002100005")
    print("===================================")
    print(f"Timezone: {timezone}")
    print(f"Tanggal: {now.date()}")
    print(f"Waktu: {now.time()}")
    print("\nBerubah Menjadi\n")
    
    # Menunggu beberapa milidetik
    time.sleep(0.1)
    
    # Mendapatkan waktu saat ini lagi
    now_updated = datetime.now(timezone)
    
    # Menampilkan waktu yang telah diperbarui
    print(f"Tanggal: {now_updated.date()}")
    print(f"Waktu: {now_updated.time()}")

if __name__ == "__main__":
    display_time()
