def deteksi_wifi_mencurigakan():
    jaringan = [
        {"ssid": "HomeWiFi", "bssid": "00:11:22:33:44:55"},
        {"ssid": "OfficeWiFi", "bssid": "66:77:88:99:AA:BB"},
        {"ssid": "FakeWiFi", "bssid": "CC:DD:EE:FF:00:11"},
        {"ssid": "PhishingWiFi", "bssid": "22:33:44:55:66:77"},
    ]

    ssid_mencurigakan = ["FakeWiFi", "PhishingWiFi"]

    for jaringan in jaringan:
        ssid = jaringan["ssid"]
        bssid = jaringan["bssid"]
        if ssid in ssid_mencurigakan:
            print(f"Wi-Fi mencurigakan terdeteksi: SSID={ssid}, BSSID={bssid}")

if __name__ == "__main__":
    deteksi_wifi_mencurigakan()
