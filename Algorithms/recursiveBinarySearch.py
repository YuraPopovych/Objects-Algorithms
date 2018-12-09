
#Example, imagine if listOfdays had three instances of
#date: one for January 1st 2016, one for January 1st 2017,
#and one for January 1st 2018. Then:
#  binary_search_year(listOfdays, 2016) -> True
#  binary_search_year(listOfdays, 2015) -> False

from datetime import date

def binary_search_year(days, taget_date):
    
    for day in range(len(days)):
        if not isinstance(days[day], int):
            converted_date = days[day].year
            del days[day]
            days.insert(day, converted_date)
    days.sort()
    
    mid_point = len(days) // 2
    
    if mid_point == 0:
        return days[mid_point] == taget_date
        
    if days[mid_point] == taget_date:
        return days[mid_point] == taget_date
    
    if days[mid_point] < taget_date:
        return binary_search_year(days[mid_point:], taget_date)
    else:
        return binary_search_year(days[:mid_point], taget_date)

        

#Write your code here!

#If your function works correctly, this will originally
#print: True, then False
listOfdays = [date(2016, 11, 26), date(2014, 11, 29), 
               date(2008, 11, 29), date(2000, 11, 25), 
               date(1999, 11, 27), date(1998, 11, 28), 
               date(1990, 12, 1), date(1989, 12, 2), 
               date(1985, 11, 30)]

print(binary_search_year(listOfdays, 2016))
print(binary_search_year(listOfdays, 2007))


