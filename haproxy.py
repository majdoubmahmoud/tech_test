import subprocess

def install_haproxy():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "haproxy", "-y"])

def configure_haproxy(haproxy_port, server_name, backend_servers):
    #haproxy config file
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

    haproxy_config += "\n"

    with open("/etc/haproxy/haproxy.cfg", "w") as config_file:
        config_file.write(haproxy_config)

    subprocess.run(["sudo", "systemctl", "restart", "haproxy"])

if __name__ == "__main__":
    install_haproxy()

    #interactions
    haproxy_port = input("enter the haproxy port (default is 80): ") or "80"
    server_name = input("enter the server name for haproxy: ")

    backend_servers = []
    num_backends = int(input("enter the number of backend servers: "))
    for i in range(num_backends):
        backend_ip = input(f"enter the IP address of backend server {i+1}: ")
        backend_port = input(f"enter the port for backend server {i+1} (default is {haproxy_port}): ") or haproxy_port
        backend_servers.append((backend_ip, backend_port))

    configure_haproxy(haproxy_port, server_name, backend_servers)

    #firewall configuration
    firewall_enable = input("do you want to enable the firewall? (y/n): ").lower()
    if firewall_enable == "y":
        subprocess.run(["sudo", "ufw", "allow", haproxy_port])
        subprocess.run(["sudo", "ufw", "enable"])
        print(f"Firewall configured to allow traffic on port {haproxy_port}.")
    else:
        print("firewall not enabled")

    print("load balancer setup completed")
