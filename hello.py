from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello1 World!'


@app.route('/hello')
def hello():
    return 'Hello Hello Hello'


@app.route('/hello/<name>')         # 这个变量还可以指定为整型和浮点型，这样写<int:xxx>、<float:xxx>
def hello_name(name):
    return f'hello {name}'


if __name__ == '__main__':
    app.run(debug=True)
