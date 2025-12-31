import argparse
import sys
import json
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.config import Config
from utils.logger import Logger
from utils.network import NetworkUtils
from scanner.port_scanner import PortScanner
from scanner.banner_grabber import BannerGrabber
from scanner.service_detector import ServiceDetector
from scanner.vulnerability_check import VulnerabilityCheck

def print_banner():
    banner = fr"""{Config.C_HEADER}
  _   _      _   _____           _          
 | \ | |    | | |  __ \         | |         
 |  \| | ___| |_| |__) | __ ___ | |__   ___ 
 | . ` |/ _ \ __|  ___/ '__/ _ \| '_ \ / _ \\
 | |\  |  __/ |_| |   | | | (_) | |_) |  __/
 |_| \_|\___|\__|_|   |_|  \___/|_.__/ \___|
                                            
 NetProbe — Network Intelligence Scanner
 Made by Vision | GitHub: https://github.com/vision-dev1
{Config.C_RESET}"""
    Logger.raw(banner)

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="NetProbe - Network Vulnerability Scanner")
    parser.add_argument("target", help="Target IP, Domain, or CIDR")
    parser.add_argument("--ports", help="Ports to scan (e.g., '80,443' or '1-1000')", default=None)
    args = parser.parse_args()

    target_input = args.target

    if not NetworkUtils.validate_target(target_input):
        Logger.error(f"Invalid target: {target_input}")
        sys.exit(1)

    if args.ports:
        if '-' in args.ports:
            start, end = map(int, args.ports.split('-'))
            ports_to_scan = list(range(start, end + 1))
        else:
            ports_to_scan = [int(p) for p in args.ports.split(',')]
    else:
        ports_to_scan = Config.DEFAULT_PORTS

    Logger.info(f"Scanning target: {target_input}")
    
    vuln_checker = VulnerabilityCheck()
    full_report = {
        "scan_time": datetime.now().isoformat(),
        "target_input": target_input,
        "results": []
    }

    for ip in NetworkUtils.resolve_target(target_input):
        Logger.header(f"Results for {ip}")
        
        scanner = PortScanner(ip)
        open_ports = scanner.scan_ports(ports_to_scan)
        
        if not open_ports:
            Logger.warning("No open ports found (in scanned range).")
            continue

        host_result = {"ip": ip, "ports": []}
        
        for port in open_ports:
            banner = BannerGrabber.grab(ip, port)
            
            service, version = ServiceDetector.detect(port, banner)
            
            risk, reason = vuln_checker.assess_risk(port, service, version)
            
            status_color = Config.C_SUCCESS if risk == "Info" else (Config.C_WARNING if risk == "Medium" else Config.C_ERROR)
            Logger.raw(f"  {status_color}[+] Port {port:<5} | Service: {service:<10} | Version: {version:<20} | Risk: {risk} ({reason}){Config.C_RESET}")
            
            host_result["ports"].append({
                "port": port,
                "service": service,
                "version": version,
                "banner": banner,
                "risk": risk,
                "reason": reason
            })
            
        full_report["results"].append(host_result)

    if not os.path.exists(Config.REPORTS_DIR):
        os.makedirs(Config.REPORTS_DIR)
        
    with open(Config.REPORT_FILE, 'w') as f:
        json.dump(full_report, f, indent=4)
        
    Logger.success(f"Scan complete. Report saved to {Config.REPORT_FILE}")

if __name__ == "__main__":
    main()
