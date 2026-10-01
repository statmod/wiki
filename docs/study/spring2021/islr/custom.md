---
title: "Персональные задания по курсу \"Интеллектуальный анализ данных\""
---

## Робастная регрессия

 Задание было дано


## Классификация

 Using the Auto data set, fit classification models in order to predict whether a given auto has the mileage per gallon above or below the median. Explore logistic regression, LDA, and QDA models using various subsets of the predictors. Describe your findings.


## Регуляризация

 We have seen that as the number of features used in a model increases, the training error will necessarily decrease, but the test error may not.

1.  Generate a data set with some number of features and n = 5000 observations, and an associated quantitative response vector generated via the linear model with some coefficients set exactly to zero.
2.  Split your data set into a training set containing 500 observations and a test set containing 4500 observations.
3.  Perform best subset selection on the training set, and plot the training set MSE associated with the best model of each size.
4.  Plot the test set MSE associated with the best model of each size.
5.  For which model size does the test set MSE take on its minimum value? Comment on your results. If it takes on its minimum value for a model containing only an intercept or a model containing all of the features, then play around with the way that you are generating the data until you come up with a scenario in which the test set MSE is minimized for an intermediate model size.
6.  How does the model at which the test set MSE is minimized compare to the true model used to generate the data? Comment on the coefficient values.
7.  Study the MSE for the coefficient estimates. Compare with the MSE of the model fit. Explain your findings.


## Деревья

 Apply boosting, bagging, and random forests to a data set of your choice. Be sure to fit the models on a training set and to evaluate their performance on a test set. How accurate are the results compared to simple methods like linear or logistic regression? Which of these approaches yields the best performance? Justify your choice of the dataset. Report the most significant features (where possible). Compare with the results obtained using regularization.


## SVM


1.  Generate a simulated two-class data set with 100 observations and two features in which there is a visible but non-linear separation between the two classes. Show that in this setting, a support vector machine with a polynomial kernel (with degree greater than 1) or a radial kernel will outperform a support vector classifier on the training data. Which technique performs best on the test data? Make plots and report training and test error rates in order to back up your assertions.
2.  Do the same, but now build an example where radial kernel outperforms a polynomial one. Explain your findings.