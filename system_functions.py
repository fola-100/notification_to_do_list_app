import time
from datetime import datetime

def select_days():
    while True:
        correct=True
        print("Enter days you want to be reminded use comma to separate days")
        days_of_week=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        days = input(">:")
        days_selected = []

        for day in days.split(","):
            cleaned_day=day.strip().capitalize()
            days_selected.append(cleaned_day)

            if cleaned_day not in days_of_week:
                print(f'{day} is not a day of the week')
                correct=False
        if correct:
            return days_selected

def timer():
    while True:
        print("Enter in the time you want to be remember in this formate(H:M)")
        time_entered = input(">:")
        try:
            cleaned_time=datetime.strptime(time_entered, "%H:%M")
            string_formate=time_convert(cleaned_time)

            return string_formate
        except ValueError:
            print("Wrong formate sure you enter in correct formate")

def time_convert(time_period):
    string_format=time_period.strftime("%H:%M")
    return string_format

def collect_task():
   task=input("Enter in to-do-list task:")
   while not task:
       print("No task entered")
       task = input("Enter in to-do-list task:")
   else:
       return task

def collect_info():
  task=collect_task()
  days=select_days()
  time_period = timer()
  return task,days,time_period

def current_day():
    now = datetime.now()
    day = now.strftime("%A")
    time_formate=now.strftime("%H:%M")
    return time_formate,day


def trigger_check(reminder_time,task,state):
    for each_trigger in state:
        trigger_task, trigger_timer,time_stamp=each_trigger
        if trigger_task==task and trigger_timer==reminder_time:
            return True
    return False


def check_reminder(task_record_saved, triggered_value):
    current_time, day = current_day()
    for each_task_save in task_record_saved:
# CHECKING IF REMINDER ALREADY TRIGGERED
        time_saved = each_task_save["time"]
        task = each_task_save["task"]
        result=trigger_check(time_saved, task, triggered_value)

# IF NOT TRIGGERED
        if not result:
          if day in each_task_save["days"]:
            if current_time == each_task_save["time"]:
                triggered_period = time.monotonic()
                triggered_value.append((each_task_save["task"], each_task_save["time"],triggered_period))
                print(each_task_save["task"])



def reset_trigger(state):
    time_period = 60 * 60
    current_time = time.monotonic()

    index_to_remove=[]


    for index, each_trigger in enumerate(state):
        trigger_task, trigger_timer, time_stamp = each_trigger

        if current_time - time_stamp > time_period:
           index_to_remove.append(index)

    for index in reversed(index_to_remove):
        state.pop(index)

    






















