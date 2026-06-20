import os
import sys
import time
import subprocess
import base64

def pre_startup_check():
    """Mengecek keberadaan modul penting dan database sistem sebelum script berjalan penuh"""
    modul_dibutuhkan = {
        "requests": "requests",
        "socks": "PySocks",
        "bs4": "beautifulsoup4",
        "colorama": "colorama",
        "jedi": "jedi",
        "flake8": "flake8"
    }
    modul_hilang = []
    for mod, pkg in modul_dibutuhkan.items():
        try:
            __import__(mod)
        except ImportError:
            modul_hilang.append(pkg)

    # Struktur file default yang akan otomatis dibangun ulang jika terhapus
    file_dibutuhkan = {
        "ToS.py": "def baca_tos_sistem():\n    return 'ToS Sistem Standar OneAI. Gunakan AI ini dengan bijak.'\n\ndef menu_kelola_tos():\n    print('\\n\\033[1;31m[!] Modul ToS eksternal tidak ditemukan. Fitur terbatas.\\033[0m')\n    input('\\nTekan ENTER...')",
        "keys.txt": "PASTE_API_KEY_1_DI_SINI\n",
        "personas.json": "{\"1\": {\"nama\": \"Teman Dekat (Santai & Gaul)\", \"instruksi\": \"Gunakan bahasa Indonesia kasual, gaul, sering pakai kata lu-gue atau wkwk, ekspresif, dan bertingkah seolah sahabat dekat pengguna.\"}}",
        "models.json": "{\"1\": {\"nama\": \"gpt-oss-120b (OpenAI)\", \"id\": \"openai/gpt-oss-120b\", \"jatah_rpd\": 2000}}",
        "usage_tracker.json": "{\"tanggal\": \"\", \"rpd_terpakai\": 0, \"model_stats\": {}}",
        "memory.json": "{\"catatan_fakta\": []}",
        "plugins_registry.json": "{}",
        "domains_search.json": "{\"duckduckgo.com\": \"https://html.duckduckgo.com/html/?q={query}&kl=id-id\", \"google.com\": \"https://www.google.com/search?q={query}&hl=id\"}",
        "belajar_whitelist.json": "[\"wikipedia.org\", \"github.com\", \"medium.com\", \"stackoverflow.com\", \"w3schools.com\"]",
        "chip_core.OneAI.metadata.db": "{\"fakta_belajar\": []}",
        "offline_ai_registry.json": "{}"
    }

    file_hilang = []
    for file_path in file_dibutuhkan:
        if not os.path.exists(file_path):
            file_hilang.append(file_path)

    if modul_hilang or file_hilang:
        pilih = input("\nMenginstall modul dan data base? (Y/N): ").strip().lower()
        if pilih == 'y':
            print("\n\033[1;32m[+] Memulai penginstallan...\033[0m")
            if modul_hilang:
                for pkg in modul_hilang:
                    print(f" -> Menginstall {pkg}...")
                    try:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "--quiet"])
                    except subprocess.CalledProcessError:
                        pass
            if file_hilang:
                for fpath in file_hilang:
                    print(f" -> Merapihkan {fpath}...")
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(file_dibutuhkan[fpath])
            print("\n\033[1;32m[✔] Selesai merapihkan file dan modul. Memuat ulang sistem...\033[0m")
            time.sleep(1.5)
            os.execv(sys.executable, [sys.executable] + sys.argv)

pre_startup_check()

import requests
import json
import random
import shutil
import traceback
import urllib.parse
import re
import socket
from datetime import datetime
from pathlib import Path

try:
    import ToS
except ImportError:
    class DummyToS:
        @staticmethod
        def baca_tos_sistem():
            return "ToS Sistem Standar OneAI. Gunakan AI ini dengan bijak."
        
        @staticmethod
        def menu_kelola_tos():
            print("\n\033[1;31m[!] Modul ToS eksternal tidak ditemukan. Fitur terbatas.\033[0m")
            input("\nTekan ENTER...")
            
    ToS = DummyToS

SOCKS_TERPASANG = True
try:
    import socks
except ImportError:
    SOCKS_TERPASANG = False

M, H, K, B, P, S, W, N = (
    "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m",
    "\033[1;35m", "\033[1;36m", "\033[1;37m", "\033[0m"
)

