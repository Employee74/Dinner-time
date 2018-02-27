#Machine learning to predict what should be for dinner

from sklearn.svm import SVR
from datetime import datetime
import time
import numpy as np
import matplotlib.pyplot as plt

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

def predict_meal(dates,meals,x):
	diffDays = np.reshape(dates,len(dates), 1)
	svr_lin = SVR(kernel= 'linear', C=1e3)
	svr_poly = SVR(kernel = 'poly', C=1e3, degree = 2)
	svr_rbf = SVR(kernel = 'rbf', C=1e3, gamma =0.1)
	svr_lin.fit(diffDays, meals)
	svr_poly.fit(diffDays,meals)
	svr_rbf.fit(diffDays,meals)
	"""
	plt.scatter(diffDays,meals, color = 'black', label = 'Data')
	plt.plot(diffDays, svr_rbf.predict(days), color = 'red', label = 'RBF model')
	plt.plot(diffDays, svr_lin.predict(days), color = 'green', label = 'Linear model')
	plt.plot(diffDays, svr_poly.predict(days), color = 'blue', label = 'Polynomial model')
	plt.xlabel("Days")
	plt.ylabel("Meals")
	plt.title("SVM meals")
	plt.legend()
	plt.show()
	"""
	return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0]
	
predicted_meal = predict_meal(diffDays,meals,29)

print(predicted_meal)

print ("Top predictions are")
print ("1.",meals[0])
print ("2.",meals[1])
print ("3.",meals[2])
choice = int( input("Which of these are you eating tonight? If none press 0.\n"))
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
	newMeal = input("What will you be eating tonight?\n")
	newMeal = newMeal.lower()
	mealFile.write(newMeal)
	mealFile.write("\n")
	today = time.strftime("%d/%m/%Y")
	dayFile.write(today)
	dayFile.write("\n")
dayFile.close()
mealFile.close()

