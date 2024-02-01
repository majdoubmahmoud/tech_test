import subprocess

def install_nginx():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "nginx", "-y"])

def configure_nginx(port, server_name):
    #nginx config file
    nginx_config = f"""
    server {{
        listen {port};
        server_name {server_name};

        location / {{
            root /var/www/html;
            index index.nginx-debian.html;
        }}

        # enable SSL (uncomment if needed):
        # listen 443 ssl;
        # ssl_certificate /etc/nginx/ssl/{server_name}.crt;
        # ssl_certificate_key /etc/nginx/ssl/{server_name}.key;
    }}
    """
    with open("/etc/nginx/sites-available/default", "w") as config_file:
        config_file.write(nginx_config)

    subprocess.run(["sudo", "systemctl", "restart", "nginx"])

if __name__ == "__main__":
    install_nginx()

    #interractions
    port = input("enter the port for nginx (default is 80): ") or "80"
    server_name = input("enter the server name for nginx: ")

    configure_nginx(port, server_name)

    #firewall setup
    firewall_enable = input("do you want to enable the firewall? (y/n): ").lower()
    if firewall_enable == "y":
        subprocess.run(["sudo", "ufw", "allow", port])
        subprocess.run(["sudo", "ufw", "enable"])
        print(f"firewall configured to allow traffic on port {port}")
    else:
        print("firewall not enabled")

    print("web server setup completed")
