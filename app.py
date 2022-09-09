from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1> Здравствуй Flask </h1> <p> Second string </p> \
    <table border="1px solid black"> <tr>  <th> Someone </th> <th> Here  </th> </tr> <tr>  <th> Someone </th> <th> Here  </th> </tr> </table>'


@app.route('/hello')
def greeting():
    return 'Hello Коля'


if __name__ == '__main__':
    app.run(debug=True)
