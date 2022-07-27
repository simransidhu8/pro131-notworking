import csv
import pandas as pd

#read data file
df = pd.read_csv("main.csv")

radius = []
mass = []
gravity = []

#moving data into arrays
radius.append(df['Radius'])
mass.append(df['Mass'])

#converting measurements into SI units
def convert_to_si(radius, mass):
    for i in range(0, len(radius)-1):
        #converting mass into kilograms
        mass[i] = mass[i]*1989e+30

        #converting radius into meters
        radius[i] = radius[i]*6957e+8

convert_to_si(radius, mass)

#creating function to find gravity
def find_gravity(radius, mass):
    G = 6.67e-11
    #calculating gravity and adding it into gravity array
    for x in range(0, len(mass)):
        print('about to read')
        g = G*(mass[x]) / ((radius[x])**2) 
        print('read')
        gravity.append(g)

find_gravity(radius, mass)

#merging gravity data with column
#df["Gravity"] = gravity

#creating new data file
#df.to_csv('star_data_with_gravity.csv')