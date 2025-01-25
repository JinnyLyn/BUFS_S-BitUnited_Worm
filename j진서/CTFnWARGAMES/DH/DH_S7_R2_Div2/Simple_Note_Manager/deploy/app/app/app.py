#!/usr/bin/env python3
import subprocess
import threading
import time
from flask import Flask, make_response, redirect, request, abort, render_template, url_for

app = Flask(__name__)

lock = threading.Lock()
new_note_id = 0
notes = {}

def create_note(content):
    global new_note_id
    with lock:
        note_id = new_note_id
        new_note_id += 1
        notes[note_id] = content
        return notes[note_id]

def read_note(note_id):
    with lock:
        return notes[note_id]

def update_note(note_id, content):
    with lock:
        notes[note_id] = content
        return notes[note_id]

def delete_note(note_id):
    with lock:
        del notes[note_id]

def backup_notes(timestamp):
    with lock:
        with open('./tmp/notes.tmp', 'w') as f:
            f.write(repr(notes))
        subprocess.Popen(f'cp ./tmp/notes.tmp /tmp/{timestamp}', shell=True)


@app.route('/', methods=['GET'])
def get_index():
    return render_template('notes.html', notes=notes)


@app.route('/notes', methods=['GET'])
def get_notes():
    return render_template('notes.html', notes=notes)


@app.route('/create_note', methods=['GET'])
def get_create_note():
    return render_template('create_note.html')


@app.route('/create_note', methods=['POST'])
def post_create_note():
    content = request.form.get('content')
    if not isinstance(content, str):
        abort(400)
    create_note(content)
    return redirect(url_for('get_index'))


@app.route('/update_note', methods=['GET'])
def post_update_note():
    if len(notes) == 0:
        abort(404)
    return render_template('update_note.html')


@app.route('/update_note', methods=['POST'])
def get_update_note():
    note_id = request.form.get('note_id')
    if not isinstance(note_id, str) or not note_id.isdigit():
        abort(400)
    note_id = int(note_id)
    if note_id not in notes:
        abort(404)
    content = request.form.get('content')
    if not isinstance(content, str):
        abort(400)
    update_note(note_id, content)
    return redirect(url_for('get_index'))


@app.route('/delete_note', methods=['GET'])
def get_delete_note():
    if len(notes) == 0:
        abort(404)
    return render_template('delete_note.html')


@app.route('/delete_note', methods=['POST'])
def post_delete_note():
    note_id = request.form.get('note_id')
    if not isinstance(note_id, str) or not note_id.isdigit():
        abort(400)
    note_id = int(note_id)
    if note_id not in notes:
        abort(404)
    delete_note(note_id)
    return redirect(url_for('get_index'))


@app.route('/backup_notes', methods=['GET'])
def get_backup_notes():
    print(len(notes), flush=True)
    if len(notes) == 0:
        abort(404)
    page = render_template('backup_notes.html')
    resp = make_response(page)
    resp.set_cookie('backup-timestamp', f'{time.time()}')
    return resp


@app.route('/backup_notes', methods=['POST'])
def post_backup_notes():
    if len(notes) == 0:
        abort(404)
    backup_timestamp = request.cookies.get('backup-timestamp', f'{time.time()}')
    if not isinstance(backup_timestamp, str):
        abort(400)
    backup_notes(backup_timestamp)
    return redirect(url_for('get_index'))
