import pandas as pd
import array as arr
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
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
inv_std_dev=arr.array('d')
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
   avg=sum(required_data)/len(required_data) #calculates average temperature for the year
   std_dev.append(np.std(required_data)/np.sqrt(len(required_data)-1)) #calculates uncertainty in avg temp
   inv_std_dev.append(np.sqrt(len(required_data)-1)/np.std(required_data)) #1/(uncertainty in avg temp) for input into polyplot
   year.append(a)
   avg_temp.append(avg)
   required_data=arr.array('d')
   current_row=0
   row_start=0
   row_end=0
 a=a+1

#Plotting the error bars using above calculated standard deviations 
plt.errorbar(year, avg_temp, yerr=std_dev, xerr=None, ecolor= 'r',fmt='o',markersize=1)
#X2 function for line
def X2_line(m,c):
	y=0
	for i in range(0,len(year)): 
		y=(((avg_temp[i]-(m*year[i])-c)*inv_std_dev[i])**(2) + y)
	return y

#Calculating coefficients of X2 differentiated wrt m for line
def X2_line_diffm_m():
       	y=0
	for i in range(0,len(year)): 
		y=((year[i]*inv_std_dev[i])**(2))+y
	return y
def X2_line_diffm_c():
       	y=0
	for i in range(0,len(year)): 
		y=(year[i]*(inv_std_dev[i])**(2))+y
	return y
        
def X2_line_diffm_const():
       	y=0
	for i in range(0,len(year)): 
		y=((year[i])*(avg_temp[i])*(inv_std_dev[i])**(2))+y
	return y
#Calculating coefficients of X2 differentiated wrt c for line
def X2_line_diffc_m():
       	y=0
	for i in range(0,len(year)): 
		y=((year[i])*(inv_std_dev[i])**(2))+y
	return y
def X2_line_diffc_c():
       	y=0
	for i in range(0,len(year)): 
		y=((inv_std_dev[i])**(2))+y
	return y
def X2_line_diffc_const():
       	y=0
	for i in range(0,len(year)): 
		y=((avg_temp[i])*(inv_std_dev[i])**(2))+y
	return y
#Solving above linear equations for m,c
coeff_matrix=np.array([[X2_line_diffm_m(),X2_line_diffm_c()],[X2_line_diffc_m(),X2_line_diffc_c()]])
const_matrix=np.array([X2_line_diffm_const(),X2_line_diffc_const()])
bestfit_line=np.linalg.solve(coeff_matrix,const_matrix)

poly1d_line=np.poly1d(bestfit_line)
print(poly1d_line)

#function to calculate temp as linear function of year
def temp_line(year):
	return poly1d_line(year)
plt.plot(year, temp_line(year), 'b-')
degfrdm_line=len(year)-2
#x2 per degree of freedom
x2_per_degfrdm_line= X2_line(bestfit_line[0],bestfit_line[1])/degfrdm_line
print(x2_per_degfrdm_line )

#plot best fit line
plt.legend(["error bars"],loc=2)
plt.xlabel("Year")
plt.ylabel("Average Temperature in degree Celsius")
plt.title("Error Bar Plot and Best fit line of Average Temperature of every third year from 1880 to 2014")
plt.show()


plt.errorbar(year, avg_temp, yerr=std_dev, xerr=None, ecolor= 'r',fmt='o',markersize=1)
 
#X2 differentiated wrt a for quadratic curve
def X2_quad_diffa(a,b,c):
       	y=0
	for i in range(0,len(year)): 
		y=((avg_temp[i]-(a*year[i])**(2)-(b*year[i])-c)*(inv_std_dev[i]*year[i])**(2)) + y
	return y
def X2_quad_diffb(a,b,c):
       	y=0
	for i in range(0,len(year)): 
		y=((avg_temp[i]-(a*year[i])**(2)-(b*year[i])-c)*(inv_std_dev[i])**(2)*year[i]) + y
	return y
def X2_quad_diffc(a,b,c):
       	y=0
	for i in range(0,len(year)): 
		y=((avg_temp[i]-(a*year[i])**(2)-(b*year[i])-c)*(inv_std_dev[i])**(2)) + y
	return y
#calculating best fit values of parameters a,b,c for quadratic polynomial by solving above linear equations
coeff_matrix_quad=np.array([[X2_quad_diffa(1,0,0)-X2_quad_diffa(0,0,0),X2_quad_diffa(0,1,0)-X2_quad_diffa(0,0,0),X2_quad_diffa(0,0,1)-X2_quad_diffa(0,0,0)],[X2_quad_diffb(1,0,0)-X2_quad_diffb(0,0,0),X2_quad_diffb(0,1,0)-X2_quad_diffb(0,0,0),X2_quad_diffb(0,0,1)-X2_quad_diffb(0,0,0)],[X2_quad_diffc(1,0,0)-X2_quad_diffc(0,0,0),X2_quad_diffc(0,1,0)-X2_quad_diffc(0,0,0),X2_quad_diffc(0,0,1)-X2_quad_diffc(0,0,0)]])
const_matrix_quad=np.array([-X2_quad_diffa(0,0,0),-X2_quad_diffb(0,0,0),-X2_quad_diffc(0,0,0)])
bestfit_quad=np.linalg.solve(coeff_matrix_quad,const_matrix_quad)

#function to calculate temp as quadratic function of year
def temp_quad(year):
	return poly1d_quad(year)
poly1d_quad=np.poly1d(bestfit_quad)
#plot best fit quadratic curve
plt.plot(year, temp_quad(year), 'b-')
#X2 function for quad curve
def X2_quad(a,b,c):
	y=0
	for i in range(0,len(year)): 
		y=(((avg_temp[i]-(a*year[i])**(2)-(b*year[i])-c)*inv_std_dev[i])**(2) + y)
	return y 
degfrdm_quad=len(year)-3

#x2 per degree of freedom
x2_per_degfrdm_quad= X2_quad(bestfit_quad[0],bestfit_quad[1],bestfit_quad[2])/degfrdm_quad
print(x2_per_degfrdm_quad)
print(poly1d_quad)
plt.legend(["error bars"],loc=2)
plt.xlabel("Year")
plt.ylabel("Average Temperature in degree Celsius")
plt.title("Error Bar Plot and Best fit quadratic curve of Average Temperature of every third year from 1880 to 2014")
plt.show()

#contours of X2
m=np.linspace(-100,100 ,1000)
c=np.linspace(-100, 100, 1000)
X2=X2_line(bestfit_line[0],bestfit_line[1])
M, C = np.meshgrid(m,c)
CS=plt.contour(M,C,X2_line(M,C), colours='k')
CB = plt.colorbar(CS, shrink=0.8, extend='both')
plt.flag()
plt.xlabel("m")
plt.ylabel("c")
plt.title("Contours of X2 as function of m and c")
plt.show()

#X2 at c=c_bestfit
plt.plot(m,X2_line(m,bestfit_line[1]), 'b-'),
plt.xlabel("m")
plt.ylabel("X2")
plt.title("X2 as function of m at c_bestfit")
plt.show()

#X2 at m=m_bestfit
plt.plot(c,X2_line(bestfit_line[0],c), 'b-'),
plt.xlabel("c")
plt.ylabel("X2")
plt.title("X2 as function of c at m_bestfit")
plt.show()
