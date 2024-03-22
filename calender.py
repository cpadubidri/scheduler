from gcsa.google_calendar import GoogleCalendar
from beautiful_date import Mar, hours
from gcsa.event import Event
import pandas as pd

class GCalendar:

    def __init__(self, email):
        self.gc = GoogleCalendar(email)
        self.index=0
        self.events = list(self.gc.get_events())


    def put_event(self):
        pass

    def get_events(self):
        return self.events
    

    def delete_event(self):
        pass

    def edit_event(self):
        pass


    




if __name__=="__main__":
    ch = GCalendar(email='padubidrichirag0@gmail.com')
    x = ch.get_events()
    print(x)



