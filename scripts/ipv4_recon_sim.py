from scapy.all import IP, TCP, send
import sys

def simulate_ipv4_recon(target_ip):
    print(f"[*] Injecting IPv4 SYN Reconnaissance Traffic towards {target_ip}...")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389, 8080]
    for port in common_ports:
        pkt = IP(dst=target_ip)/TCP(dport=port, flags="S")
        send(pkt, count=5, inter=0.02, verbose=0)
    print("[+] IPv4 Reconnaissance completed.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.100"
    simulate_ipv4_recon(target)
