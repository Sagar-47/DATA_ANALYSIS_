import pandas as pd
import array as arr
import numpy as np
import matplotlib.pyplot as plt
raw_data=pd.read_table('Complete_TAVG_daily.txt', sep='\s+',comment='%') 
numpy_array=raw_data.values 
tfix= lambda t : t + 8.68
vtfix=np.vectorize(tfix)
ncolumn = vtfix(numpy_array[:,5])
reshapencolumn= np.reshape(ncolumn, (ncolumn.size,1))
total_data=np.append(numpy_array,reshapencolumn,axis=1)
year= input("enter the year:")
def f(a):
	i=1
	current_row=0
	row_start=0
	row_end=0
	while i>0:
		if (total_data[current_row][1]== a)and (row_start==0):
				row_start=current_row
		
		if (total_data[current_row][1]!= a) and (row_start!=0):	
	    		row_end=current_row-1
	    		break
		current_row=current_row+1	
	required_data=total_data[row_start : row_end+1,6] 	
	plt.xlabel('Temperature in degree Celsius')
	plt.ylabel('No. of days')
	plt.title("Average Temperature Distribution for 2012")
	plt.hist(required_data, bins=15, histtype='bar',rwidth=0.8)
	plt.show()
f(year)