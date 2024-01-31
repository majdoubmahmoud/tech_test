import subprocess

def install_haproxy():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "haproxy", "-y"])

def configure_haproxy(haproxy_port, server_name, backend_servers):
    # Customize your HAProxy configuration here if needed
    haproxy_config = f"""
    global
        daemon
        maxconn 256

    defaults
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms

    frontend http-in
        bind *:{haproxy_port}
        default_backend servers

    backend servers
    """
    
    for i, (backend_ip, backend_port) in enumerate(backend_servers, start=1):
        haproxy_config += f"        server server{i} {backend_ip}:{backend_port} check\n"

    # Add a newline character at the end of the configuration
    haproxy_config += "\n"

    with open("/etc/haproxy/haproxy.cfg", "w") as config_file:
        config_file.write(haproxy_config)

    subprocess.run(["sudo", "systemctl", "restart", "haproxy"])

if __name__ == "__main__":
    install_haproxy()

    # Get user input for HAProxy port, server name, and backend servers
    haproxy_port = input("Enter the HAProxy port (default is 80): ") or "80"
    server_name = input("Enter the server name for HAProxy (e.g., example.com): ")

    backend_servers = []
    num_backends = int(input("Enter the number of backend servers: "))
    for i in range(num_backends):
        backend_ip = input(f"Enter the IP address of backend server {i+1}: ")
        backend_port = input(f"Enter the port for backend server {i+1} (default is {haproxy_port}): ") or haproxy_port
        backend_servers.append((backend_ip, backend_port))

    configure_haproxy(haproxy_port, server_name, backend_servers)

    # Get user input for firewall configuration
    firewall_enable = input("Do you want to enable the firewall? (y/n): ").lower()
    if firewall_enable == "y":
        subprocess.run(["sudo", "ufw", "allow", haproxy_port])
        subprocess.run(["sudo", "ufw", "enable"])
        print(f"Firewall configured to allow traffic on port {haproxy_port}.")
    else:
        print("Firewall not enabled.")

    print("Load balancer setup completed.")
