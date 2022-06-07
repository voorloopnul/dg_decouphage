import base64
import sys

url = base64.b64decode(sys.argv[1])
print(url)
