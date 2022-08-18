#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask,request,render_template


# In[8]:


app = Flask(__name__)


# In[9]:


import joblib


# In[10]:


@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        #after press enter come here
           
        return(render_template("index.html",result1=r1,result2=r2))
    else: 
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




