# boost_contributions.py
import os
import subprocess
import random
import datetime
import sys

REPO_NAME = "Git_hub_contributions_Boosters"
GITHUB_USERNAME = "TakshPatel5821"
GITHUB_PAT = os.getenv("GITHUB_PAT")  # must be set in env

if not GITHUB_PAT:
    sys.exit("Error: GITHUB_PAT environment variable not set. Do not hardcode tokens in code.")

def run(cmd, cwd=None, env=None, check=True):
    print("Running:", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, env=env, check=check)

def prepare_repo(repo_dir=REPO_NAME):
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir, exist_ok=True)
        run(["git", "init"], cwd=repo_dir)
    os.chdir(repo_dir)

    # Add remote with token only temporarily
    remote_with_token = f"https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
    # Remove existing origin if present (ignore errors)
    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    run(["git", "remote", "add", "origin", remote_with_token])

def make_commits(num_commits=100):
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=365)
    for i in range(num_commits):
        random_days = random.randint(0, 364)
        commit_date = start_date + datetime.timedelta(days=random_days)
        message = f"Automated commit on {commit_date.isoformat()} #{i+1}"

        with open("contribution.txt", "a") as f:
            f.write(f"{datetime.datetime.utcnow().isoformat()} - Commit on {commit_date}\n")

        env = os.environ.copy()
        # set both committer and author dates so both reflect the past date
        gdate = commit_date.strftime("%Y-%m-%dT12:00:00")
        env["GIT_COMMITTER_DATE"] = gdate
        env["GIT_AUTHOR_DATE"] = gdate

        # Stage and commit
        run(["git", "add", "contribution.txt"], env=env)
        # Allow commit failure if nothing changed; but we always append so it should change
        run(["git", "commit", "--date", gdate, "-m", message], env=env, check=False)

def push_and_cleanup():
    run(["git", "branch", "-M", "main"])
    # push using the origin that currently contains the token in the url
    run(["git", "push", "-u", "origin", "main"])
    # remove token from the remote URL (set back to tokenless remote)
    run(["git", "remote", "set-url", "origin", f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"])

def main():
    prepare_repo()
    make_commits(num_commits=50)
    push_and_cleanup()
    print("Done. Repository pushed. Remote URL reset (no token).")

if __name__ == "__main__":
    main()
