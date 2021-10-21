import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv('shows.csv')
print(df)
print('=========================================================')
###################
n = {'UK' : 0,'USA' : 1,'N' : 2}
df['Nationality'] = df['Nationality'].map(n)
g = {'YES' : 1,'NO' : 0}
df['GO'] = df['GO'].map(g)
print(df)
print('=========================================================')
########
features = ['Age','Experience','Rank','Nationality']
X = df[features]
y = df['GO']
print(X)
print(y) 
print('=========================================================')
#########
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
