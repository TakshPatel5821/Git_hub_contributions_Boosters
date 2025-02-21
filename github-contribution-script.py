import os
import datetime
import random
import subprocess
import time

def setup_repository():
    """Set up a new repository for automating contributions."""
    # Create a new directory for the repository
    repo_name = "contribution-tracker"
    if not os.path.exists(repo_name):
        os.makedirs(repo_name)
    
    # Navigate to the repository directory
    os.chdir(repo_name)
    
    # Initialize git repository if not already initialized
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        
        # Create a README file
        with open("README.md", "w") as f:
            f.write("# Contribution Tracker\n\nThis repository tracks my coding activity.")
        
        # Configure git if needed (uncomment and modify if necessary)
        # subprocess.run(["git", "config", "user.name", "Your Name"])
        # subprocess.run(["git", "config", "user.email", "your.email@example.com"])
        
        # Make initial commit
        subprocess.run(["git", "add", "README.md"])
        subprocess.run(["git", "commit", "-m", "Initial commit"])
        
        print("Repository initialized successfully!")
    else:
        print("Repository already exists.")
    
    # Return to parent directory
    os.chdir("..")
    return os.path.abspath(repo_name)

def make_contribution(repo_path):
    """Make a contribution to the repository."""
    # Navigate to the repository
    os.chdir(repo_path)
    
    # Create or update a file
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"activity_{date}.txt"
    
    # Add random content to the file
    with open(filename, "w") as f:
        f.write(f"Activity logged at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Random number: {random.randint(1, 1000)}\n")
    
    # Commit the changes
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"Activity update for {date}"])
    
    print(f"Contribution made on {date}")
    
    # Return to parent directory
    os.chdir("..")

def connect_to_github(repo_path):
    """Connect the local repository to GitHub."""
    os.chdir(repo_path)
    
    # Instructions for manually connecting to GitHub
    print("\n=== CONNECTING TO GITHUB ===")
    print("To connect this repository to GitHub, follow these steps:")
    print("1. Create a new repository on GitHub (without README, license, or .gitignore)")
    print("2. Run the following commands in your terminal:")
    print(f"   cd {repo_path}")
    print("   git remote add origin https://github.com/YOUR_USERNAME/contribution-tracker.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print("\nAfter completing these steps, future contributions will be pushed to GitHub.\n")
    
    # Optional: Automate the push if remote is already set
    try:
        # Check if remote exists
        remote_check = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        if "origin" in remote_check.stdout:
            push_changes = input("Remote origin already configured. Push changes now? (y/n): ")
            if push_changes.lower() == 'y':
                subprocess.run(["git", "push", "-u", "origin", "main"])
                print("Changes pushed to GitHub!")
    except Exception as e:
        print(f"Error checking remote: {e}")
    
    os.chdir("..")

def automate_contributions(repo_path, days=30, frequency=1):
    """
    Automate contributions over a period of time.
    
    Parameters:
    - repo_path: Path to the git repository
    - days: Number of days to run the automation
    - frequency: Number of contributions per day
    """
    print(f"Starting contribution automation for {days} days ({frequency} commit(s) per day)")
    
    for day in range(days):
        for _ in range(frequency):
            make_contribution(repo_path)
            time.sleep(random.randint(1, 5))  # Random delay between commits
        
        # Push changes to GitHub if remote is configured
        os.chdir(repo_path)
        try:
            remote_check = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
            if "origin" in remote_check.stdout:
                subprocess.run(["git", "push"])
                print("Changes pushed to GitHub!")
        except Exception:
            pass
        os.chdir("..")
        
        # If not last day, wait until tomorrow
        if day < days - 1:
            print(f"Day {day+1} complete. Waiting for next day...")
            # In a real script, you'd wait until the next day
            # For demonstration, we'll just wait a few seconds
            time.sleep(10)  # Just for demonstration
    
    print("Contribution automation completed!")

def main():
    print("=== GitHub Contribution Automation ===")
    repo_path = setup_repository()
    
    # Ask to connect to GitHub
    connect_github = input("Would you like to connect this repository to GitHub? (y/n): ")
    if connect_github.lower() == 'y':
        connect_to_github(repo_path)
    
    # Ask for automation settings
    automate = input("Would you like to automate contributions? (y/n): ")
    if automate.lower() == 'y':
        try:
            days = int(input("For how many days? (default: 30): ") or 30)
            frequency = int(input("How many contributions per day? (default: 1): ") or 1)
            automate_contributions(repo_path, days, frequency)
        except ValueError:
            print("Invalid input. Using default values.")
            automate_contributions(repo_path)
    else:
        print(f"\nRepository created at: {repo_path}")
        print("You can make manual contributions by running this script again.")

if __name__ == "__main__":
    main()
