import pandas
from flask import Flask, render_template
import tablib
import os

app = Flask(__name__)
# dataset = tablib.Dataset()
# with open(os.path.join(os.path.dirname(__file__), 'request for startup.csv')) as f:
#     dataset.csv = f.read()


@app.route("/")
def index():
    filename = 'request for startup.csv'
    data = pandas.read_csv(filename, header=0)
    info = data.values.flatten()
    return render_template('index.html', csv_data=info)


if __name__ == "__main__":
    app.run()