import pandas
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    filename = 'request for startup.csv'
    data = pandas.read_csv(filename, header=0)
    info = data.values
    return render_template('index.html', csv_data=info)


if __name__ == "__main__":
    app.run()
