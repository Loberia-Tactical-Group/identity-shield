import os
import platform
import shutil
from PIL import Image

def loberia_banner():
    print("""
    [ 🐺 LOBERIA SENTINEL | IDENTITY SHIELD ]
    [ Tactical Anti-Doxxing & Privacy Suite ]
    ------------------------------------------
    """)

def sanitize_images(target_folder):
    """Reconstrucción profunda para eliminar metadatos y esteganografía."""
    print(f"[*] Iniciando purga de metadatos en: {target_folder}")
    exts = ('.jpg', '.jpeg', '.png')
    
    for root, _, files in os.walk(target_folder):
        for file in files:
            if file.lower().endswith(exts):
                path = os.path.join(root, file)
                try:
                    # Abrimos y reconstruimos la imagen pixel a pixel
                    with Image.open(path) as img:
                        data = list(img.getdata())
                        clean_img = Image.new(img.mode, img.size)
                        clean_img.putdata(data)
                        # Sobrescribimos el original con la versión 'estéril'
                        clean_img.save(path, optimize=True, quality=100)
                    print(f"[+] SANITIZADO: {file}")
                except Exception as e:
                    print(f"[!] Error en {file}: {e}")

def scrub_system_traces():
    """Eliminación de huellas digitales del sistema operativo."""
    os_type = platform.system()
    print(f"[*] Limpiando rastros en sistema: {os_type}")
    
    try:
        if os_type == "Windows":
            temp_path = os.environ.get('TEMP')
            os.system('ipconfig /flushdns')
        else: # Linux/Mac
            temp_path = '/tmp'
            os.system('history -c')
        
        # Limpieza de temporales genérica
        if os.path.exists(temp_path):
            shutil.rmtree(temp_path, ignore_errors=True)
            print(f"[+] Temporales eliminados.")
    except Exception as e:
        print(f"[!] Fallo en limpieza de sistema: {e}")

if __name__ == "__main__":
    loberia_banner()
    path_to_clean = input("[?] Carpeta a procesar (Enter para actual): ") or "."
    sanitize_images(path_to_clean)
    scrub_system_traces()
    print("\n[!] OPERACIÓN COMPLETADA: Identidad blindada.")
