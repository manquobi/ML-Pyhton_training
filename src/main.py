import os
os.system('cls' if os.name == 'nt' else 'clear')

import sys
import matplotlib
#matplotlib.use('Agg')

import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("data/dt.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df) 

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features) 

#plt.savefig('decision_tree.png')
#sys.stdout.flush()
plt.show()  # This will display the plot in VS Code

print(dtree.predict([[40, 10, 7, 1]])) 

 





