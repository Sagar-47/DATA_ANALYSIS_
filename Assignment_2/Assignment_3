import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

data= pd.read_csv('facebookdata.csv')
#get value of respective columns
likes=data['likes'].values
posts=data['posts'].values
friends=data['friends'].values
stddev_friends= np.std(friends)
stddev_posts= np.std(posts)
stddev_likes= np.std(likes)

plt.figure(1)
plt.hist2d(friends, posts,bins=30)
plt.xlabel("Number of friends")
plt.ylabel('Number of posts')
plt.title("Distribution of friends and posts")
cov_fp= np.cov(friends,posts)[0][1] #covariance of friends and posts
cor_fp= cov_fp/(stddev_friends*stddev_posts) #correlation of friends and posts
clb=plt.colorbar()
plt.text(1300,220,'covariance= '+str( cov_fp)+'\n correlation='+str(cor_fp)+'\n slight negative correlation')
clb.set_label('number of users')
plt.show()

plt.figure(2)
plt.hist2d(likes, posts,bins=30)
plt.xlabel("Number of likes")
plt.ylabel('Number of posts')
plt.title("Distribution of likes and posts")
cov_lp= np.cov(likes,posts)[0][1] #covariance of likes and posts
cor_lp= cov_lp/(stddev_likes*stddev_posts) #correlation of likes and posts
plt.text(620,220,'covariance= '+str( cov_lp)+'\n correlation='+str(cor_lp)+'\n positive correlation')
plt.colorbar()
plt.show()

plt.figure(3)
plt.hist2d(likes, friends,bins=20)
plt.xlabel("Number of likes")
plt.ylabel('Number of friends')
plt.title("Distribution of likes and friends")
cov_lf= np.cov(likes,friends)[0][1] #covariance of likes and friends
cor_lf= cov_lf/(stddev_likes*stddev_friends) #correlation of likes and friends
plt.text(620,1450,'covariance= '+str( cov_lf)+'\n correlation='+str(cor_lf)+'\n almost no correlation')

plt.colorbar()
plt.show()
