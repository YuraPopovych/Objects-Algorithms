
def measure_string(myStr):
    myStr = list(myStr)
    if myStr == []:
        return 0
    else:
        del myStr[0]
        return 1 + measure_string(myStr)

print(measure_string("13 characters"))



