#pip install psutil
import psutil
import time
#pip install speedtest-cli
import speedtest
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)#pip install scapy
from scapy.all import *
import threading
# Use Npcap for packet capture
#conf.use_pcap = True
#python C:\anti-virus\check_network.py


def speedtest_networks():
    st = speedtest.Speedtest()
    max_speed = (st.download() + st.upload()) / 1e6
    print("Download Speed:", max_speed) # 1e6 = 1M
    return max_speed


def send_network_brodcust_packet(message):
    udp_brodcust_packet = IP(dst="255.255.255.255") / TCP(sport=8202) / message
    send(udp_brodcust_packet, verbose=False)


def custom_lfilter(packet):
    # Define the custom filter function
    if IP in packet and TCP in packet:
        if packet[IP].dst == "255.255.255.255" and packet[TCP].sport == 8202 and packet.haslayer(Raw):
            return True
    return False
        

def recv_network_brodcust_packet():
    while True:
        packet_sniff = sniff(lfilter=custom_lfilter, count=1, timeout=1)
        if len(packet_sniff) != 0 and packet_sniff[0].load.decode().split(':')[0] == 'NTWK': 
            packet_data = packet_sniff[0].load.decode().split(':')[1].split(',')
            print(f"Network Usage opponent: {packet_data[0]} Mbps ({packet_data[1]}%)")


def check_live_usage_network_my_pc(max_network_data, reset_thread_recv=False):
    # Initialize variables to track previous network stats
    previous_net_stats = psutil.net_io_counters()
    
    t = threading.Thread(target=recv_network_brodcust_packet)
    t.start()
    
    while True:
        # Get the current network statistics
        current_net_stats = psutil.net_io_counters()
        
        # Calculate the difference in network data since the last measurement
        bytes_sent_diff = current_net_stats.bytes_sent - previous_net_stats.bytes_sent
        bytes_recv_diff = current_net_stats.bytes_recv - previous_net_stats.bytes_recv
        
        # Calculate the network usage as a percentage
        total_bytes_diff = bytes_sent_diff + bytes_recv_diff
        network_usage = int(round((total_bytes_diff / 1e6) * 8, 2))  # Convert to Mbps, 1e6 == 1M
        precent_usage = int(round(network_usage / max_network_data * 100 , 0))
        
        print(f"Network Usage: {network_usage} Mbps ({precent_usage}%)")
        
        #send and recv data
        send_network_brodcust_packet(f"NTWK:{network_usage},{precent_usage}")
        if reset_thread_recv:
            t.join()
            t = threading.Thread(target=recv_network_brodcust_packet)
            t.start()
            reset_thread_recv = False

        
        # Update the previous network stats for the next measurement
        previous_net_stats = current_net_stats
        
        time.sleep(1)
    
    t.join()


def fix_network_problems():
    pass


if __name__ == '__main__':
    #max_network_data = speedtest_networks()
    check_live_usage_network_my_pc(500)