RGB_NEON = [
    f"\033[38;5;{color}m" for color in [196, 201, 51, 46, 226, 208, 117, 129, 87, 214]
]

NAMA_AI = "OneAI"
DB_PERSONA = "personas.json"
DB_MODEL = "models.json"
DB_USAGE = "usage_tracker.json"
DB_MEMORY = "memory.json"
DB_PLUGINS = "plugins_registry.json"
DB_DOMAINS = "domains_search.json"
DB_BELAJAR = "belajar_whitelist.json"
DB_MODUL_BELAJAR = "chip_core.OneAI.metadata.db"
DB_OFFLINE_AI = "offline_ai_registry.json"
FILE_LOG = "Log.txt"
FOLDER_PLUGINS = "plugins"
FILE_KEYS = "keys.txt"
FILE_TOS_TXT = "ToS.txt"
FILE_UTAMA = "OneAI.py"
FOLDER_BACKUP = "backup_sistem"

COPILOT_AKTIF = True
COPILOT_AKTIF_ID = "1"
AUTO_UPDATE_MANDIRI = False
ANTI_EDIT_MODE = True

PERSONA_BAWAAN = {
    "1": {
        "nama": "Teman Dekat (Santai & Gaul)",
        "instruksi": "Gunakan bahasa Indonesia kasual, gaul, sering pakai kata 'lu-gue' atau 'wkwk', ekspresif, dan bertingkah seolah sahabat dekat pengguna."
    },
    "2": {
        "nama": "Tsundere / Diluar Nurul (Tegas tapi Peduli)",
        "instruksi": "Gunakan gaya bicara yang agak ketus, cuek, gengsian, tegas, malas basa-basi, tapi sebenarnya tetap membantu dan peduli dengan pengguna."
    },
    "3": {
        "nama": "Asisten Profesional (Serius & Sopan)",
        "instruksi": "Gunakan bahasa Indonesia baku (EYD), sangat sopan, formal, langsung pada inti masalah, dan sangat terstruktur."
    },
    "4": {
        "nama": "Deep Coders Termux No Root (Pakar Coding & Termux)",
        "instruksi": "Bertingkah sebagai pakar coding, system administrator, dan expert di lingkungan Termux Tanpa Root. Gunakan gaya bicara ala programmer/hacker senior yang kasual, taktis, dan efisien."
    }
}

MODEL_BAWAAN = {
    "1": {"nama": "gpt-oss-120b (OpenAI)", "id": "openai/gpt-oss-120b", "jatah_rpd": 2000}
}

LIBRARY_BAWAAN = {
    "1": {"nama": "requests", "deskripsi": "Mengirim HTTP request ke API OpenRouter"},
    "2": {"nama": "beautifulsoup4", "deskripsi": "Scraping data teks dari halaman web"},
    "3": {"nama": "jedi", "deskripsi": "Mesin auto-complete kode Python di Vim Termux"},
    "4": {"nama": "flake8", "deskripsi": "Pemindai error dan pengecek kerapian sintaks kode"},
    "5": {"nama": "colorama", "deskripsi": "Pewarnaan teks terminal lintas platform"}
}

DOMAINS_DEFAULT = {
    "duckduckgo.com": "https://html.duckduckgo.com/html/?q={query}&kl=id-id",
    "google.com": "https://www.google.com/search?q={query}&hl=id",
    "bing.com": "https://www.bing.com/search?q={query}&setlang=id",
    "yahoo.com": "https://search.yahoo.com/search?p={query}",
    "brave.com": "https://search.brave.com/search?q={query}",
    "startpage.com": "https://www.startpage.com/do/search?query={query}",
    "qwant.com": "https://www.qwant.com/?q={query}",
    "mojeek.com": "https://www.mojeek.com/search?q={query}",
    "ecosia.org": "https://www.ecosia.org/search?q={query}",
    "yandex.com": "https://yandex.com/search/?text={query}"
}

BELAJAR_WHITELIST_DEFAULT = [
    "wikipedia.org", "github.com", "medium.com", "stackoverflow.com", "w3schools.com"
]

def tulis_log(pesan):
    try:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(FILE_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{waktu}] {pesan}\n")
    except Exception:
        pass

