def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        raise ValueError("month must be between 1 and 12")
    return days[month - 1]


def days_in_year(year):
    return 366 if is_leap_year(year) else 365


def day_of_year(day, month, year):
    total = day
    for m in range(1, month):
        total += days_in_month(m, year)
    return total


def zeller_day_of_week(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return names[h]


def gregorian_to_julian_day_number(day, month, year):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045


def days_between(day1, month1, year1, day2, month2, year2):
    jd1 = gregorian_to_julian_day_number(day1, month1, year1)
    jd2 = gregorian_to_julian_day_number(day2, month2, year2)
    return jd2 - jd1


def age_in_years(birth_day, birth_month, birth_year, current_day, current_month, current_year):
    age = current_year - birth_year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1
    return age


def week_number(day, month, year):
    doy = day_of_year(day, month, year)
    return (doy - 1) // 7 + 1


def seconds_to_hms(total_seconds):
    hours = int(total_seconds) // 3600
    minutes = (int(total_seconds) % 3600) // 60
    seconds = int(total_seconds) % 60
    return (hours, minutes, seconds)


def hms_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


def unix_timestamp_to_days(timestamp):
    return timestamp / 86400.0


def easter_date(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return (day, month)
