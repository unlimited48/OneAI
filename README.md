# OneAI
​🚀 OneAI: The Ultimate Termux AI Engine 🤖
OneAI adalah skrip Python canggih yang dirancang khusus untuk lingkungan Termux (Android). Ini bukan sekadar chatbot biasa; ini adalah asisten sistem pintar yang terintegrasi dengan API OpenRouter, dilengkapi dengan fitur self-patching, manajemen database lokal, hingga sandbox terminal untuk bereksperimen dengan aman! 💻✨

​✨ Fitur Unggulan

​

🧠 Multi-Persona AI: Ubah gaya bicara AI sesuai kebutuhanmu (Teman, Tsundere, Profesional, atau Pakar Coding).
​


🛠️ Self-Coder (Auto-Patching): AI bisa memodifikasi dan memperbarui kodenya sendiri secara cerdas! (Fitur keamanan: Anti-Edit Mode).

​

📡 Smart Router API: Otomatis menangani limit API (429 Error), backoff sistem, dan fallback model jika satu model sedang down.

​

🔍 Browser & Search: Terintegrasi dengan berbagai mesin pencari populer untuk kebutuhan riset.



​🔐 Jaringan Aman: Mendukung koneksi via Tor (SOCKS5) untuk anonimitas maksimal.
​


🧪 Sandbox Terminal: Jalankan perintah Linux/Termux di dalam lingkungan yang terisolasi dengan filter keamanan.
​


📚 Database Belajar: AI memiliki "ingatan" jangka panjang melalui sistem database lokal.
​


🎨 UI Neon & Interaktif: Tampilan terminal penuh warna (ANSI 256-color) yang memanjakan mata! 🌈
​
🛠️ Cara Penggunaan (Tutorial)
​1. Persiapan Awal
​Pastikan Anda sudah menginstal Python di Termux:
pkg update && pkg upgrade
pkg install python git

2. Clone Repository

git clone https://github.com/unlimited48/OneAI
cd OneAI

3. Menjalankan OneAI
   
python OneAI.py

Saat pertama kali dijalankan, skrip akan otomatis mendeteksi modul yang hilang dan merapikan struktur file. 🛠️

​4. Konfigurasi API Key
​Masuk ke Menu 5 (Kelola Key Interaktif).
​Masukkan API Key OpenRouter Anda (format: sk-or-v1-...).
​Sekarang Anda siap berinteraksi! 🚀

💡 Perintah Pintasan (Chat Mode)
​Saat berada di mode obrolan, Anda bisa menggunakan pintasan berikut:

​!help : Melihat panduan lengkap.
​!run <perintah> : Mengeksekusi perintah terminal langsung dari chat.
​!browsing <query> : Mencari informasi dari web.
​!ingat <fakta> : Menyimpan informasi ke database memori jangka panjang AI.
​!tor : Mengecek status anonimitas koneksi.

​⚠️ Peringatan Keamanan
​Anti-Edit Mode: Aktif secara default untuk mencegah modifikasi skrip yang tidak diinginkan. 

Matikan di menu 23 jika Anda
memberikan izin akses self-patching kepada AI.
​Gunakan dengan bijak! Jangan memasukkan perintah berbahaya ke dalam Sandbox. 🛡️

​💖 Dukung Proyek Ini
​Jika Anda menyukai OneAI, jangan lupa berikan ⭐ (Star) pada repository ini
​Dibuat dengan sepenuh hati untuk komunitas Termux & AI Enthusiast. 🤖✨

​Disclaimer: Script ini dibuat untuk tujuan edukasi dan produktivitas. Pengguna bertanggung jawab penuh atas penggunaan API Key dan aktivitas di terminal masing-masing.
