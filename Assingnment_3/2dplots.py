import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

data= pd.read_csv('facebookdata.csv')
#get value of respective columns
likes=data['likes'].values
posts=data['posts'].values
friends=data['friends'].values

plt.figure(1)
plt.hist2d(friends, posts,bins=30)
plt.xlabel("Number of friends")
plt.ylabel('Number of posts')
plt.title("Distribution of friends and posts")
clb=plt.colorbar()
clb.set_label('Number of Users')
plt.show()

plt.figure(2)
plt.hist2d(likes, posts,bins=30)
plt.xlabel("Number of likes")
plt.ylabel('Number of posts')
plt.title("Distribution of likes and posts")
clb=plt.colorbar()
clb.set_label('Number of Users')
plt.show()

plt.figure(3)
plt.hist2d(likes, friends,bins=20)
plt.xlabel("Number of likes")
plt.ylabel('Number of friends')
plt.title("Distribution of likes and friends")
clb=plt.colorbar()
clb.set_label('Number of Users')
plt.show()
