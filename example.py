from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash,
    get_flashed_messages,
    url_for
    )

app = Flask(__name__)
app.secret_key = "secret_key"


users = []


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users')
def get_users():
    messages = get_flashed_messages(with_categories=True)
    return render_template(
           'users/index.html',
           users=users,
           messages=messages)


@app.route('/users/new')
def new_user():
    user = {}
    errors = {}
    return render_template(
        'users/new.html',
        user=user,
        errors=errors)


@app.post('/users')
def post_user():
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        return render_template(
          'users/new.html',
          user=user,
          errors=errors,), 422
    users.append(user)
    flash('User has been created', 'success')
    return redirect(url_for('get_users'), code=302)


def validate(user):
    err = {}
    if len(user['nickname']) <= 4:
        err['nickname'] = "Nickname must be greater than 4 characters"
    return err


# @app.route('/user/<id>/edit')
# def edit_user(id):   # обработка формы
#     user = next(filter(lambda x: x['id'] == id, users), None)
#     err = []
#     return render_template(
#            'schools/edit.html',
#            school=school,
#            err=err,  )

# END
