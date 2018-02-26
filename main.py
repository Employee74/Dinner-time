#Machine learning to predict what should be for dinner

from sklearn import tree
from datetime import datetime
import time

date_format = "%d/%m/%Y"
a = datetime.strptime('25/2/2018', date_format)
b = datetime.strptime('26/2/2018', date_format)

days = ['25/2/2018', '24/2/2018']
dtDays = []
diffDays = []
for day in days:
	dtDays = datetime.strptime(day, date_format)
	print datetime.strptime(day, date_format) - datetime.strptime(time.strftime("%d/%m/%Y",date_format)
#for day in dtDays:
#	diffDays = day - datetime.date.today() 
#print diffDays

