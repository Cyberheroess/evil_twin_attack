![alt text](![17319738335302900830042491312860](https://github.com/user-attachments/assets/abba24f5-30d4-4936-8b80-ecf99c0bf8c8)
?raw=true)
# Panduan Penggunaan Script Wi-Fi Palsu

## Pendahuluan
Panduan ini menjelaskan cara menggunakan script Wi-Fi palsu yang terdiri dari beberapa file:
1. `wifi_palsu_bot.py`
2. `control_panel.php`
3. `fake_wifi_bot.py`
4. `keamanan_wifi.py`

## Persiapan Lingkungan
Pastikan Anda memiliki lingkungan yang sesuai untuk menjalankan script ini. Anda memerlukan:
- Python 3
- PHP
- `tmux` (untuk menjalankan script di latar belakang)

### Instalasi PHP dan `tmux`
```bash
apt install tsu
sudo apt-get update
sudo apt-get install php tmux -y
sudo apt-get install git
git clone https://github.com/Cyberheroess/Cyberheroess.git
```

## Deskripsi File

### 1. `bot_wifi_palsu.py`
Script ini berjalan terus-menerus, mengirim sinyal Wi-Fi palsu, mendeteksi jaringan Wi-Fi mencurigakan, memantau koneksi, dan mengirim data ke server.

#### Cara Menjalankan
1. Jalankan script di latar belakang menggunakan `tmux`:
    ```bash
    tmux new-session -d -s bot_wifi_palsu_session 'python3 bot_wifi_palsu.py'
    ```

2. Untuk memeriksa output, lampirkan ke sesi `tmux`:
    ```bash
    tmux attach-session -t bot_wifi_palsu_session
    ```

### 2. `control_panel.php`
File PHP ini menangkap data seperti nomor telepon, lokasi, dan foto kamera, lalu mengirimkannya ke server.

#### Cara Menjalankan
1. Jalankan server PHP:
    ```bash
    php -S localhost:8000
    ```

### 3. `fake_wifi_bot.py`
Script ini dapat memulai dan menghentikan Wi-Fi palsu, mendeteksi jaringan Wi-Fi mencurigakan, dan memantau koneksi.

#### Cara Menjalankan
1. Untuk memulai Wi-Fi palsu:
    ```bash
    python3 fake_wifi_bot.py mulai
    ```

2. Untuk menghentikan Wi-Fi palsu:
    ```bash
    python3 fake_wifi_bot.py hentikan
    ```

3. Untuk mendeteksi jaringan Wi-Fi mencurigakan:
    ```bash
    python3 fake_wifi_bot.py deteksi
    ```

4. Untuk memantau koneksi:
    ```bash
    python3 fake_wifi_bot.py monitor
    ```

### 4. `keamanan_wifi.py`
Script ini mendeteksi jaringan Wi-Fi mencurigakan.

#### Cara Menjalankan
1. Jalankan script:
    ```bash
    python3 keamanan_wifi.py
    ```
