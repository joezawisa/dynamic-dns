import sys
import logging
import logging.handlers
import os
import time
import getpass
import requests

# Configure logging
logging.basicConfig(
    format='[%(asctime)s | %(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.handlers.RotatingFileHandler(
            filename=f'{os.path.splitext(sys.argv[0])[0]}.log',
            mode='a',
            maxBytes=1024*1024*5,
            backupCount=1
        )
    ]
)

# Check for valid invocation
if (len(sys.argv) < 4) or (len(sys.argv) > 5):

    print(f'Usage: {sys.argv[0]} <interval> <hostname> <username> [password]', file=sys.stderr)
    sys.exit(1)

# Read parameters
interval = 60 * int(sys.argv[1])
hostname = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4] if len(sys.argv) == 5 else getpass.getpass(prompt='Password: ')

# Update the dynamic DNS record on the requested interval
while True:

    # Check client IP address
    ip = requests.get(url='https://domains.google.com/checkip')

    logging.info(f'Posting IP Address: {bytes.decode(ip.content)}')

    # Post the IP address to the dynamic DNS record on Google Domains
    response = requests.post(
        url='https://domains.google.com/nic/update',
        auth=requests.auth.HTTPBasicAuth(username, password),
        params={
            'hostname': hostname, 'myip': ip.content
        }
    )

    logging.info(f'Response Code: {response.status_code}')

    # Wait a few minutes before updating the DNS record again
    time.sleep(interval)