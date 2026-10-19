import os
import time
import sys

def simulate_ipv6_address_churn(interface="eth0", iterations=10):
    print(f"[*] Simulating IPv6 SLAAC/Privacy Extension Address Churn on {interface}...")
    for i in range(iterations):
        temp_ip = f"2001:db8:1::{i+100:x}"
        os.system(f"ip -6 addr add {temp_ip}/64 dev {interface} 2>/dev/null")
        time.sleep(2)
        os.system(f"ip -6 addr del {temp_ip}/64 dev {interface} 2>/dev/null")
    print("[+] Address Churn simulation finished.")

if __name__ == "__main__":
    iface = sys.argv[1] if len(sys.argv) > 1 else "eth0"
    simulate_ipv6_address_churn(interface=iface)
