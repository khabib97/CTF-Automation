#digital-forensic problem
#cyber talent

from scapy.all import *
import base64

pkts = rdpcap("ARP+Storm.pcap")

flag = ''

for pkt in pkts:
    flag = flag + chr((pkt[ARP].op))

print(flag)

print(base64.b64decode(flag))
