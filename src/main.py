import os
os.system('cls' if os.name == 'nt' else 'clear')

import numpy
from sklearn import metrics
import matplotlib.pyplot as plt


actual = numpy.random.binomial(1, 0.9, size = 1000)
predicted = numpy.random.binomial(1, 0.9, size = 1000) 
#confusion_matrix = metrics.confusion_matrix(actual, predicted) 
#cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

#cm_display.plot()
#plt.show() 
Accuracy = metrics.accuracy_score(actual, predicted)    # True Positive + True Negative) / Total Predictions
Precision = metrics.precision_score(actual, predicted)  # True Positive / (True Positive + False Positive) 
Sensitivity_recall = metrics.recall_score(actual, predicted) # True Positive / (True Positive + False Negative)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)  #True Negative / (True Negative + False Positive)
F1_score = metrics.f1_score(actual, predicted) #2 * ((Precision * Sensitivity) / (Precision + Sensitivity))

#print({"Accuracy: " Accuracy,"Precision: " Precision,"Sensitivity_recall: " Sensitivity_recall,"Specificity: " Specificity,"F1_score: " F1_score})
print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score}) #look into this