# 🛡️ Loberia Identity Shield
> **"Information is the high ground. We hold it."**

Universal metadata purger and system trace cleaner designed for Windows, Linux, and macOS. Developed by **Loberia Tactical Group** to protect digital identity before file sharing.

## ✨ Key Features
* **Deep Image Sanitization:** Reconstructs images bit-by-bit to remove EXIF, GPS, and steganographic data.
* **Cross-Platform Scrubbing:** Automatically detects OS to target specific temporary directories and DNS caches.
* **Minimalist Footprint:** Zero-bloat Python core optimized for "Lite" environments.
  
## 🚀 Installation & Usage

### 1. Installation
Ensure you have **Python 3.x** installed. Then, install the security dependencies from the root directory:
```bash
pip install -r requirements.txt
```
### 2. Execution
Run the sentinel core using Python:

```bash
Linux/macOS: python3 core/sentinel.py
```
```bash
Windows: python core/sentinel.py
```
Note: You can also install it as a system command using pip install .

---

## 📲 Mobile Protection (Android/Termux)
The suite includes a specialized mobile watchdog located in `/mobile`.

* **Real-time Monitoring:** Scans your Screenshots/DCIM folders every 5 seconds.
* **Automatic Sanitization:** Any new image is instantly stripped of metadata and moved to a secure `/Loberia_Clean` folder.
* **Stealth Mode:** Runs efficiently within the Termux terminal without battery-draining GUIs.

🚀 Field Deployment (Android/Termux)
Now that the code is in the cloud, it's time to activate it on your device. Follow these tactical steps on your phone:

### 1. Open Termux and sync the repository:
```bash
cd identity-shield
git pull origin main
```
### 2. Ensure storage permissions (if not already granted):
```bash
termux-setup-storage
```
### 3. Launch the Mobile Shield:
```bash
python mobile/mobile_shield.py
```

⚖️ Operational Security (OPSEC)
Always run this script before uploading renders, photos, or documents to social media or third-party cloud services. Sanitizing your files is the first step in anti-doxxing defense.

<p align="center">
<b>Classification: Open Source Security Engine | Lead Architect: @XL0b3r14X</b>
