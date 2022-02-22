from datetime import datetime
from todolist import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(30))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)


class CompletedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(30))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
