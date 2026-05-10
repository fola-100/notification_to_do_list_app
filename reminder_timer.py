import time
import main
import schedule

schedule.every(60).seconds.do(main.system_engine)

while True:
    schedule.run_pending()
    time.sleep(1)

