import schedule
import time
import subprocess

# Stop the script after a certain number of iterations
max_iterations = 150
current_iteration = 0

def job():
    global current_iteration
    # Your script logic here
    current_iteration += 1
    if current_iteration >= max_iterations:
        print("Maximum iterations reached. Stopping.")
        exit()

    # Replace this with the command to execute your script
    subprocess.run(["python", "C:\\PythonClass\\AlgoTrading\\oneMin.py"])

# Schedule the job every 2 minutes
schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
 