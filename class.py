import pandas as pd
import plotly.express as pe
import plotly.graph_objects as go
import statistics as st
import csv
import numpy as nu
import plotly.figure_factory as ff
import seaborn as sns 
import random

data = pd.read_csv("class.csv")

savingData = data["quant_saved"].tolist()
remAny = data["rem_any"].tolist()

total = len(savingData)

# ------------------------------ finding total no of people who were reminded and not reminded ----------------------------------------
peopleWhoReminded = 0

for i in remAny:
    if i == 1:
        peopleWhoReminded += 1

# print(peopleWhoReminded)

peopleWhoNotReminded = total - peopleWhoReminded

# print (peopleWhoNotReminded)

# -------------------------------------------- plotting the graph for rem and not rem --------------------------------------------------

fig = go.Figure(go.Bar(x =[ "peopleWhoReminded" , "peopleWhoNotReminded"] , y = [peopleWhoReminded , peopleWhoNotReminded] ))
# fig.show()

# --------------------------------------- mean/med/mode/stdev of all the data for everyone(savingsdata) ------------------------------------------------------
mean = st.mean(savingData)
median = st.median(savingData)
mode = st.mode(savingData)
stdev = st.stdev(savingData)

print("-------------------------------------------------------------------------------")

print("Mean of saving for everyone : " , mean)
print("Mode of saving for everyone : " , mode)
print("Median of saving for everyone : " , median)
print("Stdev of saving for everyone : " , stdev)


# --------------------------------------- mean/med/mode/stdev of people who were reminded ------------------------------------------------------

with open("class.csv") as f:
    r = csv.reader(f)
    savingsD = list(r)

savingsD.pop(0)

remindedSavings = []
notRemindedSavings = []

for i in savingsD:
    if int(i[3]) == 1:
        remindedSavings.append(float(i[0]))
    else :
        notRemindedSavings.append(float(i[0]))


meanR = st.mean(remindedSavings)
median = st.median(remindedSavings)
mode = st.mode(remindedSavings)
stdev = st.stdev(remindedSavings)

print("-------------------------------------------------------------------------------")
print("Mean of saving for those who were reminded : " , meanR)
print("Mode of saving for those who were reminded : " , mode)
print("Median of saving for those who were reminded : " , median)
print("Stdev of saving for those who were reminded : " , stdev)


# --------------------------------------- mean/med/mode/stdev of people who were not reminded ------------------------------------------------------

meanNR = st.mean(notRemindedSavings)
median = st.median(notRemindedSavings)
mode = st.mode(notRemindedSavings)
stdev = st.stdev(notRemindedSavings)

print("-------------------------------------------------------------------------------")
print("Mean of saving for those who were not reminded : " , meanNR)
print("Mode of saving for those who were not reminded : " , mode)
print("Median of saving for those who were not reminded : " , median)
print("Stdev of saving for those who were not reminded : " , stdev)



# ----------------------------------- finding correlation coeff in between age and savings -------------------------------------------

age = []
savings = []

savings = data["quant_saved"].tolist()
age = data["age"].tolist()

corcoef = nu.corrcoef(savings, age )
print("Correlation coeff in between age and savings : " , corcoef[0,1])



fig = ff.create_distplot([savingData], ["savings"] , show_hist=False)
# fig.show()

# ----------------------------------------------- data story 2 ----------------------------------------------



sns.boxplot(data = data , x = data["quant_saved"])

# --------------------------------------------------

q1 = data["quant_saved"].quantile(0.25)

q3 = data["quant_saved"].quantile(0.75)

iqr = q3 - q1

print("-----------------------------")
print("Q1 : " , q1)
print("Q3 : " , q3)
print("Interquartile Range : " , iqr)


lowerWhisker = q1 - 1.5*iqr
upperWhisker = q3 + 1.5*iqr

print("-----------------------------")
print("Lower Whisker : " , lowerWhisker)
print("Upper Whisker : " , upperWhisker)



newData = data[ data["quant_saved"] < upperWhisker ] 

newAllSavings = newData["quant_saved"].tolist()


print("-------------------------------------------------------------------------------")

print("Mean of saving for everyone (newdata) : " , st.mean(newAllSavings) )
print("Mode of saving for everyone (newdata)  : " , st.mode(newAllSavings))
print("Median of saving for everyone (newdata)  : " , st.median(newAllSavings))
print("Stdev of saving for everyone (newdata) : " , st.stdev(newAllSavings))


fig = ff.create_distplot([newAllSavings], ["savings"] , show_hist=False)
# fig.show()

# -----------------------------------------------Making bell curve----------------------------------------------

samplingMean = []

for i in range(1000):
    temp = []
    for j in range(100):
        temp.append(random.choice(newAllSavings))

    samplingMean.append( st.mean(temp)  )



meanOfSampleNewData = st.mean(samplingMean)

stdevOfSampleNewData = st.stdev(samplingMean)

print("----------------------------------------------------------------")


print("Mean of sample: " , meanOfSampleNewData)
print("Stdev of sample : " , stdevOfSampleNewData)



fig = ff.create_distplot([samplingMean], ["savings"] , show_hist=False)
fig.show()

print("----------------------------------------------------------------")

tempData = newData[newData.age != 0]


savings = tempData["quant_saved"].tolist()
age = tempData["age"].tolist()

corcoef = nu.corrcoef(savings, age )
print("Correlation coeff in between age and savings : " , corcoef[0,1])


# ---------------------------------------------------------------------------------------------------






