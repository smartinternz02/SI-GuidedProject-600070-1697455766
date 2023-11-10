from flask import Flask, render_template, request
app=Flask(__name__)
import pickle
import numpy as np
model=pickle.load(open('model1.pkl','rb'))
@app.route('/')
def start():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login():
    p=request.form["qe"]
    q=request.form["ae"]
    r=request.form["qf"]
    s=request.form["pb"]
    t=request.form["in"]
    u=request.form["ct"]
    v=request.form["pt"]
    w=[[float(p), float(q), float(r), float(s), float(t), float(u), float(v)]]
    output=model.predict(w)
    print(output)
    return render_template("index.html",y="The predicted university score is "+str(round(output[0],3)))

if __name__=='__main__':
    app.run(debug=True)
