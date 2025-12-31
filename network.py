import ipaddress
import socket
import sys

class NetworkUtils:
    @staticmethod
    def validate_target(target):
        try:
            ipaddress.ip_address(target)
            return 'ip'
        except ValueError:
            try:
                ipaddress.ip_network(target, strict=False)
                return 'cidr'
            except ValueError:
                if NetworkUtils.is_valid_domain(target):
                    return 'domain'
                return None

    @staticmethod
    def is_valid_domain(domain):
        if len(domain) > 255: return False
        if domain[-1] == ".": domain = domain[:-1]
        allowed = lambda c: c.isalnum() or c == "-" or c == "_"
        return all(allowed(c) for part in domain.split(".") for c in part)

    @staticmethod
    def resolve_target(target):
        type_ = NetworkUtils.validate_target(target)
        
        if type_ == 'ip':
            yield target
        
        elif type_ == 'cidr':
            for ip in ipaddress.ip_network(target, strict=False).hosts():
                yield str(ip)
        
        elif type_ == 'domain':
            try:
                ip_addr = socket.gethostbyname(target)
                yield ip_addr
            except socket.gaierror:
                pass
        
        else:
            return
