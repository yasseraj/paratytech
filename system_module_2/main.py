import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    dummy_times = [datetime.datetime(2021, 12, 7, 10, 0, 0),
                   datetime.datetime(2021, 12, 8, 10, 30, 0),
                   datetime.datetime(2021, 12, 9, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
