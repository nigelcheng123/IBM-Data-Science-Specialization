#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# Using this Python notebook you will:
# 1. Understand 3 Chicago datasets  
# 1. Load the 3 datasets into 3 tables in a Db2 database
# 1. Execute SQL queries to answer assignment questions 

# ### Connect to the database 
# Let us first load the SQL extension and establish a connection with the database

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In the next cell enter your db2 connection string. Recall you created Service Credentials for your Db2 instance in first lab in Week 3. From the __uri__ field of your Db2 service credentials copy everything after db2:// (except the double quote at the end) and paste it in the cell below after ibm_db_sa://
# 
# <img src ="https://ibm.box.com/shared/static/hzhkvdyinpupm2wfx49lkr71q9swbpec.jpg">

# In[2]:


# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name
# Enter the connection string for your Db2 on Cloud database instance below
get_ipython().run_line_magic('sql', 'ibm_db_sa://bds36432:t7fxp01hr36bvf%2Bq@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB')


# ## Problems
# Now write and execute SQL queries to solve assignment problems
# 
# ### Problem 1
# 
# ##### Find the total number of crimes recorded in the CRIME table

# In[6]:


get_ipython().run_line_magic('sql', 'select count(*) from CHICAGO_CRIME_DATA')


# ### Problem 2
# 
# ##### Retrieve first 10 rows from the CRIME table
# 

# In[4]:


get_ipython().run_line_magic('sql', 'select * from CHICAGO_CRIME_DATA fetch first 10 rows only;')


# ### Problem 3
# 
# ##### How many crimes involve an arrest?

# In[9]:


get_ipython().run_cell_magic('sql', 'select count(*) from CHICAGO_CRIME_DATA', '                           where ARREST = TRUE;')


# ### Problem 4
# 
# ##### Which unique types of crimes have been recorded at GAS STATION locations?
# 

# In[10]:


get_ipython().run_cell_magic('sql', 'select distinct PRIMARY_TYPE from CHICAGO_CRIME_DATA', "                                   where LOCATION_DESCRIPTION = 'GAS STATION'")


# Hint: Which column lists types of crimes e.g. THEFT?

# ### Problem 5
# 
# ##### In the CENUS_DATA table list all Community Areas whose names start with the letter ‘B’.

# In[18]:


get_ipython().run_cell_magic('sql', 'select COMMUNITY_AREA_NAME from CENSUS_DATA', "                                 where COMMUNITY_AREA_NAME like 'B%'")


# ### Problem 6
# 
# ##### Which schools in Community Areas 10 to 15 are healthy school certified?

# In[23]:


get_ipython().run_cell_magic('sql', 'select NAME_OF_SCHOOL from ', "(select NAME_OF_SCHOOL, HEALTHY_SCHOOL_CERTIFIED, COMMUNITY_AREA_NUMBER from CHICAGO_PUBLIC_SCHOOLS\nwhere COMMUNITY_AREA_NUMBER between 10 and 15) as COMMUNITY_10_15\nwhere HEALTHY_SCHOOL_CERTIFIED = 'Yes';")


# ### Problem 7
# 
# ##### What is the average school Safety Score? 

# In[24]:


get_ipython().run_line_magic('sql', 'select avg(SAFETY_SCORE) from CHICAGO_PUBLIC_SCHOOLS;')


# ### Problem 8
# 
# ##### List the top 5 Community Areas by average College Enrollment [number of students] 

# In[25]:


get_ipython().run_cell_magic('sql', 'select COMMUNITY_AREA_NAME, avg(COLLEGE_ENROLLMENT) as number_of_students from CHICAGO_PUBLIC_SCHOOLS', 'group by COMMUNITY_AREA_NAME order by number_of_students desc fetch first 5 rows only;')


# ### Problem 9
# 
# ##### Use a sub-query to determine which Community Area has the least value for school Safety Score? 

# In[28]:


get_ipython().run_cell_magic('sql', 'select COMMUNITY_AREA_NAME from CENSUS_DATA CD', 'where COMMUNITY_AREA_NUMBER = \n(select COMMUNITY_AREA_NUMBER from CHICAGO_PUBLIC_SCHOOLS order by SAFETY_SCORE limit 1);')


# ### Problem 10
# 
# ##### [Without using an explicit JOIN operator] Find the Per Capita Income of the Community Area which has a school Safety Score of 1.

# In[29]:


get_ipython().run_cell_magic('sql', 'select PER_CAPITA_INCOME, COMMUNITY_AREA_NAME from CENSUS_DATA', 'where COMMUNITY_AREA_NUMBER = \n(select COMMUNITY_AREA_NUMBER from CHICAGO_PUBLIC_SCHOOLS\nwhere SAFETY_SCORE = 1);')


# Copyright &copy; 2018 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
# 
