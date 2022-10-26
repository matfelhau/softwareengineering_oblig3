# Sources I used to make it work.
# Source1 = "https://stackoverflow.com/questions/33813848/how-to-say-to-the-python-that-the-number-should-not-be-divisible"
# Source2 = "https://www.programiz.com/python-programming/examples/leap-year"
# Source3 = "https://stackoverflow.com/questions/11621740/how-to-determine-whether-a-year-is-a-leap-year"

def isLeapYear(year: int):
    if (year % 4 == 0) & (year % 100 != 0):
        return True
    elif (year % 400 == 0): 
        return True
    else:
        return False