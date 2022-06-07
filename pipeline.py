import base64
import os
import sys

url = base64.b64decode(sys.argv[1]).decode("utf-8")
os.system(f'wget "{url}" -O input_file')
os.system(f"python3 decouphage.py input_file")
