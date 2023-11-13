from flask import Flask, render_template

app = Flask(__name__)


@app.route('/result')
def result():
    dict = {'phy': 59, 'che': 60, 'maths': 90}
    return render_template('result.html',result=dict)


if __name__ == '__main__':
    app.run(debug=True)