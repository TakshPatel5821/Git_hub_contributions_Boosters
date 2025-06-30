import os
import subprocess
import random
import datetime

# GitHub repository details
REPO_NAME = "Git_hub_contributions_Boosters"
GITHUB_USERNAME = "TakshPatel5821"
GITHUB_PAT = "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"  # Use environment variables instead

# Clone or initialize the repo
if not os.path.exists(REPO_NAME):
    os.makedirs(REPO_NAME)
    subprocess.run(["git", "init"], cwd=REPO_NAME)

# Change directory to repo
os.chdir(REPO_NAME)

# Add remote if not exists
subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
subprocess.run(["git", "remote", "add", "origin", f"https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"])

# Generate random commit dates in the past year
today = datetime.date.today()
start_date = today - datetime.timedelta(days=365)

for _ in range(100):  # Make 100 commits
    random_days = random.randint(0, 364)
    commit_date = start_date + datetime.timedelta(days=random_days)
    commit_message = f"Automated commit on {commit_date}"

    # Create a dummy file or modify an existing one
    with open("contribution.txt", "a") as file:
        file.write(f"Commit on {commit_date}\n")

    # Git commands to commit with a past date
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = commit_date.strftime("%Y-%m-%d 12:00:00")
    subprocess.run(["git", "add", "."], env=env)
    subprocess.run(["git", "commit", "--date", commit_date.strftime("%Y-%m-%d 12:00:00"), "-m", commit_message], env=env)

# Push to GitHub
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "push", "-u", "origin", "main"])

print("GitHub contribution commits added successfully!")

# Update: 2025-02-21 08:50:54
def sort_algorithm(arr):
    return sorted(arr, key=lambda x: (x % 2, x))

# Test function with random input: 63

# Update: 2025-02-21 08:51:57
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Test function with random input: 98

# Update: 2025-02-21 09:02:47
def sort_algorithm(arr):
    return sorted(arr, key=lambda x: (x % 2, x))

# Test function with random input: 16

# Update: 2025-02-21 09:02:53
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test function with random input: 79

# Update: 2025-04-24 07:25:45
def reverse_string(s):
    return s[::-1]

# Test function with random input: 55

# Update: 2025-02-14 15:31:48
def sort_algorithm(arr):
    return sorted(arr, key=lambda x: (x % 2, x))

# Test function with random input: 35

# Update: 2025-11-08 04:32:40
def reverse_string(s):
    return s[::-1]

# Test function with random input: 59

# Update: 2025-10-20 15:45:28
def sort_algorithm(arr):
    return sorted(arr, key=lambda x: (x % 2, x))

# Test function with random input: 34

# Update: 2025-06-30 06:48:55
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Test function with random input: 69
