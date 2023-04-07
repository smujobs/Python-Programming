input_year = int(input('년:'))
input_month = int(input('월:'))

days_31 = [1, 3, 5, 7, 8, 10, 12]
days_30 = [4, 6, 9, 11]

def is_leap_year(year_to_check):
    if year_to_check % 4 == 0 and year_to_check % 100 != 0:
        return True
    elif year_to_check % 400 == 0:
        return True
    else: return False

def month_days(month_to_check):
    if month_to_check in days_31:
        return 31
    elif month_to_check in days_30:
        return 30
    else: return 28

if is_leap_year(input_year) and input_month == 2:
    day = 29
else:
    day = month_days(input_month)

print('{}년 {}월은 {}일까지 있습니다.'.format(input_year, input_month, day))
