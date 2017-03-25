from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Example(db.Model):
	__tablename__ = 'example'
	id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
	data = db.Column('data', db.Unicode)

	def __init__(self, data):
		self.data = data
