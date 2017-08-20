import pandas as pd
import array as arr
import numpy as np
import dis
import matplotlib.pyplot as plt
raw_data=pd.read_table('Complete_TAVG_daily.txt', sep='\s+',comment='%')
numpy_array=raw_data.values 
tfix= lambda t : t + 8.68
vtfix=np.vectorize(tfix)
ncolumn = vtfix(ar[:,5])
reshapencolumn= np.reshape(ncolumn, (ncolumn.size,1))
total_data=np.append(numpy_array,reshapencolumn,axis=1)
year= input("enter the year:")
def graphing(a):
	i=1
	current_row=0
	row_start=0
	row_end=0
	required_data=arr.array('d')
	while i>0: #goes through all the days and checks for the condition
		if (total_data[current_row][1]== a) and ((total_data[current_row][3]== 1) or (total_data[current_row][3]==15)):
				row_start=current_row
				required_data.append(total_data[current_row][6])
		
		if (total_data[current_row][1]!= a) and (row_start!=0):	
	    		break
		current_row=current_row+1	 	
	plt.xlabel("Temperature in degree Celsius")
	plt.ylabel('No. of days')
	plt.title("Average Temperature Distribution for the 1st and 15th each month of 1912")
	plt.hist(required_data, bins=7, histtype='bar',rwidth=0.3)
	plt.show()
graphing(year)
