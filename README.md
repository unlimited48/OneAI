[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![The Real OneAI](https://img.shields.io/badge/OneAI-Official_Build-ff0000.svg)](https://github.com/unlimited48/OneAI)
[![DMCA Protected](https://img.shields.io/badge/DMCA-Protected-success.svg)](https://github.com/unlimited48/OneAI/blob/main/NOTICE)
[![GitHub last commit](https://img.shields.io/github/last-commit/unlimited48/OneAI)](https://github.com/unlimited48/OneAI/commits/main)
[![Termux](https://img.shields.io/badge/For-Termux-black?logo=android)](https://termux.dev)
[![GitHub Repo stars](https://img.shields.io/github/stars/unlimited48/OneAI?style=social)](https://github.com/unlimited48/OneAI/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/unlimited48/OneAI?style=social)](https://github.com/unlimited48/OneAI/network/members)
# 🚀 OneAI: The Ultimate Termux AI Engine

OneAI adalah skrip Python canggih yang dirancang khusus untuk lingkungan Termux (Android). Ini bukan sekadar chatbot biasa; ini adalah asisten sistem pintar yang terintegrasi dengan API OpenRouter, dilengkapi dengan fitur self-patching, manajemen database lokal, hingga sandbox terminal untuk bereksperimen dengan aman! 🖥️📱

Mau ikut bantu? Cek [CONTRIBUTING.md](CONTRIBUTING.md) buat panduan kontribusi.

🌟 Fitur Unggulan
- 🧠 *Multi-Persona AI*: Ubah gaya bicara AI sesuai kebutuhanmu (Teman, Tsundere, Profesional, atau Pakar Coding).
- 🛠️ *Self-Coder (Auto-Patching)*: AI bisa memodifikasi dan memperbarui kodenya sendiri secara cerdas! (Fitur keamanan: Anti-Edit Mode).
- 📡 *Smart Router API*: Otomatis menangani limit API (429 Error), backoff sistem, dan fallback model jika satu model sedang down.
- 🌐 *Browser & Search*: Terintegrasi dengan berbagai mesin pencari populer untuk kebutuhan riset.
- 🔒 *Jaringan Aman*: Mendukung koneksi via Tor (SOCKS5) untuk anonimitas maksimal.
- 📝 *Sandbox Terminal*: Jalankan perintah Linux/Termux di dalam lingkungan yang terisolasi dengan filter keamanan.
- 💾 *Database Belajar*: AI memiliki "ingatan" jangka panjang melalui sistem database lokal.
- 🎨 *UI Neon & Interaktif*: Tampilan terminal penuh warna (ANSI 256-color) yang memanjakan mata!

🚀 Cara Penggunaan (Tutorial)

1. Persiapan Awal
Pastikan Anda sudah menginstal Python di Termux:
pkg update && pkg upgrade
pkg install python git
2. Clone Repository
git clone https://github.com/unlimited48/OneAI
cd OneAI
3. Menjalankan OneAI
python OneAI.py
Saat pertama kali dijalankan, skrip akan otomatis mendeteksi modul yang hilang dan merapikan struktur file. 🛠️

4. Konfigurasi API Key
Masuk ke `Menu 5` (Kelola Key Interaktif). Masukkan API Key OpenRouter Anda (format: `sk-or-v1-...`). Sekarang Anda siap berinteraksi! ✨

## ⌨️ Usage

Launch OneAI by typing:  
`python OneAI.py`

## 🚀 Show menu

| Command | Action |
| --- | --- |
| `1` | Mulai Mengobrol |
| `2` | Ganti / Tambah Persona |
| `3` | Ganti / Tambah Model AI |
| `4` | Cek Cepat Semua Status Key |
| `5` | Kelola Key Interaktif |
| `6` | Cek Limit & Info Model AI |
| `7` | Kelola Dokumen ToS |
| `8` | Fitur Tambahan Termux & Sandbox |
| `9` | KELOLA LIBRARY PYTHON TUX |
| `10` | KELOLA DB & PLUGINS KUSTOM |
| `11` | AUTO-PATCHER / AI SELF-CODER |
| `12` | MENU SETTING COPILOT KUSTOM |
| `13` | TOGGLE AUTO UPDATE AI TO SCRIPT |
| `14` | KELOLA DOMAIN SEARCH ENGINE |
| `15` | CEK KESEHATAN SCRIPT & REPAIR |
| `16` | CONFIG BELAJAR (WHITELIST WEB) |
| `17` | LIHAT & HAPUS chip_core.OneAI.metadata.db |
| `18` | PANEL MANAGEMENT OFFLINE AI |
| `19` | LIVE AI GRATIS OPENROUTER (TRENDING) |
| `20` | CEK & HAPUS BERKAS LOG AKTIVITAS |
| `21` | BERSIHKAN RAM CACHE AI |
| `22` | TOGGLE COPILOT MODE (ON/OFF) |
| `23` | TOGGLE ANTI-EDIT SCRIPT CODES (ON/OFF) |
| `X` | Keluar Aplikasi |

💡 Perintah Pintasan (Chat Mode)
Saat berada di mode obrolan, Anda bisa menggunakan pintasan berikut:
- `!help` : Melihat panduan lengkap
- `!run` : Mengeksekusi perintah terminal langsung dari chat
- `!browsing` : Mencari informasi dari web
- `!ingat` : Menyimpan informasi ke database memori jangka panjang AI
- `!tor` : Mengecek status anonimitas koneksi

⚠️ Peringatan Keamanan
*Anti-Edit Mode*: Aktif secara default untuk mencegah modifikasi skrip yang tidak diinginkan. Matikan di menu 23 jika Anda memberikan izin akses self-patching kepada AI. Gunakan dengan bijak! Jangan memasukkan perintah berbahaya ke dalam Sandbox. 🛡️

💖 Dukung Proyek Ini
Jika Anda menyukai OneAI, jangan lupa berikan ⭐ (Star) pada repository ini!

Dibuat dengan sepenuh hati untuk komunitas Termux & AI Enthusiast. 🤖📱

---
*Disclaimer*: Script ini dibuat untuk tujuan edukasi dan produktivitas. Pengguna bertanggung jawab penuh atas penggunaan API Key dan aktivitas di terminal masing-masing.

*The Real OneAI™ - Only at unlimited48/OneAI*
