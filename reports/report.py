import json
import csv
import os


# Save data to a JSON file.
def save_json(data, filename):
    """
    Save Python data structure into a JSON file.
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"[+] Data saved to {filename}")

    except Exception as e:
        print(f"[-] JSON save error: {e}")


# Save data to a CSV file.
def save_csv(data, filename):
    """
    Save a list of dictionaries into a CSV file.
    Each dict must have the same keys.
    """
    try:
        if not data:
            print("[-] No data to save.")
            return

        keys = data[0].keys()

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=keys)

            writer.writeheader()
            writer.writerows(data)

        print(f"[+] Data saved to {filename}")

    except Exception as e:
        print(f"[-] CSV save error: {e}")




def main():
    # Hardcoded report data (future: will come from scanners)
    report = {
        "target": "192.168.0.179",
        "open_ports": [8022],
        "credentials_username": "nano666",
        "credentials_password": "hunter123"
    }

    # Ensure output directory exists
    os.makedirs("reports", exist_ok=True)

    # Save JSON (full structure preserved)
    save_json(report, "reports/report.json")

    # Save CSV (flat structure required)
    save_csv([report], "reports/report.csv")


if __name__ == "__main__":
    main()        