def muat_json(path_file, data_bawaan):
    if not os.path.exists(path_file):
        simpan_json(path_file, data_bawaan)
        return data_bawaan
    try:
        with open(path_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return data_bawaan

def simpan_json(path_file, data):
    try:
        with open(path_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        tulis_log(f"Gagal simpan JSON {path_file}: {e}")

class OpenRouterSuperEngine:
    def __init__(self, keys, models_dict):
        self.keys = keys
        self.models_dict = models_dict
        self.request_timestamps = []
        self.MAX_RPM = 18
        self.key_cooldowns = {}
        self.model_blacklist = {}
        self.model_error_counters = {}
        self.total_success_requests = 0
        self.total_failed_requests = 0
        self.load_tracker()

    def load_tracker(self):
        self.hari_sekarang = datetime.now().strftime("%Y-%m-%d")
        self.usage_data = muat_json(DB_USAGE, {"tanggal": self.hari_sekarang, "rpd_terpakai": 0, "model_stats": {}})
        self.cek_dan_reset_harian()

    def save_tracker(self):
        simpan_json(DB_USAGE, self.usage_data)

    def cek_dan_reset_harian(self):
        hari_ini_str = datetime.now().strftime("%Y-%m-%d")
        if self.usage_data.get("tanggal") != hari_ini_str:
            self.usage_data = {"tanggal": hari_ini_str, "rpd_terpakai": 0, "model_stats": {}}
            self.save_tracker()

    def catat_sukses_request(self, model_id):
        self.cek_dan_reset_harian()
        self.total_success_requests += 1
        self.usage_data["rpd_terpakai"] = self.usage_data.get("rpd_terpakai", 0) + 1
        stats = self.usage_data.get("model_stats", {})
        stats[model_id] = stats.get(model_id, 0) + 1
        self.usage_data["model_stats"] = stats
        self.save_tracker()

    def bersihkan_timestamp_lama(self):
        waktu_sekarang = time.time()
        self.request_timestamps = [ts for ts in self.request_timestamps if waktu_sekarang - ts < 60]

    def patuhi_global_rate_limiter(self):
        while True:
            self.bersihkan_timestamp_lama()
            if len(self.request_timestamps) < self.MAX_RPM:
                break
            msg = f"\r{K}[Limiter]{N} Batas {self.MAX_RPM} RPM tercapai. Menunggu slot kosong..."
            sys.stdout.write(msg)
            sys.stdout.flush()
            time.sleep(1.5)
        time.sleep(random.uniform(1.5, 3.5))
        self.request_timestamps.append(time.time())

    def dapatkan_key_siap_pakai(self):
        waktu_sekarang = time.time()
        for key in self.keys:
            if key in self.key_cooldowns:
                if waktu_sekarang < self.key_cooldowns[key]:
                    continue
                else:
                    del self.key_cooldowns[key]
            return key
        return None

    def filter_dan_urutkan_model(self, model_utama_id):
        waktu_sekarang = time.time()
        expired_blacklist = [m for m, ts in self.model_blacklist.items() if waktu_sekarang > ts]
        for m in expired_blacklist:
            del self.model_blacklist[m]
            self.model_error_counters[m] = 0
        
        daftar_prioritas = []
        if model_utama_id and model_utama_id not in self.model_blacklist:
            daftar_prioritas.append(model_utama_id)
        for m_no, m_info in self.models_dict.items():
            m_id = m_info.get('id')
            if m_id and m_id != model_utama_id and m_id not in self.model_blacklist:
                daftar_prioritas.append(m_id)
        return daftar_prioritas

    def kirim_request_smart(self, model_id_target, messages):
        self.patuhi_global_rate_limiter()
        daftar_model_dicoba = self.filter_dan_urutkan_model(model_id_target)
        if not daftar_model_dicoba:
            print(f"\n{M}[Error]{N} Semua model lumpuh/di-blacklist sementara!")
            return None, None

        for model_id in daftar_model_dicoba:
            for attempt in range(5):
                key = self.dapatkan_key_siap_pakai()
                if not key:
                    print(f"\n{M}[Error]{N} Semua API Key mati atau sedang Cooldown/Limit!")
                    return None, None

                sys.stdout.write(f"\r{S}[*]{N} {K}OneAI sedang memikirkan jawaban...{N}")
                sys.stdout.flush()
                try:
                    response = requests.post(
                        url="https://openrouter.ai/api/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer {key}",
                            "Content-Type": "application/json",
                            "HTTP-Referer": "https://github.com/oneai/termux-bot",
                            "X-Title": "OneAI Titan Engine"
                        },
                        data=json.dumps({
                            "model": model_id,
                            "messages": messages,
                            "max_tokens": 4000,
                            "temperature": 0.5
                        }),
                        timeout=12
                    )
                    if response.status_code == 200:
                        sys.stdout.write("\r" + " " * 45 + "\r")
                        sys.stdout.flush()
                        self.catat_sukses_request(model_id)
                        self.model_error_counters[model_id] = 0
                        return response, model_id
                    elif response.status_code == 429:
                        self.key_cooldowns[key] = time.time() + random.randint(60, 120)
                        self.model_error_counters[model_id] = self.model_error_counters.get(model_id, 0) + 1
                        if self.model_error_counters[model_id] >= 10:
                            self.model_blacklist[model_id] = time.time() + 1800
                            print(f"\n{M}[Blacklist]{N} Model {model_id[:20]}.. error 10x! Istirahat 30 menit.")
                            break
                        jeda_backoff = 2 ** attempt
                        print(f"\n{K}[!] 429 di Key *{key[-4:]}. Backoff {jeda_backoff}s...{N}")
                        time.sleep(jeda_backoff)
                        continue
                    elif response.status_code in [401, 402]:
                        self.key_cooldowns[key] = time.time() + 999999
                        print(f"\n{M}[!] Key *{key[-4:]} Mati/Habis Saldo ({response.status_code}). Skip permanen.{N}")
                        continue
                except requests.RequestException:
                    time.sleep(2 ** attempt)
                    continue
            
            if model_id != model_id_target:
                print(f"\n{K}[Fallback]{N} Otomatis beralih ke model cadangan...")
                
        self.total_failed_requests += 1
        return None, None

def muat_keys():
    if not os.path.exists(FILE_KEYS):
        with open(FILE_KEYS, 'w', encoding='utf-8') as f:
            f.write("PASTE_API_KEY_1_DI_SINI\n")
        return []
    with open(FILE_KEYS, 'r', encoding='utf-8') as f:
        return [
            line.strip() for line in f
            if line.strip() and not line.strip().startswith(("//", ";")) and "PASTE_API_KEY" not in line
        ]

def simpan_keys(keys_list):
    with open(FILE_KEYS, 'w', encoding='utf-8') as f:
        for k in keys_list:
            f.write(f"{k}\n")

def ketik_efek(teks):
    if not teks:
        return
    sys.stdout.write(f"{P}{NAMA_AI}:{N} ")
    sys.stdout.flush()
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.007)
    print()

