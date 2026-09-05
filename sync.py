import requests

username = "shivuelumalairr"

url = f"https://codeforces.com/api/user.status?handle={username}"

response = requests.get(url)
data = response.json()

submissions = data["result"]

for submission in submissions:
    if submission["verdict"] == "OK":

        problem = submission["problem"]

        print("Submission ID:", submission["id"])
        print("Problem:", problem["name"])
        print("Contest:", problem["contestId"])
        print("Index:", problem["index"])
        print("Rating:", problem.get("rating"))
        print("Language:", submission["programmingLanguage"])
        print("-" * 40)