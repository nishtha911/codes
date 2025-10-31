import socket

def dns_lookup():
    address = input("Enter a URL (e.g., google.com) or an IP address (e.g., 8.8.8.8): ").strip()
    
    if not address:
        print("Error: Input cannot be empty.")
        return

    if all(part.isdigit() for part in address.split('.')) and address.count('.') == 3:
        print(f"\nAttempting Reverse Lookup for IP: {address}...")
        try:
            hostname, aliases, ips = socket.gethostbyaddr(address)
            
            print(f"URL/Hostname: {hostname}")
            if aliases:
                print(f"Aliases: {', '.join(aliases)}")
            if ips:
                print(f"IP Address (Verified): {ips[0]}")
                
        except socket.herror as e:
            print(f"Error during Reverse Lookup: No URL found for this IP or lookup failed ({e})")
        except socket.error as e:
            print(f"Error: {e}")

    else:
        print(f"\nAttempting Forward Lookup for URL: {address}...")
        try:
            ip_address = socket.gethostbyname(address)
            hostname, aliases, ips = socket.gethostbyname_ex(address)
            
            print(f"IP Address: {ip_address}")
            print(f"Canonical Name: {hostname}")
            if aliases:
                print(f"Aliases: {', '.join(aliases)}")
            if len(ips) > 1:
                print(f"Additional IPs: {', '.join(ips[1:])}")
            
        except socket.gaierror as e:
            print(f"Error during Forward Lookup: Cannot resolve URL or network error ({e})")
        except socket.error as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    dns_lookup()