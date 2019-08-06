year = input("Enter Calendar Year: ")
month = input("Enter Month Number: ")
date = input("Enter Date: ")
def dayNumber(day, month, year):
	t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
	year -= month < 3
	ind = t[month-1]
	value = (year + year / 4 - year / 100 + year / 400 + ind + day) % 7
	return value
def getMonthName(monthNumber):
	months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
	return (months[monthNumber])
def numberOfDays(monthNumber, year):
	# January
	if (monthNumber == 0):
		return 31
	# February
	if (monthNumber == 1):
		# If the year is leap then February has 29 days 
		if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
			return 29
		else:
			return 28
	# March 
	if (monthNumber == 2):
		return 31
	# April
	if (monthNumber == 3):
		return 30
	# May
	if (monthNumber == 4):
		return 31
	# June
	if (monthNumber == 5):
		return 30
	# July
	if (monthNumber == 6):
		return 31
	# August
	if (monthNumber == 7):
		return 31
	# September
	if (monthNumber == 8):
		return 30
	# October
	if (monthNumber == 9):
		return 31
	# November
	if (monthNumber == 10):
		return 30
	# December
	if (monthNumber == 11):
		return 31
def printCalendar(date, month, year):
	print "         Calendar - %s" %year
	current = dayNumber(date, month, year)
	days = numberOfDays(month, year)
	MonthName = getMonthName(month-1)
	print "  ------------%s-------------" %MonthName
	print "  Sun   Mon   Tue   Wed   Thu   Fri   Sat\n" # Print the columns
	for k in range(1,current): 		# Print appropriate spaces
		print "     ",
	for j in range(1,days+1):
		print '{: >5}'.format(j),
		k=k+1
		if (k > 6):
			print "\n"
			k = 0
	if (k):
		print "\n"
	current = k
printCalendar(1, month, year)
