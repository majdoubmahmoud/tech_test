import subprocess

def install_nginx():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "nginx", "-y"])

def configure_nginx(port, server_name):
    # Customize your Nginx configuration here if needed
    nginx_config = f"""
    server {{
        listen {port};
        server_name {server_name};

        location / {{
            root /var/www/html;
            index index.nginx-debian.html;
        }}

        # Additional security measures (you can customize this)
        # Add firewall rule to allow traffic on specified port
        # Uncomment the following line to enable the firewall rule
        # sudo ufw allow {port}/tcp

        # Enable SSL (uncomment if needed)
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

    # Get user input for port and server name
    port = input("Enter the port for Nginx (default is 80): ") or "80"
    server_name = input("Enter the server name for Nginx (e.g., example.com): ")

    configure_nginx(port, server_name)

    # Set up basic firewall using ufw
    firewall_enable = input("Do you want to enable the firewall? (y/n): ").lower()
    if firewall_enable == "y":
        subprocess.run(["sudo", "ufw", "allow", port])
        subprocess.run(["sudo", "ufw", "enable"])
        print(f"Firewall configured to allow traffic on port {port}.")
    else:
        print("Firewall not enabled.")

    print("Web server setup completed.")
