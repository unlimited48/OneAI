import os
import sys
import shutil
import glob
import subprocess
from datetime import datetime

M = "\033[1;31m"
H = "\033[1;32m"
K = "\033[1;33m"
B = "\033[1;34m"
P = "\033[1;35m"
S = "\033[1;36m"
W = "\033[1;37m"
N = "\033[0m"

FILE_UTAMA = "OneAI.py"
FOLDER_BACKUP = "backup_sistem"

def bersihkan_layar():
    os.system('clear')

def verifikasi_sintaks_file(jalur_file):
    if not os.path.exists(jalur_file):
        return False, "File tidak ditemukan"
    try:
        hasil = subprocess.run(
            [sys.executable, "-m", "py_compile", jalur_file],
            capture_output=True,
            text=True
        )
        if hasil.returncode == 0:
            return True, "Sintaks Sehat & Valid"
        else:
            return False, hasil.stderr.strip()
    except Exception as e:
        return False, str(e)

def tampilkan_banner():
    print(f"{M}========================================={N}")
    print(f"        ONEAI HEALING & REPAIR KIT       ")
    print(f"{M}========================================={N}")

def menu_cek_kesehatan():
    bersihkan_layar()
    tampilkan_banner()
    print(f"\n{S}[🔄] Memeriksa kondisi berkas {FILE_UTAMA}...{N}")
    
    if not os.path.exists(FILE_UTAMA):
        print(f"{M}[🚨] STATUS KRITIS: Berkas {FILE_UTAMA} HILANG dari direktori!{N}")
        input("\nTekan ENTER untuk masuk ke menu pemulihan...")
        return
        
    sehat, pesan = verifikasi_sintaks_file(FILE_UTAMA)
    print(f"{W}-----------------------------------------{N}")
    if sehat:
        print(f"🔹 Nama Berkas : {FILE_UTAMA}")
        print(f"🔹 Status Kode : {H}NORMAL / SEHAT{N}")
        print(f"🔹 Diagnosa   : {pesan}")
    else:
        print(f"🔹 Nama Berkas : {FILE_UTAMA}")
        print(f"🔹 Status Kode : {M}RUSAK / CRASH{N}")
        print(f"🔹 Detail Error:\n{K}{pesan}{N}")
    print(f"{W}-----------------------------------------{N}")
    input("\nTekan ENTER untuk kembali...")

def dapatkan_daftar_backup():
    pola = os.path.join(FOLDER_BACKUP, "*OneAI.py")
    berkas_backup = glob.glob(pola)
    berkas_backup.sort(key=os.path.getmtime, reverse=True)
    return berkas_backup

def menu_restore_cadangan():
    while True:
        bersihkan_layar()
        tampilkan_banner()
        print(f"\n{K}[ PANEL RESTORE & ROLLBACK SISTEM ]{N}")
        
        if not os.path.exists(FOLDER_BACKUP):
            print(f"{M}[!] Folder cadangan '{FOLDER_BACKUP}' belum dibuat.{N}")
            input("\nTekan ENTER...")
            break
            
        daftar = dapatkan_daftar_backup()
        if not daftar:
            print(f"{M}[!] Tidak ditemukan file cadangan di dalam folder.{N}")
            print(f"{W}Silakan lakukan backup manual via chatbot terlebih dahulu.{N}")
            input("\nTekan ENTER...")
            break
            
        print(f"{S} NO | KODE CADANGAN (TERBARU -> LAMA)       | WAKTU MODIFIKASI{N}")
        print(f"{W}-----------------------------------------------------------------{N}")
        for idx, jalur in enumerate(daftar, 1):
            nama_file = os.path.basename(jalur)
            waktu_mtime = os.path.getmtime(jalur)
            waktu_str = datetime.fromtimestamp(waktu_mtime).strftime('%Y-%m-%d %H:%M:%S')
            print(f" [{idx}] | {nama_file:<35} | {waktu_str}")
        print(f"{W}-----------------------------------------------------------------{N}")
        print(f" [{M}K{N}] Kembali ke Menu Utama")
        
        pilihan = input("\nPilih nomor file untuk dipulihkan: ").strip().lower()
        if pilihan == 'k':
            break
            
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar):
            target_backup = daftar[int(pilihan) - 1]
            nama_target = os.path.basename(target_backup)
            
            print(f"\nMeneliti integritas data {nama_target}...")
            valid, info_valid = verifikasi_sintaks_file(target_backup)
            
            if not valid:
                print(f"{M}[❌] Gagal! File cadangan ini terdeteksi rusak/cacat sintaks.{N}")
                print(f"Detail cacat: {info_valid}")
                input("\nPemulihan dibatalkan. Tekan ENTER...")
                continue
                
            yakin = input(f"Apakah Tuan yakin ingin menimpa {FILE_UTAMA} dengan versi ini? (y/n): ").strip().lower()
            if yakin == 'y':
                try:
                    if os.path.exists(FILE_UTAMA):
                        os.remove(FILE_UTAMA)
                    shutil.copy(target_backup, FILE_UTAMA)
                    print(f"\n{H}[✔] KESUKSESAN TOTAL! {FILE_UTAMA} berhasil dipulihkan secara utuh.{N}")
                except Exception as e:
                    print(f"\n{M}[❌] Proses tulis gagal: {e}{N}")
                input("\nTekan ENTER...")
                break

def menu_utama_healing():
    while True:
        bersihkan_layar()
        tampilkan_banner()
        print(f" Sesi Aktif: Dokter Penyelamat Berkas Termux")
        print(f"{M}-----------------------------------------{N}")
        print(f" [{H}1{N}] Cek Kesehatan & Integritas Sintaks")
        print(f" [{H}2{N}] Masuk Panel Pemulihan (Restore / Rollback)")
        print(f" [{M}X{N}] Keluar dari Repair Kit")
        
        opsi = input("\nMasukkan opsi tindakan: ").strip().lower()
        if opsi == 'x':
            print(f"\n{H}Sistem Healing ditutup. Semoga OneAI Tuan selalu sehat!{N}")
            break
        elif opsi == '1':
            menu_cek_kesehatan()
        elif opsi == '2':
            menu_restore_cadangan()

if __name__ == '__main__':
    menu_utama_healing()