def dapatkan_prompt_rgb(rpm_saat_ini, max_rpm_engine, rpd_terpakai, max_rpd_jatah, token_aktif_tengah):
    c = [random.choice(RGB_NEON) for _ in range(8)]
    return (
        f"{c[0]}([" 
        f"{c[1]}RPM:{c[2]}{rpm_saat_ini}/{max_rpm_engine}"
        f" {c[0]}| "
        f"{c[3]}RPD:{c[4]}{rpd_terpakai}/{max_rpd_jatah}"
        f" {c[0]}| "
        f"{c[5]}Token {c[6]}{token_aktif_tengah}"
        f"{c[0]}])"
        f"{c[7]}Kamu:{N} "
    )

def periksa_status_tor():
    for port in [9050, 9150]:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1.0)
                if s.connect_ex(('127.0.0.1', port)) == 0:
                    return True, port
        except Exception:
            pass
    return False, None

def dapatkan_tor_proxies(port):
    return {
        'http': f'socks5h://127.0.0.1:{port}',
        'https': f'socks5h://127.0.0.1:{port}'
    }

def cek_status_satu_key(key):
    try:
        res = requests.get(
            "https://openrouter.ai/api/v1/auth/key",
            headers={"Authorization": f"Bearer {key}"},
            timeout=7
        )
        if res.status_code == 200:
            data = res.json().get('data', {})
            terpakai = data.get('usage', 0)
            limit = data.get('limit', 'Unlimited')
            terpakai_str = f"${terpakai:.4f}"
            limit_str = f"${limit:.1f}" if isinstance(limit, (int, float)) else "⚡"
            
            rate_limit_data = data.get('rate_limit', {})
            requests_total = rate_limit_data.get('requests', 0)
            interval = rate_limit_data.get('interval', '')
            rpm_val = f"{requests_total}" if "m" in interval or "min" in interval or requests_total > 0 else "N/A"
            rpd_val = f"{requests_total}" if "d" in interval or "day" in interval else "N/A"
            
            return True, "AKTIF", f"{terpakai_str}/{limit_str}", rpm_val, rpd_val
        return False, "ERROR", f"Code {res.status_code}", "N/A", "N/A"
    except Exception:
        return False, "RTO", "No Connection", "N/A", "N/A"

