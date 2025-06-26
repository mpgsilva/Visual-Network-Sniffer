from scapy.all import sniff, IP # type: ignore  //ignora alerta do VS code
from collections import defaultdict
import threading

# dicionário global que conta pacotes por protocolo
protocol_counts = defaultdict(int)

def process_packet(pkt):
    if IP in pkt:
        proto = pkt[IP].proto
        if proto == 6:
            protocol_counts['TCP'] += 1
        elif proto == 17:
            protocol_counts['UDP'] += 1
        elif proto == 1:
            protocol_counts['ICMP'] += 1
        
def start_sniffing():
    sniff(prn=process_packet, store=False)