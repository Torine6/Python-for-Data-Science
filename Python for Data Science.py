#!/usr/bin/env python
# coding: utf-8

# These are sample codes for getting started in Python for Data Science

# In[1]:


print('Hello World!')


# $a = b + c$

# # Variables

# In[5]:


x = 3


# In[6]:


get_ipython().run_line_magic('whos', '')


# In[7]:


print(type(x))


# In[8]:


x = 4.6


# In[9]:


get_ipython().run_line_magic('whos', '')


# In[10]:


print(type(x))


# In[11]:


abcd = 895.79


# In[12]:


get_ipython().run_line_magic('whos', '')


# In[13]:


a, b, c, d, e, f = 1, 2, 3, 4, 5, 6


# In[14]:


get_ipython().run_line_magic('whos', '')


# In[15]:


del abcd


# In[16]:


get_ipython().run_line_magic('whos', '')


# In[17]:


print(abcd)


# In[18]:


c = 4+6j


# In[19]:


print(type(c))


# In[20]:


i = 'Hello, how are you?'


# In[21]:


print(type(i))


# # Operators

# In[22]:


get_ipython().run_line_magic('whos', '')


# In[23]:


sumOfaAndb = a + b


# In[24]:


print(sumOfaAndb)


# In[25]:


type(sumOfaAndb)


# In[27]:


type(a + x)


# In[28]:


z = ((a + x)**3)/4


# In[29]:


print(z)


# In[31]:


x1 = 'Good'
x2 = ' morning.'
x3 = x1 + x2
print(x3)


# In[32]:


10//3


# In[33]:


_


# # Type bool and Comparisons

# In[1]:


w = True
y = True
z = False


# In[2]:


get_ipython().run_line_magic('whos', '')


# In[3]:


print(w and y)
print(w and z)
print(z and w)


# In[4]:


d = w or z
print(d)


# In[5]:


not(w)


# In[6]:


not(y)


# In[7]:


not(z)


# In[8]:


t = not(d)


# In[9]:


type(t)


# In[10]:


print(t)


# In[12]:


not((w and y) or (z or d))


# In[13]:


print(2 < 3)


# In[14]:


c = 2 < 3
print(type(c))
print(c)


# In[15]:


d = 3==4


# In[16]:


print(d)


# In[17]:


5 == 5.0


# In[18]:


x = 4
y = 7
z = 9.3
r = -5


# In[19]:


(x < y) and (z < y) or (r == x)


# In[20]:


print((not(2!=3) and True) or (False and True))


# # Functions

# In[21]:


divmod(22, 10)


# In[23]:


g = divmod(37, 9)


# In[24]:


print(g)


# In[25]:


type(g)


# In[26]:


g[0]


# In[27]:


g[1]


# In[28]:


round(3.412)


# In[29]:


isinstance(4, int)


# In[31]:


isinstance(2.4, (float, int))


# In[32]:


isinstance(2 + 3j,(int, float, str))


# In[33]:


pow(3, 3)


# In[36]:


pow(3, 3, 4)


# In[1]:


c = input('Enter a number: ')


# In[ ]:




