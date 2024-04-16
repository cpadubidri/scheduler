from calender import GCalendar
from beautiful_date import Apr, hours


if __name__=="__main__":
    calen = GCalendar(email='jyotiharti1@gmail.com')

    event_name = 'Test_meeting'
    start = (20/Apr/2024)[14:00]
    end =  start + 2 * hours
    calen.add_event(event_name, start,end)


    print(calen.get_event())


    event_name = 'reading_test'
    start = (22/Apr/2024)[10:00]
    end =  start + 1 * hours
    calen.add_event(event_name,start,end)

    print(calen.get_event())



