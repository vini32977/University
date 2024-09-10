import datetime
today=datetime.datetime.now().date()
print("Current date is: ",today)
days_to_add=int(input("Enter the number of days to add: "))
new_date=today+datetime.timedelta(days=days_to_add)
print("Date after adding the days",days_to_add,"day is: ",new_date)