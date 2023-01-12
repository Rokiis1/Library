from flask import request, jsonify
from psycopg2 import sql
from database.__init__ import connection, app
from flask_jwt_extended import create_access_token


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    cursor = connection.cursor()

    query = sql.SQL(
        "SELECT * FROM users WHERE username = {} AND password = {}")
    cursor.execute(query.format(sql.Identifier(
        data['username']), sql.Identifier(data['password'])))

    user = cursor.fetchone()
    if user:
        access_token = create_access_token(identity=user[1])
        return jsonify(message="Login succeeded!", access_token=access_token), 200
    else:
        return jsonify(message="Invalid username or password"), 401


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    cursor = connection.cursor()

    query = sql.SQL(
        "INSERT INTO users (username, email, password) VALUES ({}, {}, {})")
    cursor.execute(query.format(sql.Identifier(data['username']), sql.Identifier(
        data['email']), sql.Identifier(data['password'])))

    connection.commit()
    return jsonify(message="User created successfully"), 201
