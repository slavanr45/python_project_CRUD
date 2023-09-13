from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash,
    get_flashed_messages,
    session,
    url_for
    )

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route('/')
def index():
    if 'users_DB' not in session:
        session['users_DB'] = []
    if not session.modified:
        session.modified = True
    print(session)
    mes = get_flashed_messages(with_categories=True)
    return render_template(
        'index.html',   messages=mes)


@app.route('/users')
def users_get():
    if session.get('password', None) != '123':
        flash('Для продолжения авторизируйтесь', 'error')
        return redirect(url_for('index'))
    mes = get_flashed_messages(with_categories=True)
    users = session['users_DB']
    return render_template(
           'users/index.html',
           users=users,   messages=mes)


@app.route('/users/<int:id>')
def user_get(id):
    user = next(filter(lambda x: x['id'] == id, session['users_DB']), None)
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
    if session['users_DB']:
        data['id'] = sorted(session['users_DB'], key=lambda x: x['id'])[-1].get('id', 0) + 1
    else:
        data['id'] = 1
    session['users_DB'].append(data)
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
    user = next(filter(lambda x: x['id'] == id, session['users_DB']), None)
    err = {}
    return render_template(
        'users/edit.html',
        user=user,
        err=err)


@app.route('/users/<int:id>/edit', methods=['POST'])
def user_update(id):
    user = next(filter(lambda x: x['id'] == id, session['users_DB']), None)
    data = request.form.to_dict()
    err = validate(data)
    if err:
        return render_template(
            'users/edit.html',
            user=user,
            err=err), 422
    session['users_DB'].remove(user)
    user['name'] = data['name']
    user['email'] = data['email']
    session['users_DB'].append(user)
    flash('User has been updated', 'success')
    return redirect(url_for('users_get'))


@app.route('/users/<int:id>/delete', methods=['POST'])
def user_delete(id):
    user = next(filter(lambda x: x['id'] == id, session['users_DB']), None)
    session['users_DB'].remove(user)
    flash('User has been deleted', 'success')
    return redirect(url_for('users_get'))


@app.route('/login', methods=['post'])
def login_post():
    data = request.form.to_dict()
    session['password'] = data['password']
    if session.get('password', None) != '123':
        flash('Ошибочный пароль. Авторизация не выполнена', 'error')
    else:
        flash('Авторизация успешна. Доступуп открыт', 'success')
    return redirect(url_for('index'))


@app.route('/logout', methods=['post'])
def logout_post():
    session.pop('password')
    flash('Выход выполнен', 'success')
    return redirect(url_for('index'))
