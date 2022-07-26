def leap_year(year):
    if year % 4 == 0:
        if not year % 100 == 0:
            return True
        if year % 100 == 0 and year % 400 == 0:
            return True
    return False
