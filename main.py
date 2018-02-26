#Machine learning to predict what should be for dinner

from sklearn import tree
from datetime import datetime
import time

date_format = "%d/%m/%Y"
dayFile = open("days.txt", "r")
days = []
for line in dayFile:
	days.append(line.replace('\n',''))
dayFile.close()
#print days
diffDays = []
for day in days:
	
	listDay = datetime.strptime(time.strftime("%d/%m/%Y"), date_format)
	currDay = datetime.strptime(day, date_format)
	#diffDays becomes a list of no. days since date in days (so changes every day)
	diffDays.append((listDay-currDay).days)
	
mealFile = open("meals.txt", "r")
meals = []
for line in mealFile:
	meals.append(line.replace('\n',''))
mealFile.close()

'''
predictionResults = [] #This should be made ofcourse

print "Top predictions are"
print "1.",predictionResults[0]
print "2.",predictionResults[1]
print "3.",predictionResults[2]
'''

print "Top predictions are"
print "1.",meals[0]
print "2.",meals[1]
#print "3.",meals[2]
choice = input("Which of these are you eating tonight? If none press 0.\n")
dayFile = open("days.txt", "a")
mealFile = open("meals.txt", "a")

if (choice <4 and choice >0):
	#add the chosen meal to the meals files
	#mealFile.write(predictionResults[choice-1])
	mealFile.write(meals[choice-1])
	mealFile.write("\n")
	#add the current date to the dates files
	today = time.strftime("%d/%m/%Y")
	dayFile.write(today)
	dayFile.write("\n")

if (choice == 0):
	newMeal = raw_input("What will you be eating tonight?\n")
	newMeal = newMeal.lower()
	mealFile.write(newMeal)
	mealFile.write("\n")
	today = time.strftime("%d/%m/%Y")
	dayFile.write(today)
	dayFile.write("\n")
dayFile.close()
mealFile.close()

