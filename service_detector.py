import re

class ServiceDetector:
    COMMON_PORTS = {
        21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns",
        80: "http", 110: "pop3", 135: "msrpc", 139: "netbios-ssn",
        143: "imap", 443: "https", 445: "microsoft-ds", 3306: "mysql",
        3389: "rdp", 5432: "postgresql", 5900: "vnc", 6379: "redis",
        8080: "http-proxy", 27017: "mongodb"
    }

    @staticmethod
    def detect(port, banner):
        service = ServiceDetector.COMMON_PORTS.get(port, "unknown")
        version = "unknown"

        if banner:
            lower_banner = banner.lower()
            
            if "ssh" in lower_banner:
                service = "ssh"
                version = banner.split(" ")[0] if " " in banner else banner
            elif "ftp" in lower_banner:
                service = "ftp"
                v_match = re.search(r'vsftpd\s+([\d\.]+)', lower_banner, re.IGNORECASE)
                if v_match: version = f"vsftpd {v_match.group(1)}"
            elif "http" in lower_banner:
                service = "http"
                s_match = re.search(r'server:\s*(.*)', lower_banner, re.IGNORECASE)
                if s_match: version = s_match.group(1)
            elif "mysql" in lower_banner:
                service = "mysql"
            elif "redis" in lower_banner:
                service = "redis"
                v_match = re.search(r'redis_version:([\d\.]+)', lower_banner)
                if v_match: version = v_match.group(1)
            
            if version == "unknown" and len(banner) < 50:
                version = banner

        return service, version
