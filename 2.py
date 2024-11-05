def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    if month < 1 or month > 12 or year < 1:
        return None

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987, 2024, 2023, 0]
test_months = [2, 2, 1, 11, 2, 12, 1]
test_results = [28, 29, 31, 30, 29, 31, None]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print(" OK")
    else:
        print(" Failed")
