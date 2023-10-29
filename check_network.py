#pip install psutil
import psutil
import time

# Initialize variables to track previous network stats
previous_net_stats = psutil.net_io_counters()

while True:
    # Get the current network statistics
    current_net_stats = psutil.net_io_counters()
    
    # Calculate the difference in network data since the last measurement
    bytes_sent_diff = current_net_stats.bytes_sent - previous_net_stats.bytes_sent
    bytes_recv_diff = current_net_stats.bytes_recv - previous_net_stats.bytes_recv
    
    # Calculate the network usage as a percentage
    total_bytes_diff = bytes_sent_diff + bytes_recv_diff
    network_usage = (total_bytes_diff / 1e6) * 8  # Convert to Mbps, 1e6 == 1M
    
    print(f"Network Usage: {round(network_usage, 2)} Mbps ({(round(network_usage / 10 , 2))}%)")
    
    # Update the previous network stats for the next measurement
    previous_net_stats = current_net_stats
    
    time.sleep(1)