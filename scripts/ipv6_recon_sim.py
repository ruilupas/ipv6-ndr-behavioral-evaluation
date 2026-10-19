from scapy.all import IPv6, ICMPv6EchoRequest, send
import sys

def simulate_ipv6_recon(target_ipv6):
    print(f"[*] Injecting IPv6 Non-Exhaustive Reconnaissance Traffic towards {target_ipv6}...")
    icmp_pkt = IPv6(dst=target_ipv6)/ICMPv6EchoRequest()
    send(icmp_pkt, count=20, inter=0.05, verbose=0)
    mcast_pkt = IPv6(dst="ff02::1")/ICMPv6EchoRequest()
    send(mcast_pkt, count=5, inter=0.1, verbose=0)
    print("[+] IPv6 Reconnaissance completed.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "2001:db8::1"
    simulate_ipv6_recon(target)
