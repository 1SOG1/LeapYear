import pytest
from leap_year_check_function import leap_year_check

print("==== Leap Year Checker 3000 ====\n\n")

print("What year would you like to check? ")


year_to_check = int(input(" "))

if leap_year_check(year_to_check):
    print(f"\n{year_to_check} is a leap year! boy-oh boy... what will you do with all this time?!\n")
else:
    print(f"\n{year_to_check} is not a leap year :-( dont get to leap into the couch one extra day this year i guess\n")





