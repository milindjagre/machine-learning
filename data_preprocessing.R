#  DATA PREPROCESSING

# setting the working directory
setwd("C:\\Users\\User\\Desktop\\blog\\3 ML Data Preprocessing\\R")

# IMPORTING THE DATASET
dataset = read.csv("Data.csv")
# viewing the imported dataset
View(dataset)

#IMPUTING THE MISSING DATA
# replacing NULL in Age with the mean of Age
dataset$Age = ifelse(is.na(dataset$Age) , mean(dataset$Age, na.rm=TRUE), dataset$Age)
# replacing NULL in Salary with the mean of Salary
dataset$Salary = ifelse(is.na(dataset$Salary) , mean(dataset$Salary, na.rm=TRUE), dataset$Salary)
# viewing the dataset for confirmation
View(dataset)

# CONVERSION OF CATEGORICAL DATA
# factor() is used for creating the DUMMY VARIABLES in R
# converting categorical Country variable in to continuous variable
dataset$Country = factor( x = dataset$Country, 
                          levels = c('France', 'Spain', 'Germany'), 
                          labels = c(1, 2, 3) )
# converting categorical Purchased variable in to continuous variable
dataset$Purchased = factor( x = dataset$Purchased, 
                            levels = c('No', 'Yes'), 
                            labels = c(0, 1) )
# viewing the dataset for confirmation
View(dataset)

# SPLITTING DATASET INTO TRAINING AND TEST SET
# we are going to use caTools library for doing this
# installing the library caTools
install.packages("caTools")
# loading the library in R workspace
library(caTools)
# creating the samples split ration for test and train data
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# creating the training set
training_set = subset(dataset , split == TRUE)
# creating the testing set
test_set = subset(dataset , split == FALSE)
# viewing the training set for confirmation
View(training_set)
# viewing the test set for confirmation
View(test_set)

# FEATURE SCALING
# scale() function is used for doing feature scaling
# doing feature scaling for training set
training_set[, c(2,3)] = scale(training_set[, c(2,3)])
# doing feature scaling for test set
test_set[, c(2,3)] = scale(test_set[, c(2,3)])
# viewing the training set for confirmation
View(training_set)
# viewing the test set for confirmation
View(test_set)
