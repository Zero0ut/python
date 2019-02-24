from flask import Flask, render_template, jsonify
from random import sample
from flask_pymongo import PyMongo
import logging, sys

app = Flask(__name__)

#app.config['MONGO_DBAME'] = 'prettyprinted_chartist'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/prettyprinted_chartist'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('chart.html')

@app.route('/data')
def data():
    charts = mongo.db.charts

    result = charts.find_one({'name' : 'Chart2'})

    # Hardcode Values
    #return jsonify({'results' : sample(range(1,10), 5)})

    # Fetch from MongoDB
    return jsonify({'results' : result['values']})


if __name__ == '__main__':
    app.run(debug=True)
