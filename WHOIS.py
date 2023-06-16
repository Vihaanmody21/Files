from collections import OrderedDict
import whois

Host = input("Enter Hostname[NO IP]: ")
WHOIS = whois.whois("yahoo.com")
SERVERS = WHOIS.name_servers
for Name in range(len(SERVERS)):
    SERVERS[Name] = SERVERS[Name].lower()
print(f"[+] Domain Name: {WHOIS.domain_name[1]}")
print(f"[+] Domain Creation Date: {str(WHOIS.creation_date[0])}")
print(f"[+] Domain Updated Date: {str(WHOIS.updated_date)}")
print(f"[+] Domain Expiration Date: {str(WHOIS.expiration_date[0])}")
print("[+] Domain Name Servers: ", end = "")
for Server in list(OrderedDict.fromkeys(SERVERS)):
    print(Server + ", ", end = "")
print(f"\n[+] Domain Name System Security Extensions: {WHOIS.dnssec}")
print(f"[+] Organization: {WHOIS.org}")
print(f"[+] Country: {WHOIS.country}")
print(f"[+] Address: {WHOIS.address}")
print(f"[+] Postal Code: {WHOIS.postal_code}")
print(f"[+] State: {WHOIS.state}")
print(f"[+] City: {WHOIS.city}")
print(f"[+] Status: {WHOIS.status}")