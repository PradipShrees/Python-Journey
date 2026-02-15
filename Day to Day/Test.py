import json
import requests

import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=)" + sys.argv[1])

Res = response.json()
for result in Res["results"]:
    print(result["trackName"])


#python3 "Day to Day/Test.py" weezer