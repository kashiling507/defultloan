# from flask import Flask, render_template, request
# from joblib import load

# app = Flask(__name__)

# # Load the trained model
# model = load('C:/Users/Lenovo/Desktop/cc/templates/trained_model.joblib')

# @app.route("/")
# def home():
#     return render_template('index.html')

# @app.route('/process_data', methods=['POST'])
# def process_data():
#     # Get the input values from the form
#     id = int(request.form['id'])
#     limit_bal = int(request.form['limit_bal'])
#     sex = int(request.form['sex'])
#     education = int(request.form['education'])
#     marriage = int(request.form['marriage'])
#     age = int(request.form['age'])
#     pay_0 = int(request.form['pay_0'])
#     pay_2 = int(request.form['pay_2'])
#     pay_3 = int(request.form['pay_3'])
#     pay_4 = int(request.form['pay_4'])
#     pay_5 = int(request.form['pay_5'])
#     pay_6 = int(request.form['pay_6'])
#     bill_amt1 = int(request.form['bill_amt1'])
#     bill_amt2 = int(request.form['bill_amt2'])
#     bill_amt3 = int(request.form['bill_amt3'])
#     bill_amt4 = int(request.form['bill_amt4'])
#     bill_amt5 = int(request.form['bill_amt5'])
#     bill_amt6 = int(request.form['bill_amt6'])
#     pay_amt1 = int(request.form['pay_amt1'])
#     pay_amt2 = int(request.form['pay_amt2'])
#     pay_amt3 = int(request.form['pay_amt3'])
#     pay_amt4 = int(request.form['pay_amt4'])
#     pay_amt5 = int(request.form['pay_amt5'])
#     pay_amt6 = int(request.form['pay_amt6'])
#     if 'default.payment.next.month' in request.form:
#         default_payment_next_month = int(request.form['default.payment.next.month'])



#     # Create a list of features
#     features = [[id, limit_bal, sex, education, marriage, age, pay_0, bill_amt1, pay_amt1,
#                  pay_2, bill_amt2, pay_amt2, pay_3, bill_amt3, pay_amt3, pay_4, bill_amt4,
#                  pay_amt4, pay_5, bill_amt5, pay_amt5, pay_6, bill_amt6, pay_amt6, default_payment_next_month]]

#     # Make the prediction
#     prediction = model.predict(features)

#     # Return the prediction as a string
#     if prediction == 0:
#         result = "Not Defaulted"
#     else:
#         result = "Defaulted"

#     return render_template('result.html', prediction=result, id=id)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('C:/Users/sonaw/Downloads/cc (2)/cc/templates/trained_model.joblib')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    # Get the input values from the form
    id = int(request.form['id'])
    limit_bal = int(request.form['limit_bal'])
    sex = int(request.form['sex'])
    education = int(request.form['education'])
    marriage = int(request.form['marriage'])
    age = int(request.form['age'])
    pay_0 = int(request.form['pay_0'])
    pay_2 = int(request.form['pay_2'])
    pay_3 = int(request.form['pay_3'])
    pay_4 = int(request.form['pay_4'])
    pay_5 = int(request.form['pay_5'])
    pay_6 = int(request.form['pay_6'])
    bill_amt1 = int(request.form['bill_amt1'])
    bill_amt2 = int(request.form['bill_amt2'])
    bill_amt3 = int(request.form['bill_amt3'])
    bill_amt4 = int(request.form['bill_amt4'])
    bill_amt5 = int(request.form['bill_amt5'])
    bill_amt6 = int(request.form['bill_amt6'])
    pay_amt1 = int(request.form['pay_amt1'])
    pay_amt2 = int(request.form['pay_amt2'])
    pay_amt3 = int(request.form['pay_amt3'])
    pay_amt4 = int(request.form['pay_amt4'])
    pay_amt5 = int(request.form['pay_amt5'])
    pay_amt6 = int(request.form['pay_amt6'])
    default_payment_next_month = int(request.form.get('default.payment.next.month', 0))

    # Create a list of features
    features = [[id, limit_bal, sex, education, marriage, age, pay_0, bill_amt1, pay_amt1,
                 pay_2, bill_amt2, pay_amt2, pay_3, bill_amt3, pay_amt3, pay_4, bill_amt4,
                 pay_amt4, pay_5, bill_amt5, pay_amt5, pay_6, bill_amt6, pay_amt6, default_payment_next_month]]

    # Make the prediction
    prediction = model.predict(features)

    # Return the prediction as a string
    if prediction == 0:
        result = "Not Defaulted"
    else:
        result = "Defaulted"

    return render_template('result.html', prediction=result, id=id)

if __name__ == '__main__':
    app.run(debug=True)
