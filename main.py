import calendar
from colorama import Fore, Style, init


init(autoreset=True)


year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))


print(f"\n{calendar.month_name[month]} {year}\n")


week_header = ["Mo", "Tu", "We", "Th", "Fr", "Sa", Fore.RED + "Su" + Style.RESET_ALL]
print(" ".join(f"{day:>2}" for day in week_header))  

month_calendar = calendar.monthcalendar(year, month)


for week in month_calendar:
    for i, day in enumerate(week):
        if day == 0:  
            print("  ", end=" ")  
        elif i == 6:  
            print(Fore.RED + f"{day:2}" + Style.RESET_ALL, end=" ")
        else:
            print(f"{day:2}", end=" ")  
    print()  
