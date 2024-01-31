import subprocess

def install_packages():
    subprocess.run(['sudo', 'apt-get', 'install', 'git', 'awscli'])

def clone_git_repo():
    git_repo_url = input("Enter Git repository URL: ")
    subprocess.run(['git', 'clone', git_repo_url])
    print("Web application code cloned successfully.")

def configure_aws_cli():
    aws_access_key = input("Enter AWS access key: ")
    aws_secret_key = input("Enter AWS secret key: ")
    aws_region = input("Enter AWS region (e.g., us-west-2): ")
    output_format = input("Enter desired output format (e.g., json): ").lower()

    subprocess.run(['aws', 'configure', 'set', 'aws_access_key_id', aws_access_key])
    subprocess.run(['aws', 'configure', 'set', 'aws_secret_access_key', aws_secret_key])
    subprocess.run(['aws', 'configure', 'set', 'region', aws_region])
    subprocess.run(['aws', 'configure', 'set', 'output', output_format])
    print("AWS CLI configured successfully.")

def pull_data_from_s3():
    s3_bucket = input("Enter S3 bucket name: ")
    local_data_path = input("Enter local path to store S3 data (default: /path/to/local/data): ") or '/path/to/local/data'
    
    subprocess.run(['aws', 's3', 'sync', f's3://{s3_bucket}', local_data_path])
    print("Data pulled from S3 successfully.")

def configure_firewall():
    firewall_enabled = input("Enable firewall? (y/n): ").lower() == 'y'

    if firewall_enabled:
        subprocess.run(['sudo', 'ufw', 'allow', '22'])  # Git SSH port
        subprocess.run(['sudo', 'ufw', 'allow', '443'])  # AWS CLI HTTPS port
        subprocess.run(['sudo', 'ufw', 'enable'])
        print("Firewall configured and enabled.")
    else:
        print("Firewall not configured.")

def main():
    install_packages()
    clone_git_repo()
    configure_aws_cli()
    pull_data_from_s3()
    configure_firewall()
    
    print("Git, AWS CLI configuration, and data sync completed.")

if __name__ == "__main__":
    main()
