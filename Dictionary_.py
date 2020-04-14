# Первый тестовый
# Второй тестовый
month_switcher = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

for i in range(14):
    if i in month_switcher:
        print(i, month_switcher[i])
    else:
        print(i,'invalid month number')