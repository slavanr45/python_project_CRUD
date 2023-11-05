from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash,
    get_flashed_messages,
    url_for
    )
import json

app = Flask(__name__)
app.secret_key = "secret_key"

with open('users_db.json', encoding='utf8') as file:
    users_db = json.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users_get():
    mes = get_flashed_messages(with_categories=True)
    users = users_db
    return render_template(
           'users/index.html',
           users=users,   messages=mes)


@app.route('/users/<int:id>')
def user_get(id):
    user = next(filter(lambda x: x['id'] == id, users_db), None)
    if not user:
        return 'Page not fount', 404
    return render_template(
        'users/show.html',
        user=user)


@app.route('/users/new')
def user_new():
    user = {}
    err = {}
    return render_template(
        'users/new.html',
        user=user,
        err=err)


@app.route('/users', methods=['post'])
def user_post():
    data = request.form.to_dict()
    err = validate(data)  # Проверяем данные
    if err:
        return render_template(
            'users/new.html',
            user=data,
            err=err), 422
    data['id'] = sorted(users_db, key=lambda x: x['id'])[-1].get('id', 0) + 1
    users_db.append(data)
    with open('users_db.json', 'w', encoding='utf8') as file:
        json.dump(users_db, file)
    flash('Новый пользователь был создан', 'success')
    return redirect(url_for('users_get'))


def validate(data):
    err = {}
    if not data['name'] or len(data['name']) < 3:
        err['name'] = "Can't be blank or short"
    if not data['email']:
        err['email'] = "Can't be blank"
    return err


@app.route('/users/<int:id>/edit')
def user_edit(id):
    user = next(filter(lambda x: x['id'] == id, users_db), None)
    err = {}
    return render_template(
        'users/edit.html',
        user=user,
        err=err)


@app.route('/users/<int:id>/edit', methods=['POST'])
def user_update(id):
    user = next(filter(lambda x: x['id'] == id, users_db), None)
    data = request.form.to_dict()
    err = validate(data)
    if err:
        return render_template(
            'users/edit.html',
            user=user,
            err=err), 422
    users_db.remove(user)
    user['name'] = data['name']
    user['email'] = data['email']
    users_db.append(user)
    with open('users_db.json', 'w', encoding='utf8') as file:
        json.dump(users_db, file)
    flash('User has been updated', 'success')
    return redirect(url_for('users_get'))


@app.route('/users/<int:id>/delete', methods=['POST'])
def user_delete(id):
    user = next(filter(lambda x: x['id'] == id, users_db), None)
    users_db.remove(user)
    with open('users_db.json', 'w', encoding='utf8') as file:
        json.dump(users_db, file)
    flash('User has been deleted', 'success')
    return redirect(url_for('users_get'))


@app.route('/login', methods=['post'])
def login_post():
    # working only in sessions
    return redirect(url_for('index'))


@app.route('/logout', methods=['post'])
def logout_post():
    # working only in sessions
    return redirect(url_for('index'))
