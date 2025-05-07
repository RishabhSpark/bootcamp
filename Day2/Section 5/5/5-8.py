import subprocess
import time

# Start a long-running subprocess
process = subprocess.Popen(["sleep", "10"])

# Wait for 3 seconds and terminate the subprocess
time.sleep(3)
process.terminate()
print("Subprocess terminated.")
