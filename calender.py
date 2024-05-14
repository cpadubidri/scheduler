from gcsa.google_calendar import GoogleCalendar
from beautiful_date import Apr, hours, May
from gcsa.event import Event
# import pandas as pd

class GCalendar():

    def __init__(self, email, credentials_path='../.credentials/credentials.json'):
        self.gc = GoogleCalendar(email, credentials_path=credentials_path)
        

    def get_event(self, time_min=None, time_max=None):
        event_list = list(self.gc.get_events(time_min, time_max))
        return event_list

    def put_event(self, event_name, start, end):
       event = Event(summary=event_name,start=start,end=end)
       self.gc.add_event(event)

    def delete_event(self, event_name):
        event_list = self.get_event()
        
        len_list = len(event_list)
        for event in event_list:
            if event.summary == event_name:
                self.gc.delete_event(event.event_id)
                break

            len_list=len_list-1
            if len_list==0:
                    print(f"{event_name} not found in the calendar")



if __name__=="__main__":
    calen = GCalendar(email='jyotiharti1@gmail.com',credentials_path='../.credentials/credentials.json')

    min_time = (19/May/2024)[14:00]
    max_time = (19/May/2024)[15:00]
    x = calen.get_event(min_time, max_time)
    print(x)





