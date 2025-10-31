import ipaddress

def calculate_subnet_info(ip_cidr):
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)
    except ValueError as e:
        print("Error processing IP/CIDR:", e)
        return
    
    netmask = str(network.netmask)
    network_address = str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    num_usable_hosts = network.num_addresses - 2
    
    # Calculate First Usable Host (Network Address + 1)
    if network.num_addresses > 1:
        first_host = str(network.network_address + 1)
    else:
        first_host = "N/A (No usable hosts)"

    # Calculate Last Usable Host (Broadcast Address - 1)
    if network.num_addresses > 1:
        last_host = str(network.broadcast_address - 1)
    else:
        last_host = "N/A (No usable hosts)"

    print("Input IP/CIDR:", ip_cidr)
    print("---------------------------------")
    print("Subnet Mask:", netmask)
    print("Network Address:", network_address)
    print("Broadcast Address:", broadcast_address)
    print("First Usable Host:", first_host)
    print("Last Usable Host:", last_host)
    print("Total Addresses:", network.num_addresses)
    print("Usable Hosts:", num_usable_hosts)

calculate_subnet_info("192.168.1.50/27")

print("\n")

calculate_subnet_info("172.16.10.20/24")

print("\n")

calculate_subnet_info("10.0.0.1/8")