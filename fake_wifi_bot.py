
import requests
import sys

def kendali_wifi_palsu(aksi):
    url = "http://localhost:8000/control_panel.php"  # Ubah ini ke URL sebenarnya dari file PHP Anda
    data = {'aksi': aksi}
    response = requests.post(url, data=data)
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python3 fake_wifi_bot.py <mulai|hentikan>")
        sys.exit(1)
    
    aksi = sys.argv[1].strip().lower()
    if aksi in ["mulai", "hentikan"]:
        kendali_wifi_palsu(aksi)
    else:
        print("Aksi tidak valid. Silakan masukkan 'mulai' atau 'hentikan'.")

