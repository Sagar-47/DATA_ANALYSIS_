import pandas as pd
import array as arr
import numpy as np
import matplotlib.pyplot as plt
#Reading data from file into a numpy array
raw_data=pd.read_table('Complete_TAVG_daily.txt', sep='\s+',comment='%')
numpy_array=raw_data.values 
#Adding a new column containing avarage temperature
tfix= lambda t : t + 8.68
vtfix=np.vectorize(tfix)
ncolumn = vtfix(numpy_array[:,5])
reshapencolumn= np.reshape(ncolumn, (ncolumn.size,1))
total_data=np.append(numpy_array,reshapencolumn,axis=1)
#Calculating average and standard deviation for the required years
i=1
current_row=0
row_start=0
row_end=0
required_data=arr.array('d')
year=arr.array('d')
avg_temp=arr.array('d')
std_dev=arr.array('d')
a=1880
while a<=2014:
 if (a%3==0):
   while i>0 :
       if (total_data[current_row][1]== a)and (row_start==0):
           row_start=current_row
       if (total_data[current_row][1]!= a) and (row_start!=0):
           row_end=current_row-1
           break
       current_row=current_row+1	
   required_data=np.append(required_data,total_data[row_start : row_end+1,6],axis=0)
   avg=sum(required_data)/len(required_data)
   std_dev.append(np.std(required_data))
   year.append(a)
   avg_temp.append(avg)
   required_data=arr.array('d')
   current_row=0
   row_start=0
   row_end=0
 a=a+1
 #Plotting the extracted as a scatter plot
plt.plot(year,avg_temp,label="x")
plt.scatter(year,avg_temp,label="x",color='g')
plt.legend(["line","scatter"])
plt.xlabel("Year")
plt.ylabel("Average Temperature in degree Celsius")
plt.title("Plot of Average Temperature of every third year from 1880 to 2014")
plt.show()
#Plotting the error bars using above calculated standard deviations
plt.errorbar(year, avg_temp, yerr=std_dev, xerr=None, ecolor= 'r', elinewidth=1)
plt.legend(["error bars"],loc=2)
plt.xlabel("Year")
plt.ylabel("Average Temperature in degree Celsius")
plt.title("Error Bar Plot of Average Temperature of every third year from 1880 to 2014")
plt.show()





