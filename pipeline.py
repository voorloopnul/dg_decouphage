import base64
import os
import sys
from subprocess import run
import requests as requests

url = base64.b64decode(sys.argv[1]).decode("utf-8")
parameters = " ".join(sys.argv[2:])

# Download input file
#

ret = os.system(f'wget "{url}" -O input_file')

# Run decouphage
#

cmd = f"python3 decouphage.py --tmp_dir output --output output/output.gbk {parameters} input_file"
decouphage = run(cmd.split(" "))
if decouphage.returncode:
    sys.exit(1)

# Compress output
#

os.system("tar -zcvf output.tar.gz output")

# Upload output
#

with open('output.tar.gz', 'rb') as data:
    r = requests.put(os.getenv("DOCKGRID_RESULT_URL"), data=data)
    print(r.status_code)
