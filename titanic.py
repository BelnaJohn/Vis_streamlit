# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:22:58 2020

@author: USER
"""
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline 
st.write('titanic data explanatory analysis')
train=pd.read_csv('train.csv')
st.title('Data')
st.write(train)

train.isnull()
a=sns.heatmap(train.isnull(),yticklabels=False,cbar=False)
st.write(a)
#hist_values = np.histogram(train.isnull())
#st.bar_chart(hist_values)
b=sns.countplot(x="Survived",data=train)
st.write(b)
st.write("less people survived")
sns.countplot(x='Survived',hue='Sex',data=train)
st.write("more female survived than male")
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')
st.write("Rich people survived more")
sns.distplot(train['Age'].dropna(),kde=False,bins=40)
st.write("more people travelled was in 15-40 age group.")
sns.countplot(x='SibSp',data=train)
sns.boxplot(x='Pclass',y='Age',data=train)