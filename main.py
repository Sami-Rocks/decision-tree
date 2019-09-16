from flask import Flask
import pickle


app = Flask(__name__)

@app.route("/")

def hello():

    model_file = open('model.sav', 'rb')
    data = pickle.load(model_file)

    p = [[658.06, 541299235, 502757091]]
    pr =  data.predict(p)
    return pr


if __name__ == '__main__':
    app.run(debug=True)