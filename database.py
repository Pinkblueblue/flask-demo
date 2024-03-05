from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click
from model import User,db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+ os.path.join(app.root_path,'data.db')

db.init_app(app)

@app.cli.command()
@click.option('--drop', is_flag=True, help='create data base after drop')
def createdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('initialized database')

@app.route('/add/<name>/<age>')
def addUser(name,age):

    user = User(name=name,age=age)
    db.session.add(user)
    db.session.commit()
    return 'success'

@app.route('/alluser')
def allUser():
    users = []
    for user in User.query.all():
        temp = {}
        temp['name'] = user.name
        temp['age'] = user.age
        users.append(temp)
    print(users)
    return jsonify(users)

@app.route('/getuser/<name>')
def getuser(name):
    user = User.query.filter_by(name=name).first()
    return jsonify(name=user.name,age=user.age)

@app.route('/updateuser/<name>/<age>')
def updateuser(name, age):
    for user in User.query.filter_by(name=name).all():
        user.age=age
    db.session.commit()
    return 'success'

@app.route('/deluser/<name>')
def deluser(name):
    for user in User.query.filter(User.name == name).all():
        db.session.delete(user)
    db.session.commit()
    return 'success'


        




