import pickle
from flask import Flask, render_template, request
app = Flask('__name__')
knnmodelobject = pickle.load(open("knnnModel.pickle", "rb"))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', result1="")
    elif request.method == 'POST':
        sepallength = request.form['sepallength']
        sepalwidth = request.form['sepalwidth']
        petallength = request.form['petallength']
        petalwidth = request.form['petalwidth']
        print(sepallength, sepalwidth, petallength, petalwidth)
        result = knnmodelobject.predict(
            [[sepallength, sepalwidth, petallength, petalwidth]])
        target = ['setosa', 'versicolor', 'virginica']
        print(target[result[0]])
        return render_template('index.html', result1=target[result[0]])


if __name__ == '__main__':
    app.run(debug=True)
