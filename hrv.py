import ijson
import matplotlib.pyplot as plt

filename = 'hr_data.json'

with open( filename , 'r') as f:
    objects = ijson.items(f,'item')
    columns = list(objects)

interval = []

for i ,j in  enumerate(columns):
   interval.append(float(columns[i]['RRInterval'])/1000)

print(interval)

plt.hist(interval, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel("RRInterval in Milliseconds")
plt.show()













