
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import joblib


# In[26]:


dataset = pd.read_csv('website_classification.csv')
print("\nDataset:\n",dataset.head())


# In[27]:


df=pd.DataFrame(dataset)
df.drop(["Unnamed: 0","website_url"],axis=1,inplace=True)
print("\nDataset After feature selection:\n",df.head())


# In[28]:


x=df["cleaned_website_text"]
print("\nDataset Feature values(x values):\n",x.head())

x.to_csv("dat.csv")
# In[29]:


df["Category"].unique()


# In[30]:


le=LabelEncoder()


# In[31]:


le.fit(df["Category"])


# In[32]:


file=open("labels.pickle","wb")
joblib.dump(le,file)
file.close()


# In[33]:


print("\nDataset Labels:(y values)\n",list(le.classes_))


# In[34]:


y=le.transform(df["Category"])
y


# In[35]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15)


# In[36]:


#print("\nFeatures Training Data:\n",x_train.head())


# In[37]:


#print("\nFeatures Testing Data:\n",x_test.head())


# In[38]:


#print("\nLabel Training Data:\n",y_train)


# In[39]:


#print("\nLabel Testing Data:\n",y_test)


# In[40]:


tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(x_train)
file=open("tokenizer.pickle","wb")
joblib.dump(tfidf_vectorizer,file)
file.close()


# In[41]:


tfidf_test = tfidf_vectorizer.transform(x_test)


# In[42]:


from sklearn.svm import SVC # "Support vector classifier"  
classifier = SVC(kernel='linear', random_state=0)  
classifier.fit(tfidf_train, y_train)


# In[43]:


file=open("model.pickle","wb")
joblib.dump(classifier,file)
file.close()

print("Testing value:\n",tfidf_test)
# In[44]:


y_pred= classifier.predict(tfidf_test)
print("\npredicted value:\n",y_pred)

# In[45]:


print(classification_report(y_test,y_pred))


# In[46]:


print("\nAccuracy:",round(accuracy_score(y_test,y_pred),4)*100,"%")


# In[47]:


#print(confusion_matrix(y_test,y_pred))
"""file=open("input.txt","r",encoding='utf-8')
text=file.read()
file.close()

dat=pd.DataFrame({'text':[text]})

dat=tfidf_vectorizer.transform(dat)

pred= classifier.predict(dat)
print("\npredicted value:\n",pred)"""
