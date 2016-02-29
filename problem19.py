def is_leap_year(year):
    return year % 4 == 0 and ((year % 400 == 0) or (year % 100 != 0))


def num_days_for_year(year):
    num_days_in_feb = (29 if is_leap_year(year) else 28)
    return (4 * 30) + (31 * 7) + num_days_in_feb


def num_days_for_month(month, year):
    if month == 2:
        return (29 if is_leap_year(year) else 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31


def num_of_sundays_in_year(year, start_day):
    total = 0
    for month in range(1, 12 + 1):
        if start_day == 0:
            total += 1
        num_days = num_days_for_month(month, year)
        #print "Number of days for month {}: {}".format(month, num_days)
        start_day = (start_day + num_days) % 7
        #print "Day for new month: {}".format(start_day)
    return total, start_day


def main():

    total_days_in_1900, current_day = num_of_sundays_in_year(1900, 1)
    print "Number of Sundays in first of month in 1900: {}".format(total_days_in_1900)

    total = 0
    for year in range(1901, 2000 + 1):
        result = num_of_sundays_in_year(year, current_day)
        total += result[0]
        current_day = result[1]

    print "Number of Sundays in first of month from 1901 - 2000: {}".format(total)

if __name__ == '__main__':
    main()
