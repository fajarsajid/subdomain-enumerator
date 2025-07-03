# 🌐 Subdomain Enumerator

A simple but powerful Python tool that scans and identifies active subdomains for any target domain using a custom wordlist.

## 🔍 What It Does

This script:
- Reads a list of common subdomains from `subdomains.txt`
- Tries to connect to `https://{subdomain}.{target-domain}`
- Prints which ones return a valid response (status code 200)

## 💡 Why It Matters

Subdomain enumeration is a key step in:
- Reconnaissance (ethical hacking, red teaming, bug bounty hunting)
- Attack surface mapping
- Cybersecurity audits

## 🧪 Example Output

```bash
$ python3 subdomain_enum.py --domain github.com

[DEBUG] Loaded 14 subdomains.

🔍 Scanning subdomains for: github.com
--------------------------------------------------
[*] Trying https://www.github.com...
[+] Found: https://www.github.com (200)
...
✅ Scan complete. 9 subdomain(s) found.
``` 
⚙️ Usage
```bash
python3 subdomain_enum.py --domain example.com
python3 subdomain_enum.py --domain example.com --wordlist mylist.txt
```
📁 Files
subdomain_enum.py – Main Python script

subdomains.txt – Default wordlist

requirements.txt – Library dependencies (requests)

📦 Installation
Make sure requests is installed:
```bash

pip install -r requirements.txt
```
👨‍💻 Author
Fajar Sajid
Cybersecurity & Python Enthusiast
GitHub Profile
