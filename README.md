#Tech_Test Guide

Prerequisites

Before starting the setup, ensure that Git is installed on your system. If not, you can install it using the following command:

<sudo apt install git>

Clone the repository using the following command:

<git clone https://github.com/majdoubmahmoud/tech_test>

<cd tech_test>


#Step 1: Nginx Configuration

Run the nginx.py script on your backend servers:

<python3 nginx.py>

The script will prompt you for the following information:

Port for Nginx (default is 80)

Server name for Nginx (e.g., example.com)

Option to enable the firewall (y/n)


#Step 2: HAProxy Configuration

Run the haproxy.py script on your proxy server (load balancer):

<python3 haproxy.py>

The script will prompt you for the following information:

HAProxy Port (default is 80)

Server name for HAProxy (e.g., example.com)

Number of backend servers

IP address and port for each backend server


#Step 3: Git and AWS CLI Configuration

Run the git_awscli.py script on your backend servers to prepare for application deployment:

<python3 git_awscli.py>

The script will prompt you for the following information:

Git repository URL

AWS access key, secret key, region, and output format

S3 bucket name and local path to store S3 data

Option to enable the firewall (y/n)


#Step 4: Monitoring Setup

To monitor your solution, start a cron job that runs autoheal.py every 5 seconds:

<crontab -e>

Add the following line to the crontab file:

*/5 * * * * /path/to/your/python3 /path/to/your/autoheal.py

The autoheal.py script will prompt you for the health check URL and the path to the web app. It performs a health check using the provided URL. If the health check fails, it will redeploy the web app and restart Nginx.
