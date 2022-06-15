import base64
import os
import sys

import requests as requests

url = base64.b64decode(sys.argv[1]).decode("utf-8")
cmd = " ".join(sys.argv[2:])

ret = os.system(f'wget "{url}" -O input_file')
print(ret)

ret = os.system(f"python3 decouphage.py --tmp_dir output --output output/output.gbk {cmd} input_file")
print(ret)

ret = os.system('pwd')
print(ret)

ret = os.system("ls")
print(ret)

ret = os.system("tar -zcvf output.tar.gz output")
print(ret)

with open('output.tar.gz', 'rb') as data:
    r = requests.put(os.getenv("DOCKGRID_RESULT_URL"), data=data)
    print(r.status_code)
    print(r.status_code)
