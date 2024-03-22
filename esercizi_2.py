#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('esercitazione_2/facebook.csv')


# In[3]:


df.columns


# In[4]:


#converto la colonna status_published in formato Timestamp
pd.to_datetime(df['status_published'])


# In[5]:


# Converto la colonna "status_published" in formato Timestamp
df['status_published'] = pd.to_datetime(df['status_published'])

# Formatta le date
df['status_published'] = df['status_published'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Verifica il risultato
print(df.head())


# In[6]:


# Converto la colonna "status_published" in formato Timestamp
df['status_published'] = pd.to_datetime(df['status_published'])

#informazioni sulle date delle transazioni
df['anno'] = df['status_published'].dt.year
df['mese'] = df['status_published'].dt.month
df['giorno'] = df['status_published'].dt.day
df['giorno_settimana'] = df['status_published'].dt.dayofweek
df['giorno_anno'] = df['status_published'].dt.dayofyear

print(df.head(5))


# In[7]:


df['status_published'] = pd.to_datetime(df['status_published'])

#post relativi al 2012
df_2012 = df[df['status_published'].dt.year == 2012]

print(df_2012.head(5))


# In[8]:


df['status_published'] = pd.to_datetime(df['status_published'])

#nuova colonna "giorno_settimana"
df['giorno_settimana'] = df['status_published'].dt.dayofweek

#numero di post pubblicati nel weekend
post_weekend = df[(df['giorno_settimana'] == 5) | (df['giorno_settimana'] == 6)].shape[0]

#numero di post pubblicati nel resto della settimana
post_settimana = df[(df['giorno_settimana'] >= 0) & (df['giorno_settimana'] <= 4)].shape[0]

print("Numero di post pubblicati nei weekend:", post_weekend)
print("Numero di post pubblicati nel resto della settimana:", post_settimana)


# In[9]:


df['status_published'] = pd.to_datetime(df['status_published'])

#anno dalla colonna "status_published"
df['anno'] = df['status_published'].dt.year

#primo e ultimo post pubblicati in ogni anno
first_last_posts = df.groupby('anno')['status_published'].agg(['first', 'last'])

print(first_last_posts)


# In[10]:


#"status_published" in formato Timestamp con fuso orario
df['status_published'] = pd.to_datetime(df['status_published']).dt.tz_localize('UTC')

print(df.head())


# In[11]:


df['status_published'] = pd.to_datetime(df['status_published'])

# Ordino la colonna "status_published"
df = df.sort_values(by='status_published')

#differenza di tempo tra due transazioni
df['differenza_tempo'] = df['status_published'].diff()

print(df[['status_published', 'differenza_tempo']])


# In[12]:


#tipi di post
tipi_post = df['status_type'].value_counts()

print("Numero totale di tipi di post:", len(tipi_post))
print("\nNumero di post per tipo:")
print(tipi_post)

