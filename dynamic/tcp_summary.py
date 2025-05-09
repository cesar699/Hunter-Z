
from scapy.all import rdpcap

def summarize_pcap(pcap_path):
    return {"dst":[],"points":[0]*60}
