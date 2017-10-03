import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

data= pd.read_csv('facebookdata.csv')
#get value of respective columns
likes=data['likes'].values
posts=data['posts'].values
friends=data['friends'].values
stddev_friends= np.std(friends) #Standard Deviation for friends
stddev_posts= np.std(posts) #Standard Deviation for posts
stddev_likes= np.std(likes) #Standard Deviation for likes

plt.figure(1)
plt.xlabel("Number of friends")
plt.ylabel('Number of posts')

cov_fp= np.cov(friends,posts) #covariance matrix of friends and posts
cov_fp_1= np.cov(friends,posts)[0][1] #covariance of friends and posts only
cor_fp= cov_fp_1/(stddev_friends*stddev_friends) #correlation of friends and posts
plt.text(0.2,0.5,'covariance= '+str( cov_fp)+'\n\n correlation='+str(cor_fp)+'\n\n slight negative correlation')

plt.show()


plt.figure(2)

plt.xlabel("Number of likes")
plt.ylabel('Number of posts')

cov_lp= np.cov(likes,posts) #covariance matrix  of likes and posts
cov_lp_1= np.cov(likes,posts)[0][1] #covariance of likes and posts only
cor_lp= cov_lp_1/(stddev_likes*stddev_posts) #correlation of likes and posts
plt.text(0.2,0.5,'covariance= '+str( cov_lp)+'\n\n correlation='+str(cor_lp)+'\n \npositive correlation')

plt.show()

plt.figure(3)

plt.xlabel("Number of likes")
plt.ylabel('Number of friends')

cov_lf= np.cov(likes,friends) #covariance matrix  of likes and friends
cov_lf_1= np.cov(likes,friends)[0][1] #covariance of likes and friends only
cor_lf= cov_lf_1/(stddev_likes*stddev_friends) #correlation of likes and friends
plt.text(0.2,0.5,'covariance= '+str( cov_lf)+'\n\n correlation='+str(cor_lf)+'\n\n almost no correlation')

plt.show()
