#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import pandas as pd
import io


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
api = Api(app)

tbl = '''
id,name,looks
1,Taro,Hage
2,Jiro,Mottohage
3,Saburo,Suggokuhage
'''


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    looks = db.Column(db.String(80), unique=False)

    def __init__(self, name, looks):
        self.name = name
        self.looks = looks

    def __repr__(self):
        return '{{"class": "{}", "id": "{}", "name": "{}", "looks": "{}"}}'.format(__class__.__name__, self.id, self.name, self.looks)


class My_Resource(Resource):
    def get(self, id, name, looks):
        if id != "-":
            user = User.query.get(id)
            if isinstance(user, type(None)):
                return jsonify({'r': 'GET fail, no id found', 'id': id}), 403

        else:
            user = User.query.filter_by(name=name).first()
            if isinstance(user, type(None)):
                return jsonify({'r': 'GET fail, no name found', 'name': name}), 403

        r = {
            'r': 'GET success',
            'id': user.id,
            'name': user.name,
            'looks': user.looks
        }

        return jsonify(r), 200
        # return make_response(json.dumps(result, ensure_ascii=False))

    def put(self, id, name, looks):
        if id != "-":
            user = User.query.get(id)
            if isinstance(user, type(None)):
                return jsonify({'r': 'PUT fail, no id found', 'id': id}), 403

            user.name = name
            user.looks = looks

        else:
            user = User.query.filter_by(name=name).first()
            if isinstance(user, type(None)):
                user = User(name=name, looks=looks)
            else:
                user.looks = looks

            db.session.add(user)
            db.session.commit()
            return jsonify({'r': 'PUT success', 'id': user.id, 'name': name, 'looks': looks}), 200

    def delete(self, id, name, looks):
        user = User.query.get(id)
        if isinstance(user, type(None)):
            return jsonify({'r': 'DELETE fail, no id found', 'id': id}), 403

        db.session.delete(user)
        db.session.commit()
        return jsonify({'r': 'DELETE success'}), 200


api.add_resource(My_Resource, '/sqlalc/<string:id>/<string:name>/<string:looks>')


@app.route('/sqlalc/', methods=['GET'])
def all():
    d = {'r': 'GET success'}
    d['data'] = [{'id': i.id, 'name': i.name, 'looks': i.looks} for i in User.query.all()]
    return jsonify(d), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({'r': '404 Not found'}), 404


if __name__ == '__main__':
    db.create_all()
    # df = pd.read_csv(io.StringIO(tbl))
    # df.to_sql('users', db.engine.connect(), index=False, if_exists='replace')
    app.run(debug=True, port=8000)
