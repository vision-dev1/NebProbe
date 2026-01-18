# NetProbe — Network Intelligence Scanner

<div align="center">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python">
    <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux">
    <img src="https://img.shields.io/badge/Wi--Fi-High_Speed-blue?style=for-the-badge&logo=wi-fi&logoColor=white" alt="WiFi">
</div>

NetProbe is a professional-grade network scanner designed for defensive security and learning. It rapidly scans targets, detects running services, identifies versions, and flags potential security risks based on configuration and outdated software.

> **Disclaimer**: This tool is for **educational and defensive purposes only**. Do not use against targets you do not have permission to audit. The author is not responsible for any misuse.

## Features

- **Fast & Modular**: Threaded TCP scanning for speed.
- **Service Detection**: Identifies services (SSH, FTP, HTTP, Databases, etc.) and versions via banner grabbing and heuristics.
- **Risk Analysis**: Automatically matches detected services against a database of known risky configurations and vulnerable versions (e.g., Telnet, old vsftpd).
- **Target Handling**: Supports single IPs, domains, and CIDR ranges.
- **Reporting**: JSON report generation for easy integration.

## Installation

NetProbe requires **Python 3.8+**.

1. Clone the repository:
   ```bash
   git clone https://github.com/vision-dev1/NetProbe.git
   cd netprobe
   ```

2. Set up a Virtual Environment (Recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r netprobe/requirements.txt
   ```
   *Note: NetProbe uses standard libraries mostly but having `requests` is recommended for future modules.*

## How to Run

### Quick Start (Linux/Mac)
Run the helper script from the root directory:
```bash
chmod +x run.sh
./run.sh <target>
```
Example: `./run.sh 127.0.0.1`

### Standard Usage

You can run NetProbe directly using Python:

**Option 1: Direct Script**
```bash
python3 main.py 192.168.1.1
```

**Option 2: As a Module**
```bash
python3 -m main 192.168.1.1
```

### Command Examples
```bash
# Scan a single IP
python3 main.py 192.168.1.1

# Scan a domain
python3 main.py example.com

# Scan a CIDR range
python3 main.py 192.168.1.0/24

# Scan specific ports
python3 main.py 127.0.0.1 --ports 80,443,8080
python3 main.py 127.0.0.1 --ports 1-1000
```

## Project Structure

- `scanner/`: Core modules for port scanning and detection.
- `utils/`: Networking, logging, and configuration helpers.
- `data/`: `risky_services.json` database.
- `reports/`: JSON output of scan results.

---
**Made by Vision**
[GitHub](https://github.com/vision-dev1)
[Portfolio](https://visionkc.com.np)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
