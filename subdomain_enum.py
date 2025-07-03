import requests
import argparse

def check_subdomains(domain, wordlist):
    print(f"\n🔍 Scanning subdomains for: {domain}")
    print("-" * 50)
    found = 0

    for sub in wordlist:
        url = f"https://{sub}.{domain}"
        print(f"[*] Trying {url}...")  
        try:
            response = requests.get(url, timeout=3)
            print(f"[+] Found: {url} ({response.status_code})")
            found += 1
        except requests.RequestException:
            pass  # Ignore subdomains that don’t resolve

    print(f"\n✅ Scan complete. {found} subdomain(s) found.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Enumerator")
    parser.add_argument("--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("--wordlist", default="subdomains.txt", help="Path to subdomain wordlist")

    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        words = [line.strip() for line in f if line.strip()]
    
    check_subdomains(args.domain, words)
