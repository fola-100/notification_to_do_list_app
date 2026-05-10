class Checklist:
    def __init__(self,reminder,days,time):
        self.task=reminder
        self.timer=time
        self.days=days

    def dic_format(self):
        return{ "task":self.task,
               "time":self.timer,
               "days":self.days}


