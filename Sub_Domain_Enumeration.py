import os
import requests
import sys

file = f"{sys.argv[1]}"
path = os.getcwd() + file

sub_domain = open(file).read()
directories= sub_domain.splitlines()

for sub in directories:
    sub_enum = f"http://{sub}.{sys.argv[2]}"
    try:
        requests.get(sub_enum)
    except requests.ConnectionError :
        pass
    else:
        print(" Valid Domain ----- ",sub_enum)