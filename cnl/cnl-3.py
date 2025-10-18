import ipaddress
import sys

def calculate_subnet_details(ip_with_cidr):
    
    try:
        network = ipaddress.ip_network(ip_with_cidr, strict=False)


        print(f"--- Subnetting Calculation for {ip_with_cidr} ---")
        print(f"1️⃣ Input IP/CIDR: {ip_with_cidr}")
        print(f"2️⃣ Subnet Mask:   {network.netmask}")
        print(f"3️⃣ CIDR Prefix:   /{network.prefixlen}")
        print("---------------------------------------------")
        print(f"➡️ Network Address (Subnet ID): {network.network_address}")
        print(f"➡️ Broadcast Address:           {network.broadcast_address}")
        print(f"➡️ Total Host Addresses:        {network.num_addresses}")
        print(f"➡️ Usable Host Range:           {network.hosts()[0]} - {network.hosts()[-1]}")
        print(f"➡️ Maximum Usable Hosts:        {network.num_addresses - 2}")
        print("---------------------------------------------")

    except ValueError as e:
        print(f"\n❌ Error: Invalid IP address or CIDR notation.")
        print(f"   Details: {e}")
        print("   Please use a format like '192.168.1.50/26'.")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    
    print("### Subnetting Demonstration ###\n")

    print("Example 1: Standard Class C (No Subnetting)")
    calculate_subnet_details("192.168.10.1/24")
    print("\n" + "="*50 + "\n")

    print("Example 2: Subnetting with a /26 prefix")
    print("The /26 prefix requires 2 host bits to be borrowed for the subnet ID (24 -> 26).")
    calculate_subnet_details("192.168.10.75/26") 
    print("\n" + "="*50 + "\n")

    print("Example 3: Subnetting a different host in the /26 subnet")
    calculate_subnet_details("192.168.10.150/26")
    print("\n" + "="*50 + "\n")

    print("Example 4: Class B with /30 (Point-to-Point Link)")
    calculate_subnet_details("172.16.5.1/30") 
    print("\n" + "="*50 + "\n")
    
    if len(sys.argv) > 1:
        print("### Interactive Input ###")
        user_input = sys.argv[1]
    else:
        print("### Interactive Mode ###")
        user_input = input("Enter IP address in CIDR format (e.g., 10.0.0.1/28): ")

    calculate_subnet_details(user_input)
    print("\n\n*Note: The program uses the ipaddress module for precise calculations.*")