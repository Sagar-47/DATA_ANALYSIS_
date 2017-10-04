import pandas as pd
import array as arr
import numpy as np
import dis
import matplotlib.pyplot as plt
data=pd.read_excel('facebookdata.xls')
likes=data['likes'].values
friends=data['friends'].values
posts=data['posts'].values
#calc for average and standard deviation
al=np.average(likes)
af=np.average(friends)
ap=np.average(posts)
sl=np.std(likes)
sf=np.std(friends)
sp=np.std(posts)
#print(al,af,ap,sl,sf,sp)
#hist for number of likes
f1=plt.figure(1)
tx1=f1.add_subplot(111)
f1.subplots_adjust(top=0.85)
tx1.text(350,400,r'Average=%s'%(al),fontsize=10)
tx1.text(350,380,r'Standard deviation=%s'%(sl),fontsize=8)
plt.hist(likes,bins=60,histtype= 'bar', rwidth=0.6)
plt.xlabel('No. of likes')
plt.ylabel('Count')
plt.title('Number of likes')
plt.show()
#hist for number of friends
f2=plt.figure(2)
tx2=f2.add_subplot(111)
f2.subplots_adjust(top=0.85)
tx2.text(900,850,r'Average=%s'%(af),fontsize=10)
tx2.text(850,800,r'Standard deviation=%s'%(sf),fontsize=8)
plt.hist(friends,bins=30,histtype='bar',rwidth=0.6)
plt.xlabel('No. of friends')
plt.ylabel('Count')
plt.title('Number of friends')
plt.show()
#hist for number of posts
f3=plt.figure(3)
tx3=f3.add_subplot(111)
f3.subplots_adjust(top=0.85)
tx3.text(130,1200,r'Average=%s'%(ap),fontsize=10)
tx3.text(125,1100,r'Standard deviation=%s'%(sp),fontsize=8)
plt.hist(posts,bins=20, histtype='bar',rwidth=0.6)
plt.xlabel('No. of posts')
plt.ylabel('Count')
plt.title('Number of posts')
plt.show()