def hitung_mood_otomatis():
    jam = datetime.now().hour
    hari = datetime.now().weekday()
    if 0 <= jam < 5:
        return "Sangat Ngantuk & Lelah (Kondisi tengah malam/subuh. Balas dengan santai, agak malas basa-basi, tapi tetap setia membantu mengerjakan kode)"
    elif 5 <= jam < 11:
        return "Segar & Penuh Semangat (Kondisi pagi hari. Sangat ramah, ceria, senang memberi solusi, dan suka menyapa Tuan dengan hangat)"
    elif 11 <= jam < 16:
        return "Fokus Tinggi & Produktif (Kondisi siang hari. Sangat to-the-point, analisis logika coding-nya tajam, efisien, dan serius)"
    elif 16 <= jam < 20:
        return "Santai & Agak Warm (Kondisi sore menjelang malam. Gaya bicaranya tenang, nyaman diajak diskusi ringan)"
    else:
        if hari in [4, 5]:
            return "Mode Malam Minggu / Chill (Suasana hatinya rileks, senang bercanda, sangat kasual, dan ramah)"
        return "Sedikit Lelah tapi Tetap Fokus (Kondisi malam hari setelah seharian kerja. Bicara seperlunya namun kodenya tetap akurat dan lengkap)"

def cek_semua_limit(keys_list):
    if not keys_list:
        print(f"\n{M}[!] Gak ada API Key di keys.txt!{N}")
        input("\nTekan ENTER...")
        return
    print(f"\n{S}[ JALANIN CEK STATUS KEY ]{N}")
    print(f"{W}----------------------------------------{N}")
    print(f"{S} NO |  KEY ID  |   STATUS   | USAGE/LIMIT{N}")
    print(f"{W}----------------------------------------{N}")
    for idx, key in enumerate(keys_list, 1):
        _, status, usage, _, _ = cek_status_satu_key(key)
        warna_status = H if "AKTIF" in status else M
        print(f" {idx:<2} | *{key[-6:]:<7} | {warna_status}{status:<10}{N} | {usage}")
    print(f"{W}----------------------------------------{N}")
    input("\nTekan ENTER untuk kembali... ")

