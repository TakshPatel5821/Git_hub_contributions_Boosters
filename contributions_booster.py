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

# Update: 2025-11-03 15:55:27
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test function with random input: 34

# Update: 2025-02-01 14:27:15
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test function with random input: 18

# Update: 2025-11-19 07:03:23
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test function with random input: 47

# Update: 2025-09-02 19:04:39
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test function with random input: 26

# Update: 2025-02-03 12:25:18
def reverse_string(s):
    return s[::-1]

# Test function with random input: 50

# Update: 2025-11-21 06:57:47
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test function with random input: 89

# Update: 2025-08-06 05:25:15
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test function with random input: 63

# Update: 2025-08-08 13:13:05
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Test function with random input: 11

# Update: 2025-10-19 02:26:12
def reverse_string(s):
    return s[::-1]

# Test function with random input: 34

# Update: 2025-07-10 02:36:50
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test function with random input: 14

# Update: 2025-05-20 12:26:37
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Test function with random input: 41

# Update: 2025-07-17 16:14:34
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test function with random input: 93

# Update: 2022-09-26 08:34:52
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test function with random input: 18

# Update: 2022-04-26 07:29:17
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test function with random input: 88

# Update: 2022-06-28 18:33:18
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test function with random input: 88

# Update: 2022-03-23 01:50:50
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test function with random input: 69

# Update: 2022-07-23 01:21:59
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test function with random input: 63

# Update: 2022-06-11 15:07:52
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test function with random input: 62

# Update: 2022-01-07 11:59:18
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test function with random input: 45

# Update: 2022-05-30 05:15:56
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test function with random input: 70

# Update: 2022-08-05 13:59:30
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test function with random input: 36

# Update: 2022-12-03 18:27:44
def sort_algorithm(arr):
    return sorted(arr, key=lambda x: (x % 2, x))

# Test function with random input: 92

# Update: 2022-01-28 17:42:02
def sort_algorithm(arr):
    return sorted(arr, key=lambda x: (x % 2, x))

# Test function with random input: 4

# Update: 2022-09-17 09:13:31
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test function with random input: 20

# Update: 2022-02-02 13:55:48
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test function with random input: 56

# Update: 2022-06-22 19:43:06
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test function with random input: 31
