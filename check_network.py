#pip install psutil
import psutil
import time
#pip install speedtest-cli
import speedtest

def speedtest_networks():
    st = speedtest.Speedtest()
    max_speed = (st.download() + st.upload()) / 1e6
    print("Download Speed:", max_speed) # 1e6 = 1M
    return max_speed

def check_live_usage_network_my_pc(max_network_data):
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
        
        print(f"Network Usage: {int(round(network_usage, 0))} Mbps ({int((round(network_usage / max_network_data * 100 , 0)))}%)")
        
        # Update the previous network stats for the next measurement
        previous_net_stats = current_net_stats
        
        time.sleep(1)


def fix_network_problems():
    pass

if __name__ == '__main__':
    max_network_data = speedtest_networks()
    check_live_usage_network_my_pc(max_network_data)