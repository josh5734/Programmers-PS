def solution(a, b):
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    import calendar
    day_number = calendar.weekday(2016, a, b)
    answer = day[day_number]
    return answer
