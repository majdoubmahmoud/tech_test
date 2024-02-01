import subprocess

def install_packages():
    subprocess.run(['sudo', 'apt-get', 'install', 'git', 'awscli'])

def clone_git_repo():
    git_repo_url = input("enter git repository url: ")
    subprocess.run(['git', 'clone', git_repo_url])
    print("web application code cloned successfully")

def configure_aws_cli():
    aws_access_key = input("enter AWS access key: ")
    aws_secret_key = input("enter AWS secret key: ")
    aws_region = input("enter AWS region (us-east-1 for example): ")
    output_format = input("enter desired output format (json for example): ").lower()

    subprocess.run(['aws', 'configure', 'set', 'aws_access_key_id', aws_access_key])
    subprocess.run(['aws', 'configure', 'set', 'aws_secret_access_key', aws_secret_key])
    subprocess.run(['aws', 'configure', 'set', 'region', aws_region])
    subprocess.run(['aws', 'configure', 'set', 'output', output_format])
    print("AWS CLI configured successfully")

def pull_data_from_s3():
    s3_bucket = input("enter S3 bucket name: ")
    local_data_path = input("enter local path to store S3 data (/path/to/local/data): ") or '/s3/data'
    
    subprocess.run(['aws', 's3', 'sync', f's3://{s3_bucket}', local_data_path])
    print("data pulled from S3 successfully")

def configure_firewall():
    firewall_enabled = input("enable firewall? (y/n): ").lower() == 'y'

    if firewall_enabled:
        subprocess.run(['sudo', 'ufw', 'allow', '22'])  #for git ssh
        subprocess.run(['sudo', 'ufw', 'allow', '443'])
        subprocess.run(['sudo', 'ufw', 'enable'])
        print("firewall configured and enabled")
    else:
        print("firewall not configured")

def main():
    install_packages()
    clone_git_repo()
    configure_aws_cli()
    pull_data_from_s3()
    configure_firewall()
    
    print("git, AWS CLI configuration, and data sync completed")

if __name__ == "__main__":
    main()
