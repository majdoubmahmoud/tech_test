#Tech_Test Guide \n
Prerequisites \n
Before starting the setup, ensure that Git is installed on your system. If not, you can install it using the following command: \n
sudo apt install git \n
Clone the repository using the following command: \n
git clone https://github.com/majdoubmahmoud/tech_test \n
cd tech_test \n
\n
#Step 1: Nginx Configuration \n
Run the nginx.py script on your backend servers: \n
python3 nginx.py \n
The script will prompt you for the following information: \n
Port for Nginx (default is 80) \n
Server name for Nginx (e.g., example.com) \n
Option to enable the firewall (y/n) \n
\n
#Step 2: HAProxy Configuration \n
Run the haproxy.py script on your proxy server (load balancer): \n
python3 haproxy.py \n
The script will prompt you for the following information: \n
HAProxy Port (default is 80) \n
Server name for HAProxy (e.g., example.com) \n
Number of backend servers \n
IP address and port for each backend server \n
\n
#Step 3: Git and AWS CLI Configuration \n
Run the git_awscli.py script on your backend servers to prepare for application deployment: \n
python3 git_awscli.py \n
The script will prompt you for the following information: \n
Git repository URL \n
AWS access key, secret key, region, and output format. \n
S3 bucket name and local path to store S3 data \n
Option to enable the firewall (y/n) \n
\n
#Step 4: Monitoring Setup \n
To monitor your solution, start a cron job that runs autoheal.py every 5 seconds: \n
crontab -e \n
Add the following line to the crontab file: \n
*/5 * * * * /path/to/your/python3 /path/to/your/autoheal.py \n
The autoheal.py script will prompt you for the health check URL and the path to the web app. It performs a health check using the provided URL. If the health check fails, it will redeploy the web app and restart Nginx. \n
