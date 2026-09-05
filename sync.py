import requests

username = "shivuelumalairr"

url = f"https://codeforces.com/api/user.status?handle={username}"

response = requests.get(url)
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

        problem = submission["problem"]

        print("Submission ID:", submission["id"])
        print("Problem:", problem["name"])
        print("Contest:", problem["contestId"])
        print("Index:", problem["index"])
        print("Rating:", problem.get("rating"))
        print("Language:", submission["programmingLanguage"])
        print("-" * 40)
if submissions:
    latest_submission = submissions[0]["id"]

    with open("last_submission.txt", "w") as file:
        file.write(str(latest_submission))