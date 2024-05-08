from flask import Flask,request,render_template
import pickle

# Importar los modelos
model = pickle.load(open('pickle_files/model.pkl','rb'))

# crear flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    gender = request.form['gender']
    ssc_p = request.form['ssc_p']
    hsc_p = request.form['hsc_p']
    degree_p = request.form['degree_p']
    workex = request.form['workex']
    etest_p = request.form['etest_p']
    specialisation = request.form['specialisation']
    mba_p = request.form['mba_p']

    def prediction(gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p):
        gender = 0 if "F" else 0
        workex = 1 if "Yes" else 0
        specialisation = 0 if "Mkt&Fin" else 1
        data = [[gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p]]
        prediction = model.predict(data)
        return prediction

    prediction = prediction(gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation,mba_p)

    if prediction[0] == 1:
        result = 'Contratado'
    else:
        result = 'No Contratado'
    return render_template('index.html',result = result)


# python main
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)