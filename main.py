import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features)]
    prediction = model.predict(final_features)
    
    if prediction==1:
        return render_template('index.html',prediction_text='You have cardio')
    else:
        return render_template('index.html',prediction_text="You Don't Have cardio")
        
if __name__=='__main__':
    app.run(debug=True,port=2020)
    
        
        