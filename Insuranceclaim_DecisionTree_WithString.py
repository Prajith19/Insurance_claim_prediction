import pandas as pd
import numpy as np
df = pd.read_csv("D:/testing.csv")

indep = df.drop('insuranceclaim',axis='columns')

dept = df['insuranceclaim']

from sklearn.preprocessing import LabelEncoder
la_heartproblem=LabelEncoder()
indep['heartproblem_n']=la_heartproblem.fit_transform(indep['heartproblem'])

Indep_n = indep.drop('heartproblem',axis='columns')

from sklearn import tree
model=tree.DecisionTreeClassifier()

model.fit(Indep_n,dept)
model.score(Indep_n,dept)

from sklearn import tree
import matplotlib.pyplot as plt
fig = fig = plt.figure(figsize=(100,50))
print(tree.plot_tree((model),filled=1))
print("                             ")

print("Give the inputs as per the example, use only LOWERCASE")
age_in = int(input("Enter your age (eg: 19,56): "))
sex_in = input("Mention your sex (eg: male, female): ")
bmi_in = float(input("Enter your bmi (eg: 27.9,39.22): "))
steps_in = int(input("Mention the average steps you walk in a day (eg: 3009,10478): "))
children_in = int(input("Mention number of children you have (eg: 0,2,1): "))
smoker_in = input("Mention whether you are smoker are not (eg: no,yes): " )
region_in = input("Choose from the mentioned region (eg: chennai,kanchipuram,thiruvallur,trichy): ")
charges_in = float(input("Enter the amount you want to claim (eg: 12345,5678): "))
heartproblem_n_in =input("Enter the risk of your heart problem (eg: high,low,medium): ")
h_prob_list = [heartproblem_n_in]
sex_prob_list = [sex_in]
smoker_prob_list = [smoker_in]
region_prob_list = [region_in]

h_prob = 0
sex_prob = 0
smoker_prob = 0
region_prob = 0

for heart_d in h_prob_list:
    if heart_d == "high":
        h_prob = 0
    elif heart_d == "low":
        h_prob = 1
    elif heart_d == "medium":
        h_prob = 2
    else:   
        h_prob = 100
for sex_d in sex_prob_list:
    if sex_d == "male":
        sex_prob = 0    
    elif sex_d == "female":
        sex_prob = 1
    else:
        sex_prob = 100
for smoke_d in smoker_prob_list:
    if smoke_d == "no":
        smoker_prob = 0
    elif smoke_d == "yes":
        smoker_prob = 1
    else:
        smoker_prob = 100
for region_d in region_prob_list:
    if region_d == "chennai":
        region_prob = 0
    elif region_d == "kanchipuram":
        region_prob = 1
    elif region_d == "thiruvallur":
        region_prob = 2
    elif region_d == "trichy":
        region_prob = 3
    else:
        region_prob = 100
print("              ")
print(f'\nYour age is:- {age_in}')
sex_list = [sex_prob]
for sex in sex_list:
  if sex == 0:
     print("Mentioned sex is:- Male")
  if sex == 1:
    print("Mentioned sex is:- Female")
  if sex == 100:
    print("Please mention correct sex (your prediction is wrong)")
print(f'Your bmi is:- {bmi_in}')
print(f'Your average steps in a day:- {steps_in}')
print(f'Mentioned number of children: {children_in}')
smoker_list = [smoker_prob]
for smoker in smoker_list:
    if smoker == 0:
      print("Are you a smoker:- No")
    if smoker == 1:
      print("Are you a smoker:- Yes")
    if smoker == 100:
      print("Please enter yes or no in smoker (your prediction is wrong)")
region_list = [region_prob]
for region in region_list:
    if region == 0:
        print("Mentioned Region is:- Chennai")
    if region == 1:
        print("Mentioned Region is:- Kanchipuram")
    if region == 2:
        print("Mentioned region is:- Thiruvallur")
    if region == 3:
        print("Mentioned region is:- Trichy")
    if region == 100:
        print(f'{region_in} region is not covered.(your prediction is wrong)')
print(f'Mentioned charges is:- {charges_in}')
h_list = [h_prob]
for h_risk in h_list:
    if h_risk == 0:
        print("Your heart problem risk rate is:- High")
    if h_risk == 1:
        print("Your heart problem risk rate is:- Low")
    if h_risk == 2:
        print("Your heart problem risk rate is:- Medium")
    if h_risk == 100:
        print("Mention whether your heart attack risk is high, medium or low (your prediction is wrong)" )

insurance = model.predict([[age_in,sex_prob,bmi_in,steps_in,children_in,smoker_prob,region_prob,charges_in,h_prob]])
print("     ")
if insurance == [0]:
    print("Description:- Your insurance amount is NOT CLAIMABLE")
if insurance == [1]:
    print("Description:- Your insurnace amount is CLAIMABLE")