import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
if result.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Command failed with exit code {result.returncode}.")
