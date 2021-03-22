#program to tell user thier 100th year 

from datetime import date #to import date time class 

name=input("Enter your Name");
age=int(input("Enter your Current Age"));

currentYear=date.today().year;

hyrs=(currentYear-age)+100;

print("You will be of 100 years in "+ str(hyrs));