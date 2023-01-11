import pandas as pd
import numpy as np

df = pd.read_csv("D:/decision.csv")

indep = df.drop('insuranceclaim',axis='columns')
dept = df['insuranceclaim']

from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(indep,dept)
model.score(indep,dept)

from sklearn import tree
import matplotlib.pyplot as plt
fig = fig = plt.figure(figsize=(100,50))
print(tree.plot_tree((model),filled=1))
print("                     ")
age_in = int(input("Enter your age (eg: 19,56): "))
sex_in = int(input("Mention your sex (eg: 0-male, 1-female): "))
bmi_in = float(input("Enter your bmi (eg: 27.9,39.22): "))
steps_in = int(input("Mention the average steps you walk in a day (eg: 3009,10478): "))
children_in = int(input("Mention number of children you have (eg: 0,2,1): "))
smoker_in = int(input("Mention whether you are smoker are not (eg: 0-no, 1-yes): " ))
region_in = int(input("Enter your region number (eg: 0-Chennai,1-Kanchipuram,2-Thiruvallur,3-Trichy): "))
charges_in = float(input("Enter the amount you want to claim (eg: 12345,5678): "))
sex_list = [sex_in]
smoker_list = [smoker_in]
region_list = [region_in]
print("                      ")
print(f'\nYour age is:- {age_in}')
for sex in sex_list:
  if sex == 0:
     print("Mentioned sex is:- Male")
  if sex == 1:
    print("Mentioned sex is:- Female")
  if sex > 1:
    print("Please mention correct sex (your prediction is wrong)")
print(f'Your bmi is:- {bmi_in}')
print(f'Your average steps in a day:- {steps_in}')
print(f'Mentioned number of children: {children_in}')
for smoker in smoker_list:
    if smoker == 0:
      print("Are you a smoker:- No")
    if smoker == 1:
      print("Are you a smoker:- Yes")
    if smoker > 1:
      print("Please enter 0 or 1 in smoker (your prediction is wrong)")
for region in region_list:
    if region == 0:
        print("Mentioned Region is:- Chennai")
    if region == 1:
        print("Mentioned Region is:- Kanchipuram")
    if region == 2:
        print("Mentioned region is:- Thiruvallur")
    if region == 3:
        print("Mentioned region is:- Trichy")
    if region > 3:
        print("Please mention the correct region (your prediction is wrong)")
print(f'Mentioned charges is:- {charges_in}')

insurance = model.predict([[age_in,sex_in,bmi_in,steps_in,children_in,smoker_in,region_in,charges_in]])
print("     ")
if insurance == [0]:
    print("Description:- Your insurance amount is NOT CLAIMABLE")
if insurance == [1]:
    print("Description:- Your insurnace amount is CLAIMABLE")

    





