from flask import Flask, render_template, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)



@app.route('/')
def index():
	return render_template('index.html', examples=Example.query.all());

@app.route('/create', methods=['POST'])
def create():
	example = Example('data-24')
	db.session.add(example)
	db.session.commit()

	return redirect('/')

if __name__ == '__main__':
	app.run()