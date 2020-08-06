# Code your solution here
month = input()

month_dict = {
    "january" : "31",
    "february" : "28",
    "march" : "30",
    "april" : "31",
    "may" : "30",
    "june" : "31",
    "july" : "30",
    "august" : "31",
    "september" : "30",
    "october" : "31",
    "november" : "30",
    "december" : "31"
}

if month in month_dict.keys():
    data = month_dict.get(month)
