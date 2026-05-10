import json
from json import JSONDecodeError


def store_user_info(info):
        try:
            with open("task_info.json", "r") as f:
                details = json.load(f)
        except (FileNotFoundError, JSONDecodeError):
            details=[]

        details.append(info)

        with open("task_info.json", "w") as f:
            json.dump(details, f,indent=4)
        return "file saved successfully"


def fetch_info():
    try:
        with open("task_info.json","r")as file:
            saved_info=json.load(file)
            return saved_info
    except(FileNotFoundError,JSONDecodeError):
        return []




