import sys
from datetime import datetime
from .config import Config

class Logger:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def info(msg):
        print(f"{Config.C_INFO}[*] {Logger._timestamp()} - {msg}")

    @staticmethod
    def success(msg):
        print(f"{Config.C_SUCCESS}[+] {Logger._timestamp()} - {msg}")

    @staticmethod
    def warning(msg):
        print(f"{Config.C_WARNING}[!] {Logger._timestamp()} - {msg}")

    @staticmethod
    def error(msg):
        print(f"{Config.C_ERROR}[-] {Logger._timestamp()} - {msg}")

    @staticmethod
    def header(msg):
        print(f"\n{Config.C_HEADER}{Config.C_BOLD}{msg}\n{'=' * len(msg)}")
    
    @staticmethod
    def raw(msg):
        print(msg)
