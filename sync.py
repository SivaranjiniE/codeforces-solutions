import requests
from dotenv import load_dotenv
import os
import time
import hashlib
import random
import base64
import re

new_solution = False

load_dotenv()

api_key = os.getenv("CF_API_KEY")
api_secret = os.getenv("CF_API_SECRET")

username = "shivuelumalairr"

method = "user.status"

params = {
    "apiKey": api_key,
    "handle": username,
    "includeSources": "true",
    "time": int(time.time())
}

rand = str(random.randint(100000, 999999))

query = "&".join(
    f"{key}={params[key]}"
    for key in sorted(params)
)

signature_string = f"{rand}/{method}?{query}#{api_secret}"

api_sig = rand + hashlib.sha512(
    signature_string.encode()
).hexdigest()

params["apiSig"] = api_sig

url = f"https://codeforces.com/api/{method}"

response = requests.get(url, params=params)
data = response.json()

submissions = data["result"]

last_submission = 0

try:
    with open("last_submission.txt", "r") as file:
        last_submission = int(file.read())
except FileNotFoundError:
    pass


for submission in submissions:

    if submission["id"] <= last_submission:
        continue

    if submission["verdict"] == "OK":

        source = submission.get("sourceBase64")

        if source:
            code = base64.b64decode(source).decode("utf-8")

            problem = submission["problem"]

            safe_name = re.sub(
                r'[<>:"/\\|?*]',
                '',
                problem["name"]
            )

            safe_name = safe_name.replace(" ", "_")

            filename = f"{problem['index']}_{safe_name}.py"

            with open(filename, "w", encoding="utf-8") as file:
                file.write(code)
            new_solution = True
            print("Accepted solution saved:", filename)


if submissions:
    latest_submission = submissions[0]["id"]

    with open("last_submission.txt", "w") as file:
        file.write(str(latest_submission))
if new_solution:
   import subprocess

   subprocess.run(["git", "add", "."])
   subprocess.run(["git", "commit", "-m", "Add new accepted Codeforces solutions"])
   subprocess.run(["git", "push", "origin", "main"])