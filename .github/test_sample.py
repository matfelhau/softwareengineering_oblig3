from leapyear import isLeapYear

# A leap year is dividible by 4 & 400, and not dividible by 100
# A year is not a leap year when it is dividible by 100, 
# and not dividible by 4 & 400, 
# (this is what my test's check, by using isLeapYear function).

# Some specific testing of each acceptence criteria: 

# Checking leap year:

# Testing if the year is dividible by 4, but not 100:
def test_is_year_dividible_by_four_but_not_one_hundred():
    assert isLeapYear(1996) # equals 1996 is a leap year.

# Testing if the year is dividible by 400:
def test_is_year_dividible_by_four_hundred():
    assert isLeapYear(2000) # equals 2000 is a leap year.

# Checking if not a leap year:

# Testing if the year is not dividible by 4
def test_is_year_not_dividible_by_four():
    assert not isLeapYear(1997) # equals 1997 is not a leap year.

# Testing if the year is dividible by 100, but not 400:
def test_is_leap_year_dividible_by_one_hundred_but_not_four_hundred():
    assert not isLeapYear(1400) # equals 1400 is not a leap year.

# General testing of more numbers:

# Testing if year(s) is a leap year, checks if year returns true.
# If year == true, then it is a leap year.
def test_verify_if_year_is_leap_year():
    assert isLeapYear(1600) == True
    assert isLeapYear(1996) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(2012) == True
    assert isLeapYear(4000) == True

# Testing if year(s) is not a leap year, checks if year returns false. 
# If year == false, then it is not a leap year.
def test_verify_if_year_is_not_leap_year():
    assert isLeapYear(2001) == False
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False


# Confirming that a year that has been called (a leap year), if it
# is in fact a leap year, by expecting it to not return False, when it's been run.
# Similiar to the test: test_verify_if_year_is_leap_year
def test_confirming_that_leap_year_is_leap_year():
    assert not isLeapYear(1600) == False
    assert not isLeapYear(1996) == False
    assert not isLeapYear(2000) == False
    assert not isLeapYear(2012) == False
    assert not isLeapYear(4000) == False


# Confirming that a year that has been called (not a leap year), if it 
# is in fact not a leap year, by expecting it to not return True, when it's been run.
# Similiar to the test: test_verify_if_year_is_not_leap_year
def test_confirming_that_leap_year_is_not_leap_year():
    assert not isLeapYear(2001) == True
    assert not isLeapYear(1700) == True
    assert not isLeapYear(1800) == True
    assert not isLeapYear(1900) == True
    assert not isLeapYear(2100) == True
