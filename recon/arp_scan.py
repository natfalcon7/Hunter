from scapy.all import ARP, Ether, srp
import sys 


# Get the CIDR range, build the ARP packet, send it, and return the raw responses from Scapy.

def scan(ip_range):
	ether = Ether(dst="ff:ff:ff:ff:ff:ff")
	arp = ARP(pdst=ip_range)
	packet = ether / arp
	answered, unanswered = srp(packet, timeout=2, verbose=False)
	return answered 

# Get those responses, extract the IP and MAC addresses from each one, and return a list of dictionaries.

def parse_results(answered):
	clients = []

	for sent, received in answered:
		client_info = {
		    "ip": received.psrc,
		    "mac": received.hwsrc
		}
		clients.append(client_info)

	return clients	


# Get that list and print it formatted on the screen.

def display_results(hosts):
	print("IP               MAC")
	print("----------------------------------------")
	for host in hosts:
		print(f"{host['ip']:<16} {host['mac']}")

def main():
	ip_range = sys.argv[1]

	answered = scan(ip_range)
	hosts = parse_results(answered)
	display_results(hosts)

if __name__ == "__main__":
	main()
