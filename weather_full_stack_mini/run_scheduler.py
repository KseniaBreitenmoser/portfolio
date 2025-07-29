import schedule
import time
import os

def run_prediction():
    print("Runing daily prediction task...")
    os.system("python pipeline/run_daily_prediction.py")

# Schedule to run once a day at 08 am
schedule.every().day.at("17:13").do(run_prediction)

print("Scheduler started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(30) # Check every 30 seconds
