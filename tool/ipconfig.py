import netifaces


def get_ip() -> str:
    return netifaces.gateways()['default'][netifaces.AF_INET][0]
