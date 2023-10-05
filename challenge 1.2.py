enteryear = int(input("enter the year you wan to check:"))
if (enteryear % 4 == 0 and enteryear % 100 != 0 or enteryear % 400 == 0):
  print("The year you've entered is a leap year")
else:
  print("The year you've entered isn't leap year!")
