from gcsa.google_calendar import GoogleCalendar
from beautiful_date import Apr, hours
from gcsa.event import Event
# import pandas as pd

class GCalendar():

    def __init__(self, email):
        self.gc = GoogleCalendar(email)
        

    def get_event(self, time_min=None, time_max=None):
        event_list = list(self.gc.get_events(time_min, time_max))
        return event_list

    def add_event(self, event_name, start, end):
       event = Event(event_name,start=start,end=end)
       self.gc.add_event(event)
        




if __name__=="__main__":
    calen = GCalendar(email='jyotiharti1@gmail.com')

    # min_time = (17/Apr/2024)[10:00]
    # max_time = (17/Apr/2024)[14:00]
    # x = calen.get_event(min_time, max_time)
    # print(x)

    # calen.add_event()




