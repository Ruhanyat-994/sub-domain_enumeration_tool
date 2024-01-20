import os
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <file_with_subdomains> <domain>")
    sys.exit(1)

file = sys.argv[1]
path = os.path.join(os.getcwd(), file)

sub_list = open(file).read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[2]}"
    
    try:
        requests.get(sub_domains)
    except requests.ConnectionError:
        pass
    else:
        print("Valid domain:", sub_domains)
