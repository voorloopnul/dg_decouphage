import base64
import os
import sys

url = str(base64.b64decode(sys.argv[1]))
os.system(f"wget {url}")
os.system(f"ls")
