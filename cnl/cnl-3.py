import math

def subnetting(ip, subnets):
    ip_parts = ip.split('.')
    ip_class = ''
    default_mask = ''

    first_octet = int(ip_parts[0])
    if 1 <= first_octet <= 126:
        ip_class = 'A'
        default_mask = 8
    elif 128 <= first_octet <= 191:
        ip_class = 'B'
        default_mask = 16
    elif 192 <= first_octet <= 223:
        ip_class = 'C'
        default_mask = 24
    else:
        ip_class = 'Invalid'

    if ip_class == 'Invalid':
        print("Invalid IP Address")
        return

    print(f"\nIP Address: {ip}")
    print(f"Class: {ip_class}")
    print(f"Default Mask: /{default_mask}")

    bits_needed = math.ceil(math.log2(subnets))
    new_mask = default_mask + bits_needed
    total_subnets = 2 ** bits_needed
    hosts_per_subnet = (2 ** (32 - new_mask)) - 2

    mask_bin = ('1' * new_mask).ljust(32, '0')
    mask = [str(int(mask_bin[i:i+8], 2)) for i in range(0, 32, 8)]
    subnet_mask = '.'.join(mask)

    print(f"\nNumber of Subnets: {total_subnets}")
    print(f"New Subnet Mask: /{new_mask}  ({subnet_mask})")
    print(f"Hosts per Subnet: {hosts_per_subnet}")

ip = input("Enter IP Address (e.g. 192.168.1.0): ")
subnets = int(input("Enter number of required subnets: "))
subnetting(ip, subnets)
