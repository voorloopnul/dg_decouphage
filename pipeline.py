import base64
import os
import sys

import requests as requests

url = base64.b64decode(sys.argv[1]).decode("utf-8")
os.system(f'wget "{url}" -O input_file')
os.system(f"python3 decouphage.py input_file")
os.system('pwd')
os.system("ls")
with open('output.gbk', 'rb') as data:
    r = requests.put(os.getenv("DOCKGRID_RESULT_URL"), data=data)
    print(r.status_code)
