import os
from colorama import Fore, Style, init

init(autoreset=True)

class Config:
    DEFAULT_PORTS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 5900, 6379, 8080, 27017]
    TIMEOUT = 2.0
    THREAD_COUNT = 100
    
    C_HEADER = Fore.CYAN
    C_INFO = Fore.BLUE
    C_SUCCESS = Fore.GREEN
    C_WARNING = Fore.YELLOW
    C_ERROR = Fore.RED
    C_RESET = Style.RESET_ALL
    C_BOLD = Style.BRIGHT
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
    RISKY_SERVICES_FILE = os.path.join(DATA_DIR, 'risky_services.json')
    REPORT_FILE = os.path.join(REPORTS_DIR, 'scan_report.json')

    LOGO_PATH = os.path.join(BASE_DIR, 'assets', 'netprobe_logo.png')
