import schedule
import time
import subprocess

# Stop the script after a certain number of iterations
max_iterations = 250
current_iteration = 0

def job():
    global current_iteration
    # Your script logic here
    current_iteration += 1
    if current_iteration >= max_iterations:
        print("Maximum iterations reached. Stopping.")
        exit()

    # enter script language and script path to execute
    subprocess.run(["python", "C:\\Users\\Ekrem.Ersayin\\Documents\\pythonwork\\PCS\\antLab_PR_oneMin.py"])

# Schedule the job based on given frequency
# schedule.every(2).minutes.do(job)
schedule.every(90).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

