import socket
import sys

def scan_ports(ip, ports):
	open_ports = []

	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)

		result = sock.connect_ex((ip, port))

		if result == 0:
			open_ports.append(port)

		sock.close()
		
	return open_ports

def display_results(ip, open_ports):
	print(f"\nOpen ports for {ip}")
	print("----------------------------")

	if open_ports:
		for port in open_ports:
			print(f"Port {port}: OPEN")
	else:
		print("No open ports found.")
			

def main():
	ip = sys.argv[1]

	common_ports = [8022, 88, 443, 8080, 21, 23, 3306]

	open_ports = scan_ports(ip, common_ports)
	display_results(ip, open_ports)

if __name__ == "__main__":
	main()
