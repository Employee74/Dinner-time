#Machine learning to predict what should be for dinner

from sklearn import tree
from datetime import datetime
import time

date_format = "%d/%m/%Y"
days = ['25/2/2018', '24/2/2018']
diffDays = []
for day in days:
	
	listDay = datetime.strptime(time.strftime("%d/%m/%Y"), date_format)
	currDay = datetime.strptime(day, date_format)
	#diffDays becomes a list of no. days since date in days (so changes every day)
	diffDays.append((listDay-currDay).days)
	
meals = ['pizza', 'shoarma']

meals.reshape(-1,1)
diffDays.reshape(-1,1)

clf = tree.DecisionTreeClassifier()

clf = clf.fit(diffDays,meals)

prediction = clf.predict(0)

print prediction