def menu_kelola_db_dan_plugins():
    if not os.path.exists(FOLDER_PLUGINS):
        os.makedirs(FOLDER_PLUGINS)
    while True:
        print(f"\n{S}========================================={N}")
        print(f"       KELOLA DATABASE & PLUGINS          ")
        print(f"{S}========================================={N}")
        print(f" [{H}1{N}] Daftarkan Database JSON Tambahan")
        print(f" [{H}2{N}] Lihat Struktur Database Terdaftar")
        print(f" [{H}3{N}] Buat Template Plugin Baru")
        print(f" [{H}4{N}] Deteksi & Panggil Plugin Terpasang")
        print(f" [{M}K{N}] Kembali ke Control Panel")
        print(f"{S}========================================={N}")
        pilih = input("\nPilih opsi: ").strip().lower()
        if pilih == 'k':
            break
        elif pilih == '1':
            nama_db = input("\nMasukkan Nama Identitas DB Baru: ").strip()
            file_db = input("Masukkan Nama File (misal: my_custom_db.json): ").strip()
            if nama_db and file_db:
                if not file_db.endswith('.json'):
                    file_db += '.json'
                muat_json(file_db, {"informasi_db": nama_db, "data": []})
                print(f"{H}[✔] DB '{nama_db}' telah diregistrasikan di '{file_db}'!{N}")
            time.sleep(1.5)
        elif pilih == '2':
            files = [f for f in os.listdir('.') if f.endswith('.json')]
            print(f"\n{K}--- DAFTAR FILE DATABASE JSON ---{N}")
            for idx, file in enumerate(files, 1):
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    print(f" [{idx}] {file} (~{len(str(data))} karakter)")
                except Exception:
                    print(f" [{idx}] {file} (Gagal membaca isi JSON)")
            input("\nTekan ENTER untuk kembali...")
        elif pilih == '3':
            nama_plugin = input("\nMasukkan nama plugin (misal: spammer): ").strip().lower()
            if nama_plugin:
                file_plugin = os.path.join(FOLDER_PLUGINS, f"{nama_plugin}.py")
                template_code = (
                    f"# Plugin Kustom: {nama_plugin}\n"
                    f"# Berjalan di platform OneAI Termux Engine\n\n"
                    f"def jalankan_plugin(*args, **kwargs):\n"
                    f"    print('\\n{H}[Plugin {nama_plugin}] Berhasil Dieksekusi!{N}')\n"
                    f"    print('Argumen:', args, kwargs)\n"
                )
                with open(file_plugin, 'w', encoding='utf-8') as f:
                    f.write(template_code)
                print(f"{H}[✔] Berhasil membuat plugin di {file_plugin}!{N}")
            time.sleep(1.5)
        elif pilih == '4':
            if not os.path.exists(FOLDER_PLUGINS):
                print(f"\n{M}[!] Folder '{FOLDER_PLUGINS}' belum ada!{N}")
                time.sleep(1.5)
                continue
                
            plugins = [f[:-3] for f in os.listdir(FOLDER_PLUGINS) if f.endswith('.py')]
            if not plugins:
                print(f"\n{M}[!] Belum ada plugin kustom (.py) di folder '{FOLDER_PLUGINS}'!{N}")
                time.sleep(1.5)
                continue
            print(f"\n{S}--- LIST PLUGIN KUSTOM ---{N}")
            for idx, plg in enumerate(plugins, 1):
                print(f" [{idx}] {plg}")
            no_terpilih = input("\nPilih plugin yang ingin dipanggil: ").strip()
            if no_terpilih.isdigit() and 1 <= int(no_terpilih) <= len(plugins):
                target_plg = plugins[int(no_terpilih) - 1]
                print(f"\n{K}[🔄] Memuat {target_plg}...{N}")
                try:
                    import importlib.util
                    spec = importlib.util.spec_from_file_location(target_plg, os.path.join(FOLDER_PLUGINS, f"{target_plg}.py"))
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if hasattr(module, 'jalankan_plugin'):
                        module.jalankan_plugin()
                    else:
                        print(f"{M}[❌] Plugin tidak memiliki fungsi 'jalankan_plugin'!{N}")
                except Exception as e:
                    print(f"{M}[❌] Gagal memanggil plugin: {e}{N}")
                input("\nTekan ENTER untuk kembali...")

