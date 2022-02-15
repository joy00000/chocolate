#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        sugar = request.form.get("sugar")
        milk = request.form.get("milk")
        #print(sugar, milk)
        model = joblib.load("CTaste")
        pred = model.predict([[float(sugar), float(milk)]])
        #print(pred)
        pred = pred[0]
        
        if pred == 1:
            res = "good!"
        else:
            res = "bad :("
            
        s = ("Predicted taste is: " + res)
        return (render_template("index.html", result = s))
    else: 
        return (render_template("index.html", result = "Predict Chocolate Taste"))


# In[4]:


app.run()


# In[ ]:




