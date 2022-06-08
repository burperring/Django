from django.utils import timezone
import calendar


class Day:
    def __init__(self, number, past, npast):
        self.number = number
        self.past = past
        self.npast = npast

    def __str__(self):
        return str(self.number)


class Calendar(calendar.Calendar):
    def __init__(self, year, month, day):
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day = day
        self.day_names = ("Sun", "Mon", "Tue", "Wen", "Thu", "Fri", "Sat")
        self.months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_days(self):
        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        for week in weeks:
            for day, _ in week:
                now = timezone.now()
                today = now.day
                month = now.month
                past = False
                npast = False

                if month == self.month:
                    if day < today:
                        past = True
                elif month > self.month:
                    if self.day <= day:
                        past = True
                    else:
                        past = False

                if month <= self.month:
                    if self.day >= day:
                        npast = True

                new_day = Day(day, past, npast)
                days.append(new_day)
        return days

    def get_month(self):
        return self.months[self.month - 1]
