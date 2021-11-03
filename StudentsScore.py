#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  


# In[10]:


dataset = pd.read_csv('C:\\Users\\srushti\\py proj\\student_scores.csv')


# In[9]:


dataset.shape


# In[5]:


dataset.head() 


# In[6]:


dataset.describe() 


# In[8]:


dataset.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()


# In[6]:


X = dataset.iloc[:, :-1].values  
y = dataset.iloc[:, 1].values  


# In[7]:


from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  


# In[8]:


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)  


# In[9]:


print(regressor.intercept_)


# In[10]:


print(regressor.coef_)  


# In[11]:


y_pred = regressor.predict(X_test)  


# In[12]:


df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(df) 


# In[13]:


from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))  

