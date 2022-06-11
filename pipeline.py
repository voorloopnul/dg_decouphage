import base64
import os
import sys

import requests as requests

url = base64.b64decode(sys.argv[1]).decode("utf-8")
os.system(f'wget "{url}" -O input_file')
os.system(f"python3 decouphage.py --tmp_dir output --output output/output.gbk -t 2 input_file")
os.system('pwd')
os.system("ls")
os.system("tar -zcvf output.tar.gz output")
with open('output.tar.gz', 'rb') as data:
    r = requests.put(os.getenv("DOCKGRID_RESULT_URL"), data=data)
    print(r.status_code)
    print(r.status_code)