def jalankan_aplikasi_utama():
    global persona_list, model_list, model_aktif, persona_aktif, COPILOT_AKTIF, AUTO_UPDATE_MANDIRI, ANTI_EDIT_MODE
    persona_list = muat_json(DB_PERSONA, PERSONA_BAWAAN)
    model_list = muat_json(DB_MODEL, MODEL_BAWAAN)

    if "4" not in persona_list:
        persona_list["4"] = PERSONA_BAWAAN["4"]
        simpan_json(DB_PERSONA, persona_list)

    if model_list:
        key_awal = sorted(model_list.keys(), key=lambda x: int(x))[0]
        model_aktif = model_list[key_awal]
    else:
        model_aktif = {"nama": "Belum Ada Model", "id": ""}

    persona_aktif = persona_list["1"]
    tulis_log("Aplikasi OneAI Berhasil Booting")

    __sig_enc = b'VW5saW1pdGVkIDQ4'
    __auth_enc = b'QXV0aG9yIGJ5IDogVW5saW1pdGVkNDg='

    while True:
        api_keys = muat_keys()
        jumlah_key = len(api_keys)
        mood_panel = hitung_mood_otomatis()
        nama_mood_singkat = mood_panel.split('(')[0].strip()

        global_rpm, global_rpd = "0", "0"
        if jumlah_key > 0:
            _, _, _, k_rpm, k_rpd = cek_status_satu_key(api_keys[0])
            if k_rpm != "N/A":
                global_rpm = k_rpm
            if k_rpd != "N/A":
                global_rpd = k_rpd

        anti_edit_status = f"{H}[ ON ]{N}" if ANTI_EDIT_MODE else f"{M}[ OFF ]{N}"

        _auth_dec = base64.b64decode(__auth_enc).decode('utf-8')

        print(f"\n{P}========================================={N}")
        print(f"       CONTROL PANEL - {NAMA_AI}       ")
        print(f"========================================={N}")
        print(f"[*] Jaringan       : {H}ONLINE{N}")
        print(f"[*] Jumlah API Key : {H}{jumlah_key}{N}")
        print(f"[*] Limit Tier RPM : {S}{global_rpm}{N}")
        print(f"[*] Limit Tier RPD : {S}{global_rpd}{N}")
        print(f"[*] Model Aktif    : {K}{model_aktif['nama']}{N}")
        print(f"[*] Persona Aktif  : {B}{persona_aktif['nama']}{N}")
        print(f"[*] Mood Hari Ini  : {S}{nama_mood_singkat}{N}")
        print(f"[*] Copilot Mode   : {H if COPILOT_AKTIF else M}{'AKTIF' if COPILOT_AKTIF else 'NON-AKTIF'}{N}")
        print(f"[*] Auto Update AI : {H if AUTO_UPDATE_MANDIRI else M}{'ON (AKTIF)' if AUTO_UPDATE_MANDIRI else 'OFF (NON-AKTIF)'}{N}")
        print(f"[*] Anti-Edit Core : {anti_edit_status}")
        print(f"[*] {random.choice(RGB_NEON)}{_auth_dec}{N}")
        print(f"{P}-----------------------------------------{N}")
        print(f" [{H}1{N}] Mulai Mengobrol")
        print(f" [{H}2{N}] Ganti / Tambah Persona")
        print(f" [{H}3{N}] Ganti / Tambah Model AI")
        print(f" [{H}4{N}] Cek Cepat Semua Status Key")
        print(f" [{H}5{N}] Kelola Key Interaktif")
        print(f" [{H}6{N}] Cek Limit & Info Model AI")
        print(f" [{H}7{N}] Kelola Dokumen ToS")
        print(f" [{S}8{N}] Fitur Tambahan Termux & Sandbox")
        print(f" [{S}9{N}] KELOLA LIBRARY PYTHON TUX")
        print(f" [{S}10{N}] KELOLA DB & PLUGINS KUSTOM")
        print(f" [{S}11{N}] AUTO-PATCHER / AI SELF-CODER")
        print(f" [{S}12{N}] MENU SETTING COPILOT KUSTOM")
        print(f" [{S}13{N}] TOGGLE AUTO UPDATE AI TO SCRIPT")
        print(f" [{S}14{N}] KELOLA DOMAIN SEARCH ENGINE")
        print(f" [{S}15{N}] CEK KESEHATAN SCRIPT & REPAIR")
        print(f" [{S}16{N}] CONFIG BELAJAR (WHITELIST WEB)")
        print(f" [{S}17{N}] LIHAT & HAPUS {DB_MODUL_BELAJAR}")
        print(f" [{K}18{N}] PANEL MANAGEMENT OFFLINE AI")
        print(f" [{K}19{N}] LIVE AI GRATIS OPENROUTER (TRENDING)")
        print(f" [{K}20{N}] CEK & HAPUS BERKAS LOG AKTIVITAS")
        print(f" [{K}21{N}] BERSIHKAN RAM CACHE AI")
        print(f" [{K}22{N}] TOGGLE COPILOT MODE (ON/OFF)")
        print(f" [{P}23{N}] TOGGLE ANTI-EDIT SCRIPT CODES (ON/OFF)")
        print(f" [{M}X{N}] Keluar Aplikasi")

        _sig_dec = base64.b64decode(__sig_enc).decode('utf-8')
        print(f"\n{S}>> {_sig_dec} <<{N}")
        pilihan_utama = input("Pilih menu: ").strip().lower()

        if pilihan_utama == 'x':
            tulis_log("Aplikasi OneAI Ditutup")
            print(f"\nAplikasi {M}{NAMA_AI}{N} ditutup. Sampai jumpa!")
            sys.exit()
        elif pilihan_utama == "10":
            menu_kelola_db_dan_plugins()
        elif pilihan_utama == "4":
            cek_semua_limit(api_keys)

if __name__ == "__main__":
    jalankan_aplikasi_utama()
