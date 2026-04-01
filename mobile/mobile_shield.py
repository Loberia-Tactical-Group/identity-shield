import os
import time
from PIL import Image

# Configuración para Android/Termux
SOURCE_DIR = "/sdcard/DCIM/Screenshots"
CLEAN_DIR = "/sdcard/Loberia_Clean"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def sanitize_mobile(file_path, filename):
    try:
        with Image.open(file_path) as img:
            # Destrucción de metadatos mediante reconstrucción
            data = list(img.getdata())
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(data)
            
            # Ofuscación táctica del nombre (LB + timestamp)
            new_name = f"LB_SHIELD_{int(time.time())}.png"
            clean_img.save(os.path.join(CLEAN_DIR, new_name), optimize=True)
            print(f"[+] PROTEGIDO: {new_name}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    print("🐺 LOBERIA MOBILE SHIELD | Status: Active")
    ensure_dir(CLEAN_DIR)
    
    if not os.path.exists("/sdcard"):
        print("[!] ERROR: Ejecuta 'termux-setup-storage' en la terminal.")
    else:
        print(f"[*] Vigilando capturas en: {SOURCE_DIR}")
        known = set(os.listdir(SOURCE_DIR))
        try:
            while True:
                current = set(os.listdir(SOURCE_DIR))
                for f in (current - known):
                    if f.lower().endswith(('.jpg', '.png', '.jpeg')):
                        sanitize_mobile(os.path.join(SOURCE_DIR, f), f)
                known = current
                time.sleep(5)
        except KeyboardInterrupt:
            print("\n[!] Shield Standby.")
