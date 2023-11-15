import socket
import ipaddress

def get_local_network_range():
    try:
        # Get the local hostname
        hostname = socket.gethostname()

        # Get the local IP address
        local_ip = socket.gethostbyname(hostname)

        # Get the network address and netmask
        network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)

        return network
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    local_network = get_local_network_range()

    if local_network:
        print(f"Local IP address: {local_network.network_address}")
        print(f"Network range: {local_network}")
    else:
        print("Unable to determine the local network range.")
