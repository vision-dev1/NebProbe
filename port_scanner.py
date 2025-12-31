import socket
import concurrent.futures
from utils.config import Config
from utils.logger import Logger

class PortScanner:
    def __init__(self, target):
        self.target = target

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(Config.TIMEOUT)
                if s.connect_ex((self.target, port)) == 0:
                    return port
        except:
            return None
        return None

    def scan_ports(self, ports):
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=Config.THREAD_COUNT) as executor:
            future_to_port = {executor.submit(self.scan_port, port): port for port in ports}
            for future in concurrent.futures.as_completed(future_to_port):
                port = future.result()
                if port:
                    open_ports.append(port)
        return sorted(open_ports)
