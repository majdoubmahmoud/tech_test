import subprocess

# Get the health check URL and web app path from user input
health_check_url = input("Enter the health check URL: ")
web_app_path = input("Enter the path to the web app: ")

# Timeout for the HTTP request in seconds
timeout_seconds = 5

def perform_health_check():
    try:
        # Build the curl command
        curl_command = [
            "curl",
            "--output", "/dev/null",
            "--silent",
            "--head",
            "--fail",
            "--max-time", str(timeout_seconds),
            health_check_url
        ]

        # Run the curl command using subprocess
        subprocess.run(curl_command, check=True)
        return True  # Health check succeeded

    except subprocess.CalledProcessError:
        return False  # Health check failed

def restart_nginx():
    print("Restarting Nginx...")
    subprocess.run(["sudo", "service", "nginx", "restart"])

def redeploy_web_app(web_app_path):
    # Replace the following command with the actual command to redeploy your web app
    print(f"Redeploying web app at {web_app_path}...")
    subprocess.run(["your_redeployment_command", web_app_path])

# Perform the health check and redeploy web app if needed
if not perform_health_check():
    redeploy_web_app(web_app_path)
    restart_nginx()
else:
    print("Health check succeeded. No need to redeploy or restart Nginx.")
