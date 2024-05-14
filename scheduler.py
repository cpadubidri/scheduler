import os
from datamanager import DataManager
from calender import GCalendar
from beautiful_date import *
from beautiful_date import hours, days, months
import beautiful_date


class Scheduler:

    def __init__(self, email, config_path='assets/configuration.json'):
        self.dm = DataManager()
        self.gc = GCalendar(email)
        self.config_data = self.dm.read_file(config_path)


    def add_event(self, event_data):
        ed = event_data['eventData']
        ed_nw = f"(days({ed[3:6]})/months({ed[:2]})/days({ed[-2:]}))"
        # ed_nw = (20/Apr/2024)[15:00]
        event_name = event_data['eventTitle']
        start = ed_nw
        end =  ed_nw + 1 * hours
        self.gc.put_event(event_name,start,end)


        # event_list = self.gc.get_event()
        # print(dir(event_list))

    

if __name__=="__main__":
    # sche = Scheduler()
    x = beautiful_date("25/Mar/2025")
    print(x)






