
def dot_to_long_ip(ip_address):
    if ip_address:
        _ips = str(ip_address).split(".")
        return int(_ips[3]) + int(_ips[2]) * 256 + int(_ips[1]) * 256 * 256 + int(_ips[0]) * 256 * 256 * 256
    return 0
