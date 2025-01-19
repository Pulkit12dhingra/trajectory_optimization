import subprocess

def main():
    try:
        result = subprocess.run(['python', 'scripts/optimize_trajectory.py'], check=True)
        print("Script executed successfully:", result)
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the script:", e)

if __name__ == "__main__":
    main()