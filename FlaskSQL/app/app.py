from typing import List, Dict
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)


def cities_import() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'citiesData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblCitiesImport')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


@app.route('/')
def index() -> str:
    js = cities_import()
    return render_template("index.html", data=js, heading="Cities Data")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)