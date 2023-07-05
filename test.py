
# coding: utf-8

# In[25]:


import pandas as pd
import joblib
import re


# In[26]:

"""
file=open("input.txt","r",encoding='utf-8')
text=file.read()
file.close()
print("\nInput:\n",text)"""

# In[27]:
import urllib.request 
from bs4 import BeautifulSoup
import pandas as pd

file=open("input.txt","r",encoding='utf-8')
url=file.read()
file.close()
#print("\nInput:\n",text)

x=[]
# providing url
#url = "https://www.booking.com/index.html?aid=1743217"

  
# opening the url for reading
try:
    html = urllib.request.urlopen(url)
except:
    file=open("out.txt","w")
    file.write("web scrapping not supported")
    file.close()
    exit()
    
# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')
  
# getting all the paragraphs
for para in htmlParse.find_all("p"):
    x.append(para.get_text())

text=""
for i in x:
    text+=" "+str(i)
text=text.strip()
    
#print(text)
df=pd.DataFrame({'text':[text]})
df

def preprocess_text(sen):
    sentence = remove_tags(sen)
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    return sentence
	
TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)
	
X = []
sentences = list(df['text'])
for sen in sentences:
    X.append(preprocess_text(sen))
print(X)
df=pd.DataFrame({'text':[X[0]]})
df

"""df=pd.DataFrame({'text':[text]})"""
x=df['text']
x


# In[28]:


file=open("tokenizer.pickle","rb")
tfidf_vectorizer=joblib.load(file)
file.close()


# In[29]:


file=open("labels.pickle","rb")
le=joblib.load(file)
file.close()


# In[30]:


file=open("model.pickle","rb")
classifier=joblib.load(file)
file.close()


# In[31]:


tfidf_test = tfidf_vectorizer.transform(x)
print("\nTokenized Input Text:\n",tfidf_test)

# In[32]:


y_pred= classifier.predict(tfidf_test)


# In[35]:


out=le.inverse_transform(y_pred)
print(le.classes_)

# In[38]:


print("\nOutput:\n",out[0])

file=open("out.txt","w")
file.write(out[0])
file.close()

