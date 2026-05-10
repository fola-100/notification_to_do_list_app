import task_info
import storage_vault
import system_functions as sf
def store_user_info():
    task, days, time_span = sf.collect_info()
    to_do_list_info = task_info.Checklist(task, days, time_span)
    task_details = to_do_list_info.dic_format()
    storage_vault.store_user_info(task_details)

def load_saved_records():
   data_saved=storage_vault.fetch_info()
   return data_saved

#-------Triggered----
already_triggered=[]

#----------COLLECT ALL USER INFOR-------
def user_engine():
    store_user_info()
#---------
def system_engine():
    global already_triggered
    task_records = load_saved_records()
    sf.check_reminder(task_records,already_triggered)
    sf.reset_trigger(already_triggered)


user_engine()