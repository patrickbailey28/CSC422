import numpy as nm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import tree
import matplotlib.pyplot as plt

A = nm.loadtxt(open("adultProcessed.csv", "rb"), delimiter=",", skiprows=1)

X = A[:, 0:11]
Y = A[:, 11]
Y = Y.reshape((-1, 1))
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state=5)

depths = [2,3,5,8,10,11,12,13,14,15,17,20,25]
trainingErrors = []
testingErrors = []
error = 1
depth = 0
for x in depths:
    gini = DecisionTreeClassifier(criterion = "gini", max_depth=x, random_state=5, min_samples_leaf=25)
    gini.fit(X_train, y_train)
    #tree.export_graphviz(decision_tree=gini, out_file="tree.dot")
    y_trainPred = gini.predict(X_train)
    trainingErrors.append(1 - accuracy_score(y_train, y_trainPred))
    y_pred = gini.predict(X_test)
    testingError = 1 - accuracy_score(y_test, y_pred)
    testingErrors.append(testingError)
    if(error > testingError):
        error = testingError
        depth = x
#print(error)
#print(depth)
plt.plot(depths, trainingErrors, label='Training')
plt.plot(depths, testingErrors, label='Testing')
plt.xlabel('Max Depth of Decision Tree')
plt.ylabel('Error')
plt.title('Gini Index: Max Depth vs. Error')
plt.legend()
#plt.show()

gini = DecisionTreeClassifier(criterion = "gini", max_depth=depth, random_state=5, min_samples_leaf=25)
gini.fit(X_train, y_train)
#tree.export_graphviz(decision_tree=entropy, out_file="tree.dot")
y_trainPred = gini.predict(X_train)
trainingErrors.append(1 - accuracy_score(y_train, y_trainPred))
y_pred = gini.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test,y_pred))
testingErrors.append(1 - accuracy_score(y_test, y_pred))
#print(entropy.max_features_)

trainingErrors = []
testingErrors = []
error = 1
depth = 0
for x in depths:
    entropy = DecisionTreeClassifier(criterion = "entropy", max_depth=x, random_state=5, min_samples_leaf=25)
    entropy.fit(X_train, y_train)
    #tree.export_graphviz(decision_tree=entropy, out_file="tree.dot")
    y_trainPred = entropy.predict(X_train)
    trainingErrors.append(1 - accuracy_score(y_train, y_trainPred))
    y_pred = entropy.predict(X_test)
    testingError = 1 - accuracy_score(y_test, y_pred)
    testingErrors.append(testingError)
    if (error > testingError):
        error = testingError
        depth = x
plt.plot(depths, trainingErrors, label='Training')
plt.plot(depths, testingErrors, label='Testing')
plt.xlabel('Max Depth of Decision Tree')
plt.ylabel('Error')
plt.title('Information Gain: Max Depth vs. Error')
plt.legend()
#plt.show()
#print(error)
#print(depth)

entropy = DecisionTreeClassifier(criterion = "entropy", max_depth=depth, random_state=5, min_samples_leaf=25)
entropy.fit(X_train, y_train)
tree.export_graphviz(decision_tree=entropy, out_file="tree.dot")
y_trainPred = entropy.predict(X_train)
trainingErrors.append(1 - accuracy_score(y_train, y_trainPred))
y_pred = entropy.predict(X_test)
#print(1 - accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test,y_pred))
testingErrors.append(1 - accuracy_score(y_test, y_pred))
#print(entropy.max_features_)
