import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

root = "./"

x = []
y = []

with open('data.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter=",")
     for row in plots:
         x.append(float(row[0]))
         y.append(float(row[1]))

plt.scatter(x,y, label='Liers Data Frame')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
plt.show()