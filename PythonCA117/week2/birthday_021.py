import sys
import calendar
line = sys.stdin.readlines()

weekdaysweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ripper = ["Monday's child is fair of face", "Tuesday's child is full of grace", "Wednesday's child is full of woe", "Thursday's child has far to go", "Friday's child is loving and giving", "Saturday's child works hard for a living", "Sunday's child is fair and wise and good in every way"]

def day(wait):
    day, month, year = wait.split()
    return weekdaysweek[calendar.weekday(int(year), int(month), int(day))]

def notes(wait):
    day, month, year = wait.split()
    return ripper[calendar.weekday(int(year), int(month), int(day))]


for bday in line:
    print(f"You were born on a {day(bday)} and {notes(bday)}.")
