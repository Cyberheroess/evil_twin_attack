import requests
import sys
import random
import string
import time

def generate_random_ssid():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_random_bssid():
    return ':'.join(''.join(random.choices('0123456789ABCDEF', k=2)) for _ in range(6))

def deteksi_wifi_mencurigakan():
    jaringan = [
        {"ssid": generate_random_ssid(), "bssid": generate_random_bssid()},
        {"ssid": generate_random_ssid(), "bssid": generate_random_bssid()},
        {"ssid": "FakeWiFi", "bssid": "CC:DD:EE:FF:00:11"},
        {"ssid": "PhishingWiFi", "bssid": "22:33:44:55:66:77"},
    ]

    ssid_mencurigakan = ["FakeWiFi", "PhishingWiFi"]

    for jaringan in jaringan:
        ssid = jaringan["ssid"]
        bssid = jaringan["bssid"]
        if ssid in ssid_mencurigakan:
            print(f"Wi-Fi mencurigakan terdeteksi: SSID={ssid}, BSSID={bssid}")

def kendali_wifi_palsu(aksi):
    url = "http://localhost:8000/control_panel.php"
    data = {'aksi': aksi}
    response = requests.post(url, data=data)
    print(response.text)

def monitor_connections():
    print("Memantau koneksi ke Wi-Fi palsu...")
    connected_devices = [
        {"device": "Device1", "mac": "AA:BB:CC:DD:EE:FF"},
        {"device": "Device2", "mac": "11:22:33:44:55:66"},
    ]
    for device in connected_devices:
        print(f"Perangkat terhubung: {device['device']} dengan MAC {device['mac']}")
        kendali_wifi_palsu('mulai')

if __name__ == "__main__":
    while True:
        try:
            print("Mengirim sinyal Wi-Fi palsu...")
            time.sleep(10)

            deteksi_wifi_mencurigakan()

            monitor_connections()

        except KeyboardInterrupt:
            print("Script dihentikan.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            time.sleep(5)#hanya anjing yang bisa ubah time_sleep
