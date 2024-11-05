def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        return None
    if month == 2 and is_year_leap(year):
        return 29

    return days_in_months[month - 1]


def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    days_in_current_month = days_in_month(year, month)
    if day < 1 or day > days_in_current_month:
        return None

    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(year, m)
    day_of_year += day

    return day_of_year


print(day_of_year(2000, 12, 31))
print(day_of_year(2021, 1, 1))
print(day_of_year(2021, 2, 29))
print(day_of_year(2004, 2, 29 ))