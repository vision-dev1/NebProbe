import socket
from utils.config import Config

class BannerGrabber:
    @staticmethod
    def grab(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(Config.TIMEOUT)
                s.connect((ip, port))
                
                if port in [80, 8080]:
                    s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                
                try:
                    banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                    return banner
                except socket.timeout:
                    return None
        except:
            return None
