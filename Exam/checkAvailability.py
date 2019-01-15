

from datetime import datetime
class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


def check_availability(list_of_meetings, proposal_time):
    for meeting in list_of_meetings:
        if  meeting.start_time <= proposal_time <= meeting.end_time:
            return False
    return True


meetings = [Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)),
            Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
            Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]
print(check_availability(meetings, datetime(2018, 8, 1, 12, 0, 0)))
print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))


