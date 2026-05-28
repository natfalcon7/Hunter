# Hunter

Modular Python tool for network reconnaissance and attack simulation.

## ⚠️ Legal Disclaimer

This tool is developed strictly for educational purposes and authorized 
security testing in controlled lab environments. 
Unauthorized use against networks or systems you do not own or have 
explicit permission to test is illegal and unethical.

The author assumes no responsibility for misuse of this tool.
Use responsibly and in accordance with applicable laws.

## Description

Hunter is a modular Python tool designed to simulate a full attack chain:

1. **Recon** — ARP-based host discovery on local network
2. **Fingerprinting** — Port scanning and service detection  
3. **Attack** — SSH brute force against discovered targets
4. **Report** — JSON/CSV output of findings

## Requirements

```bash
pip install scapy paramiko
```

## Usage

```bash
# Run full attack chain
sudo python3 hunter.py <network> <wordlist>

# Example
sudo python3 hunter.py 192.168.0.0/24 attack/wordlist.txt

# Run individual modules
sudo python3 recon/arp_scan.py 192.168.0.0/24
python3 recon/port_scan.py <ip>
python3 attack/ssh_brute.py <ip> <port> <username> <wordlist>
```

## Project Structure

hunter/
├── recon/
│   ├── arp_scan.py       # Phase 1: ARP-based host discovery
│   └── port_scan.py      # Phase 2: TCP port scanner
├── attack/
│   └── ssh_brute.py      # Phase 3: SSH brute force
├── reports/
│   └── report.py         # Phase 4: JSON/CSV reporting
├── hunter.py             # Orchestrator: runs all phases
└── README.md

## Known Limitations

- ARP scan requires root privileges (sudo)
- SSH brute force requires delay between attempts on slow targets
- Tested on controlled home lab environment only

## Target Environment

Controlled home lab. Primary target: Android device running Termux + OpenSSH.

## Author

natfalcon7 — [github.com/natfalcon7](https://github.com/natfalcon7)