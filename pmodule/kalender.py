import calendar
kalenderblatt = calendar.LocaleTextCalendar(calendar.MONDAY)
ausgabe = kalenderblatt.formatmonth(2020,3)
print(ausgabe)
#
print()
#
print("Jahreskalendar")
kalenderblatt = calendar.LocaleTextCalendar(calendar.MONDAY)
ausgabe = kalenderblatt.formatyear(1995)
print(ausgabe)
