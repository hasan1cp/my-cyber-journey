#!/usr/bin/env python3

import whois

def main():
    domain = input("Enter a domain name (e.g., example.com): ")
    try:
        w = whois.whois(domain)
        print("\n--- WHOIS Information ---")
        print(f"Domain Name: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
        print(f"Emails: {w.emails}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
