#!/usr/bin/env python3
import hashlib
import os
import random
import threading
import time
import pymysql
from flask import Flask, abort, flash, redirect, request, render_template, session, url_for

import admin_bot

app = Flask(__name__)
app.secret_key = os.urandom(32)
app.config.update(SESSION_COOKIE_HTTPONLY=False)

admin_pw = None

def connect_mysql():
    conn = pymysql.connect(host='db',
                           port=3306,
                           user=os.environ['MYSQL_USER'],
                           passwd=os.environ['MYSQL_PASSWORD'],
                           db='social_media',
                           charset='utf8mb4')
    cursor = conn.cursor()
    return conn, cursor

def reset_admin_password():
    global admin_pw

    admin_pw = os.urandom(32).hex()

    db, cursor = connect_mysql()
    try:
        query = 'UPDATE Users SET password = %s WHERE username = \'admin\''
        cursor.execute(query, (hashlib.sha256(admin_pw.encode()).hexdigest(), ))
        db.commit()
    except Exception as e:
        print('error..', e, flush=True)
    finally:
        cursor.close()
        db.close()

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('get_login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

def nologin_required(f):
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('get_index'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

def get_secure_nonce():
    nonce = 0
    for i in range(4):
        nonce |= random.randint(0, 0xfffffffe) << 32 * i
    return hex(nonce)[2:].zfill(32)

@app.after_request
def add_header(response):
    nonce = get_secure_nonce()
    csp = f"default-src 'self'; " \
          f"script-src 'self' 'nonce-{nonce}' 'unsafe-inline'; " \
          f"img-src 'self'; " \
          f"style-src 'self' 'unsafe-inline'; " \
          f"object-src 'none'; " \
          f"base-uri 'none';"
    response.headers['Content-Security-Policy'] = csp
    return response


@app.route('/', methods=['GET'])
@login_required
def get_index():
    conn, cursor = connect_mysql()
    try:
        query = 'SELECT Posts.post_id, Posts.content, Posts.created_at, Users.username, COUNT(Likes.like_id) AS like_count FROM Posts JOIN Users ON Posts.user_id = Users.user_id LEFT JOIN Likes ON Posts.post_id = Likes.post_id GROUP BY Posts.post_id, Posts.content, Posts.created_at, Users.username'
        cursor.execute(query)
        posts = cursor.fetchall()
    except Exception as e:
        print(e, flush=True)
        abort(500)
    finally:
        cursor.close()
        conn.close()

    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET'])
@nologin_required
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
@nologin_required
def post_login():
    username = request.form['username']
    password = request.form['password']

    if username is None or username == '' or password is None or password == '':
        abort(400)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn, cursor = connect_mysql()
    try:
        query = 'SELECT * FROM Users WHERE username = %s AND password = %s'
        cursor.execute(query, (username, hashed_password))
        user = cursor.fetchone()
    except Exception as e:
        print(e, flush=True)
        abort(500)
    finally:
        cursor.close()
        conn.close()

    if user:
        session['logged_in'] = True
        session['user_id'] = user[0]
        session['username'] = username
        session['role_id'] = user[2]
        return redirect(url_for('get_index'))

    flash('Invalid username or password')
    return redirect(url_for('get_login'))


@app.route('/register', methods=['GET'])
@nologin_required
def get_register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
@nologin_required
def post_register():
    username = request.form['newUsername']
    password = request.form['newPassword']

    if username is None or username == '' or password is None or password == '':
        abort(400)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn, cursor = connect_mysql()
    try:
        query = "INSERT INTO Users (username, role_id, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, 1, hashed_password))
        conn.commit()
    except Exception as e:
        print(e, flush=True)
        abort(500)
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('get_login'))


@app.route('/create_post', methods=['POST'])
@login_required
def post_create_post():
    post_text = request.form['postText']

    if post_text is None or post_text == '':
        abort(400)

    conn, cursor = connect_mysql()
    try:
        query = "INSERT INTO Posts (user_id, content) VALUES (%s, %s)"
        cursor.execute(query, (session['user_id'], post_text))
        conn.commit()
    except Exception as e:
        print(e, flush=True)
        abort(500)
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('get_index'))


@app.route('/like_post', methods=['POST'])
@login_required
def post_like_post():
    post_id = request.form['post_id']
    if post_id is None or not isinstance(post_id, str) or not post_id.isdigit():
        abort(400)

    conn, cursor = connect_mysql()
    try:
        query = 'SELECT * FROM Likes WHERE post_id = %s AND user_id = %s'
        cursor.execute(query, (post_id, session['user_id']))
        like = cursor.fetchone()
    except Exception as e:
        print(e, flush=True)
        abort(500)
    finally:
        cursor.close()
        conn.close()

    if like:
        conn, cursor = connect_mysql()
        try:
            query = 'DELETE FROM Likes WHERE post_id = %s AND user_id = %s'
            cursor.execute(query, (post_id, session['user_id']))
            conn.commit()
        except Exception as e:
            print(e, flush=True)
            conn.rollback()
            abort(500)
        finally:
            cursor.close()
            conn.close()

    else:
        conn, cursor = connect_mysql()
        try:
            query = "INSERT INTO Likes (post_id, user_id) VALUES (%s, %s)"
            cursor.execute(query, (post_id, session['user_id']))
            conn.commit()
        except Exception as e:
            print(e, flush=True)
            abort(500)
        finally:
            cursor.close()
            conn.close()

    return redirect(url_for('get_index'))


@app.route('/report_post', methods=['POST'])
@login_required
def post_report_post():
    post_id = request.form['post_id']
    if post_id is None or not isinstance(post_id, str) or not post_id.isdigit():
        abort(400)

    conn, cursor = connect_mysql()
    try:
        query = "INSERT INTO Reports (post_id, reported_by_user_id) VALUES (%s, %s)"
        cursor.execute(query, (post_id, session['user_id']))
        conn.commit()
    except Exception as e:
        print(e, flush=True)
        abort(500)
    finally:
        cursor.close()
        conn.close()

    admin_bot.read_reports()

    return render_template('report_completed.html')


@app.route('/reports', methods=['GET'])
@login_required
def get_reports():
    if session['role_id'] != 2:
        abort(404)

    conn, cursor = connect_mysql()
    try:
        query = 'SELECT Reports.report_id, Users.username AS reporter, Posts.content AS post_content, Reports.reported_at FROM Reports JOIN Users ON Reports.reported_by_user_id = Users.user_id JOIN Posts ON Reports.post_id = Posts.post_id ORDER BY Reports.reported_at DESC'
        cursor.execute(query)
        reports = cursor.fetchall()
    except Exception as e:
        print(e, flush=True)
        abort(500)
    finally:
        cursor.close()
        conn.close()

    conn, cursor = connect_mysql()
    try:
        query = 'DELETE FROM Reports'
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e, flush=True)
        conn.rollback()
        abort(500)
    finally:
        cursor.close()
        conn.close()

    return render_template('reports.html', reports=reports)

@app.route('/admin', methods=['GET'])
@login_required
def get_admin():
    if session['role_id'] != 2:
        abort(404)

    return open('flag').read()

time.sleep(5)
reset_admin_password()
thd = threading.Thread(target=admin_bot.login, args=(admin_pw, ))
thd.start()
