def get_class(ip_first_octet):
    ip_first_octet = int(ip_first_octet)
    if 1 <= ip_first_octet <= 126:
        return 'A', 8, "255.0.0.0"
    elif 128 <= ip_first_octet <= 191:
        return 'B', 16, "255.255.0.0"
    elif 192 <= ip_first_octet <= 223:
        return 'C', 24, "255.255.255.0"
    else:
        return 'Unknown', 0, "N/A"


def calculate_subnet_details(default_mask_bits, subnet_bits):
    total_subnets = 2 ** subnet_bits
    host_bits = 32 - (default_mask_bits + subnet_bits)
    hosts_per_subnet = (2 ** host_bits) - 2 if host_bits > 0 else 0
    return total_subnets, hosts_per_subnet


def main():
    ip_address = input("Enter the IP Address (e.g., 192.168.1.0): ")
    subnet_bits = int(input("Enter the number of subnet bits: "))

    first_octet = ip_address.split(".")[0]
    ip_class, default_mask_bits, default_mask = get_class(first_octet)

    if ip_class == 'Unknown':
        print("This IP address class is not supported for subnetting.")
        return

    total_subnets, hosts_per_subnet = calculate_subnet_details(default_mask_bits, subnet_bits)

    print(f"\nIP Address: {ip_address}")
    print(f"Class: {ip_class}")
    print(f"Default Subnet Mask: {default_mask}")
    print(f"Total Subnets: {total_subnets}")
    print(f"Hosts per Subnet: {hosts_per_subnet}")


if __name__ == "__main__":
    main()
