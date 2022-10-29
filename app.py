from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ilia:password@localhost/assignments/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app = Flask(__name__)



@app.route('/add')
def add_data():
    return 0


@app.route('/update')
def update_data():
    return 0


@app.route('/delete')
def delete_data():
    return 0


@app.route('/view')
def view_data():
    return 0


if __name__ == '__main__':
    app.run()
