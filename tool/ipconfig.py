import netifaces


def get_ip() -> str:
    """获取当前网络接口的IP地址"""
    return netifaces.gateways()['default'][netifaces.AF_INET][0]
