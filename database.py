from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+ os.path.join(app.root_path,'data.db')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)

@app.cli.command()
@click.option('--drop', is_flag=True, help='create data base after drop')
def createdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('initialized database')

